from django import forms
from .models import Player
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class SearchForm(forms.Form):
    search_player = forms.CharField(max_length=256)

class CreateForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name', 'player_age', 'player_club',
                  'player_position', 'contract_per', 'player_price', 'player_category']
        widgets = {
            'player_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'player_age': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите возраст'
            }),
            'player_club': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите клуб'
            }),
            'player_position': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите позицию игрока'
            }),
            'contract_per': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите срок действия контракта'
            }),
            'player_price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите трансферную стоимость игрока'
            }),
            'player_category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию игрока'
            })
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]