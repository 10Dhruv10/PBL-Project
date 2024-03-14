from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_displa', views.add_displa, name='add-displa'),
    path('display', views.all_display, name='list-display'),
    path('search/', views.search_results, name='search_results'),
    path('update_displa/<displa_id>', views.update_displa, name="update-displa"),
    path('delete_displa/<displa_id>', views.delete_displa, name='delete-displa'),
]
