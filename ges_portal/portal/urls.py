from django.urls import path
from .views import *


urlpatterns =[
    path("users",users_reg,name="users_reg"),
    path("contingent/",contingent_reg),
    path("proff_reg/",proff_reg),
    path("startup_reg/",startup_reg),
    path("student_reg/",student_reg),
    path("ca_reg/",ca_reg),
    path("dashboard/",dashboard),
    # path("contingent/",contingent_dashboard),
    path("ca_dashboard/",ca_dashboard),
    path("get_user/",get_user),
]


