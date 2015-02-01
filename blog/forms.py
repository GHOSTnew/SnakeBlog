from django import forms


class commentForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label="Titre:")
    author = forms.CharField(max_length=60, required=True, label="Pseudo:")
    authorEmail = forms.EmailField(label="Email", required=True)
    content = forms.CharField(widget=forms.Textarea, required=True, label="Commentaire")
