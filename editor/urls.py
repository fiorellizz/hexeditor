from django.urls import path
from . import views

app_name = "editor"

urlpatterns = [
    path("", views.upload_arquivo, name="upload"), #está sendo usada
    path("upload/", views.upload_arquivo, name="upload"), #está sendo usada
    path("visualizar/<int:pk>/", views.visualizar_arquivo, name="visualizar"), #está sendo usada
    path("editar/<int:pk>/", views.editar_arquivo, name="editar"),
    path("editar/<int:pk>/<int:offset>/", views.editar_byte, name="editar_byte"),
    path("editar_endereco/<int:pk>/<int:offset>/", views.editar_endereco, name="editar_endereco"),
    path("download/<int:pk>/", views.download_arquivo, name="download"),
]
