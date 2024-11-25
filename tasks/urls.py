from django.urls import path
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskEventsView, CalendarView, EventCountView, ChartYear

urlpatterns = [
    path('dashboard/', EventCountView.as_view(), name='dashboard'),
    path('', CalendarView.as_view(), name='calendar'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('chart-year/', ChartYear.as_view(), name='chart-year'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-view'),
    path('newtask/', TaskCreateView.as_view(), name='new-task'),
    path('list/edit/<int:pk>/', TaskUpdateView.as_view(), name='edit-task'),
    path('list/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
    path('api/tasks/', TaskEventsView.as_view(), name='task_events'),
]