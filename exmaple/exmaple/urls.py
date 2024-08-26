from django.urls import re_path, include, path


urlpatterns = [
   path("notes/", include("websocket.urls"))
]
