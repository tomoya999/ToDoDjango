from django.urls import path
from . import views
app_name = 'crudapp'

urlpatterns = [
# list
# path('', views.IndexView.as_view(), name='index'),
path('', views.index, name='index'),

# create
path('create/', views.CreateView.as_view(), name='create'),
# detail
# path('todo/<int:pk>/', views.DetailsView.as_view(), name='detail'),
# update
path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
# delete
path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]
