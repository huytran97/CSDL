from django.urls import path
from paperapp import views

app_name = "paper_app"

urlpatterns = [
    # path('login/', views.form_login, name='login'),
    path('papers/', views.papers, name='papers'),
    path('add_papers/',views.add_papers, name='add_papers')
]