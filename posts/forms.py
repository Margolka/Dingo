from django import forms
from .models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author"]
        widgets = {
            "author": forms.Select(
                choices=((a.id, a.nick) for a in Author.objects.all())
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        author = cleaned_data.get("author")

        if not (title or content or author):
            raise forms.ValidationError("Błąd! Nie podano wartości!!")
        return cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get("nick")
        email = cleaned_data.get("email")

        if not (nick or email):
            raise forms.ValidationError("Błąd! Nie podano wartości!!")
        return cleaned_data
