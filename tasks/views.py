from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Task
from datetime import datetime, date, timedelta
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django.views.generic import TemplateView
from django.utils import timezone
from django.core.exceptions import PermissionDenied


class TaskListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    ordering = '-created_at'

    def get_queryset(self):
        # Se o usuário for admin (is_staff), ele verá todas as tarefas.
        if self.request.user.is_staff:
            return Task.objects.all()
        # Se o usuário não for admin, ele verá apenas suas próprias tarefas.
        else:
            return Task.objects.filter(usuario=self.request.user)


# View para ver detalhes da tarefa
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'


# View para criar uma nova tarefa
class TaskCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Task
    form_class = TaskForm
    template_name = 'tasks/addtask.html'
    success_url = reverse_lazy('calendar')

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()  # Admin vê todas as tarefas
        else:
            return Task.objects.filter(usuario=self.request.user)  # Usuário vê apenas suas próprias tarefas


# View para editar uma tarefa existente
class TaskUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edittask.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
    # Permite editar a tarefa se for o proprietário ou administrador
        if task.usuario != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("Você não tem permissão para editar esta tarefa.")
        return task



# View para deletar uma tarefa
class TaskDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Task
    template_name = 'tasks/deletetask.html'
    success_url = reverse_lazy('task-list')

    def delete(self, request, *args, **kwargs):
        task = self.get_object()
        if task.usuario != request.user and not request.user.groups.filter(name='Administrador').exists():
            # Redireciona para uma página de erro ou exibe uma mensagem
            raise PermissionDenied("Você não tem permissão para deletar esta tarefa.")
        messages.info(request, 'Tarefa deletada com sucesso.')
        return super().delete(request, *args, **kwargs)


# View do calendário de tarefas
class CalendarView(TemplateView):
    template_name = 'tasks/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.localdate()
        user = self.request.user
        is_authenticated = user.is_authenticated

        # Se for administrador, mostra todas as tarefas
        if user.is_superuser:
            events_today = Task.objects.filter(start_date__lte=today, end_date__gte=today)
        elif not is_authenticated:
            events_today = Task.objects.none()
        else:
            events_today = Task.objects.filter(usuario=user, start_date__lte=today, end_date__gte=today)

        context['events_today'] = events_today
        return context


# Visualiza os eventos como JSON
class TaskEventsView(View):
    def get(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated
        if request.user.is_superuser:  # Se for administrador, carrega todas as tarefas
            tasks = Task.objects.all()
        elif not is_authenticated:
            tasks = Task.objects.none()
        else:
            tasks = Task.objects.filter(usuario=request.user)

        events = []
        for task in tasks:
            if task.start_date and task.start_time and task.end_date and task.end_time:
                start_datetime = datetime.combine(task.start_date, task.start_time)
                end_datetime = datetime.combine(task.end_date, task.end_time)
                events.append({
                    'id': task.id,
                    'title': task.title,
                    'start': start_datetime.isoformat(),
                    'end': end_datetime.isoformat(),
                    'description': task.description,
                })

        return JsonResponse(events, safe=False)


# Contagem de tarefas para o usuário
class EventCountView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'paginas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        today = timezone.localdate()
        start_of_week = today
        end_of_week = today + timedelta(days=(6 - today.weekday()))

        tasks_today = Task.objects.none()
        tasks_week = Task.objects.none()
        total_tasks = Task.objects.none()

        # Se for administrador, mostra todas as tarefas
        if user.is_superuser:
            tasks_today = Task.objects.filter(start_date__lte=today, end_date__gte=today)
            tasks_week = Task.objects.filter(start_date__gte=start_of_week, end_date__lte=end_of_week)
            total_tasks = Task.objects.all()
        else:
            is_discente = user.groups.filter(name='Discente').exists()
            is_docente = user.groups.filter(name='Docente').exists()

            if is_discente or is_docente:
                tasks_today = Task.objects.filter(usuario=user, start_date__lte=today, end_date__gte=today)
                tasks_week = Task.objects.filter(usuario=user, start_date__gte=start_of_week, end_date__lte=end_of_week)
                total_tasks = Task.objects.filter(usuario=user)
            else:
                tasks_today = Task.objects.filter(start_date__lte=today, end_date__gte=today)
                tasks_week = Task.objects.filter(start_date__gte=start_of_week, end_date__lte=end_of_week)
                total_tasks = Task.objects.all()

        context['tasks_today_count'] = tasks_today.count()
        context['tasks_week_count'] = tasks_week.count()
        context['total_tasks_count'] = total_tasks.count()

        return context


# Gráfico anual de contagem de tarefas
class ChartYear(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        year_data = [0] * 12
        user = request.user
        is_discente = user.groups.filter(name='Discente').exists()
        is_docente = user.groups.filter(name='Docente').exists()

        if is_discente:
            tasks = Task.objects.filter(usuario=user)
        elif is_docente:
            tasks = Task.objects.filter(usuario=user)
        else:
            tasks = Task.objects.all()

        for task in tasks:
            if task.start_date:
                month = task.start_date.month - 1
                year_data[month] += 1

        return JsonResponse(year_data, safe=False)