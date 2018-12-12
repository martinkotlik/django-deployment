from django.urls import path, include
from basic_app import views

# TEMPLATES URLS!
app_name = 'basic_app_urls'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
