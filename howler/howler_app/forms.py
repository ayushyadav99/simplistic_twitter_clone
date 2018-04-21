from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Howler
from django.core.files.images import get_image_dimensions
from howler_app.models import UserProfile


class AddFollowerForm(forms.ModelForm):
    name = forms.CharField(max_length=100,label="Username")
    class Meta:
        exclude=('follows','picture','user')
        model = UserProfile
class HowlerForm(forms.ModelForm):

    class Meta:
        model = Howler
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields = {
        "username",
        "first_name",
        "last_name",
        "email",
        "password1",
        "password2",
        }

    def save(self,commit=True):
        user=super(SignUpForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']

        if commit:
            user.save()

        return user
