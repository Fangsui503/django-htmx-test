from django.urls import path
from .views import Home, Notes, DeleteNotes

urlpatterns = [
    path("", view=Home.as_view(), name="index"),
    path("notes/add", view=Notes.as_view(), name="add-note"),
    path("notes/delete/<int:id>", view=DeleteNotes.as_view(), name="delete-note"),
]
