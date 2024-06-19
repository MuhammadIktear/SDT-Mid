from django.urls import path
from.import views
urlpatterns=[
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_pass/',views.change_pass,name='change_pass'),
]