from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Moihik, Zapisi
from .forms import ClientForm, MoihikForm, ZapisiForm

def index(request):
    return render(request, 'main/index.html')

# Список клиентов и возможность редактирования/добавления
def clients(request):
    clients = Client.objects.all()
    return render(request, 'main/clients.html', {'clients': clients})

# Форма для создания или редактирования клиента
def clients_change(request, id=None):
    if id == 0:
        client = None  # Для создания нового клиента
    else:
        client = get_object_or_404(Client, id=id)  # Редактируем существующего клиента

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')  # Перенаправляем на список клиентов
    else:
        form = ClientForm(instance=client)

    return render(request, 'main/clients_change.html', {'form': form})

# Список мойщиков и возможность редактирования/добавления
def moihiki(request):
    moihiki = Moihik.objects.all()
    return render(request, 'main/moihiki.html', {'moihiki': moihiki})

# Форма для создания или редактирования мойщика
def moihiki_change(request, id=None):
    if id == 0:
        moihiki = None  # Для создания нового мойщика
    else:
        moihiki = get_object_or_404(Moihik, id=id)  # Редактируем существующего мойщика

    if request.method == 'POST':
        form = MoihikForm(request.POST, instance=moihiki)
        if form.is_valid():
            form.save()
            return redirect('moihiki')  # Перенаправляем на список мойщиков
    else:
        form = MoihikForm(instance=moihiki)

    return render(request, 'main/moihiki_change.html', {'form': form})

# Список записей и возможность редактирования/добавления
def zapisi(request):
    zapisi = Zapisi.objects.all()
    return render(request, 'main/zapisi.html', {'zapisi': zapisi})

# Форма для создания или редактирования записи
def zapisi_change(request, id=None):
    if id == 0:
        zapisi = None  # Для создания новой записи
    else:
        zapisi = get_object_or_404(Zapisi, id=id)  # Редактируем существующую запись

    if request.method == 'POST':
        form = ZapisiForm(request.POST, instance=zapisi)
        if form.is_valid():
            form.save()
            return redirect('zapisi')  # Перенаправляем на список записей
    else:
        form = ZapisiForm(instance=zapisi)

    return render(request, 'main/zapisi_change.html', {'form': form})
