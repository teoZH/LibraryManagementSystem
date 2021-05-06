from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class UserCreationFormReformed(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", 'email')
        field_classes = {'username': UsernameField}
