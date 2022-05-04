from django.forms import ModelForm, widgets
from core.models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = ["id"]
        widgets = {
<<<<<<< HEAD
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'user_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'})
=======
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "user_name": widgets.TextInput(attrs={"class": "form-control"}),
            "email": widgets.TextInput(attrs={"class": "form-control"}),
            "bio": widgets.TextInput(attrs={"class": "form-control"}),
>>>>>>> origin/main
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
<<<<<<< HEAD
        exclude = ['id', 'user_name', 'email', 'password']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'bio': widgets.TextInput(attrs={'class': 'form-control'})
        }

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'email', 'name', 'bio']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'})
        }
=======
        exclude = ["id"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "bio": widgets.TextInput(attrs={"class": "form-control"}),
        }
>>>>>>> origin/main