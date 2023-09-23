from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "note"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control text-primary text-bg-secondary"}
            ),
            "note": forms.Textarea(
                attrs={
                    "class": "form-control text-primary text-bg-secondary resize-none",
                    "style": "resize:none;",
                }
            ),
        }
