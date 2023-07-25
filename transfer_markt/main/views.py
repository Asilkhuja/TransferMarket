from django.shortcuts import render, redirect
from . import forms
from .models import Player_category, Player
from .forms import CreateForm

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()

    # Собираем названия всех продуктов
    player_info = Player.objects.all()

    # Собираем названия всех категорий
    category_info = Player_category.objects.all()

    # Передаем данные на фронт
    context = {
        'form': search_bar,
        'player': player_info,
        'category': category_info
    }

    return render(request, 'main.html', context)


def player_page(request, pk):
    player_info = Player.objects.get(id=pk)

    context = {'player': player_info}
    return render(request, 'about_player.html', context)

def category_page(request, pk):
    category_info = Player_category.objects.get(id=pk)
    player_info = Player.objects.filter(player_category=category_info)

    # Передаем данные на фронт
    context = {'players': player_info}
    return render(request, 'about_player_cat.html', context)


def search_player(request):
    if request.method == 'POST':
        get_player = request.POST.get('search_player')
        try:
            exact_player = Player.objects.get\
                (player_name=get_player)
            return redirect(f'player/{exact_player.id}')
        except:
            return redirect('/')

def create(request):
    error = ''
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'Форма была некорректной'

    form = CreateForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contacts.html')