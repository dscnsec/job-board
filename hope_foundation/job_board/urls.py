from django.urls import path
from . import views


urlpatterns = [
		path('home/', views.home, name='job_board-home'),
		path('about/', views.about, name='job_board-about'),
		path('register/', views.register, name='job_board-register'),
]


