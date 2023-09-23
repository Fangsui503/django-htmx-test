from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .forms import NoteForm
from .models import Note


# Create your views here.
class Home(View):
    def get(self, request):
        return render(
            request, "index.html", {"form": NoteForm(), "notes": Note.objects.all()}
        )


class Notes(View):
    def post(self, request):
        form = NoteForm(request.POST or None)
        if form.is_valid():
            note = form.save()
            return render(request, "partials/note.html", {"note": note})

    def get(self, request):
        return render(request, "partials/form.html")


class DeleteNotes(View):
    def delete(self, id: id):
        note = get_object_or_404(Note, id=id)
        note.delete()
        return HttpResponse(status=200)
