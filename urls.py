# controls global URl routing paths from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.global_dashboard, name='global_dashboard'),
    path('placement/<int:resident_id>/', views.placement_match_view, name='placement_match'),
]
