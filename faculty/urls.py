from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('update-faculty/<int:pk>', views.update_faculty, name='update-faculty'),
    path('update/', views.update_view, name='update'),
    path('faculty/<int:faculty_id>/research/', views.faculty_research, name='faculty_research'),
]
