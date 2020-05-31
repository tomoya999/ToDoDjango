from django.urls import path
from . import views
app_name = 'crudapp'

urlpatterns = [
# path('', views.IndexView.as_view(), name='index'),
path('', views.index, name='index'),
path('create/', views.CreateView.as_view(), name='create'),
# path('todo/<int:pk>/', views.DetailsView.as_view(), name='detail'),
path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),

# api
path('api/list', views.todo_list, name='todo_list_api'),
path('api/create', views.todo_create, name='todo_create_api'),
path('api/update/<int:pk>', views.todo_update, name='todo_update_api'),
path('api/delete/', views.todo_delete, name='todo_delete_api')

]
