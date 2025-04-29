# results/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_pdf, name='show_pdf'),
    path('res/', views.admission_result_view , name = 'admission_result_view'),
    path('not/', views.notice_board_view, name='notice_board'),
    path('add/', views.add_notice_view, name='add_notice'),
    path('routines/', views.routine_view, name='routine_view'),
    path('waiver/', views.waiver, name='waiver'),
]
