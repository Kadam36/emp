from django.urls import path
from . import views


urlpatterns = [
    path("",views.home),
    path("Addemp",views.Addemp),
    path("delete/<id>",views.delete),
    path("update/<id>",views.update),


]