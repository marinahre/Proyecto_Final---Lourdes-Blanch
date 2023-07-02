from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('profile/', views.mostrar_perfil, name="profile"),
    path('edit_profile/', views.editar_perfil, name="edit profile"),
]
