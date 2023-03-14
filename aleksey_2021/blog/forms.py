from django import forms
class CommentForm(forms.Form):
    authot = forms.CharField(
        max_length= 60,
        widget= forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":" Ваше имя"
        })
    )
    body = forms.CharField(
        widget= forms.Textarea(attrs={
            "class":"form-control",
            "placeholder":" Ваш комментарий"
        })
    )