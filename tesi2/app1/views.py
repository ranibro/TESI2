from django.contrib import messages
from django.shortcuts import render
from app1.models import Produto
from app1.forms import ClienteModelForm, ContatoModelForm, ProdutoModelForm, PedidoModelForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato cadastrado com sucesso!')
            form = ContatoModelForm()
        else:
            messages.error(request, 'Contato não cadastrado!')
    else:
        form = ContatoModelForm()
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def cliente(request):
    if request.method == 'POST':
        form = ClienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            form = ClienteModelForm()
        else:
            messages.error(request, 'Cliente não cadastrado!')
    else:
        form = ClienteModelForm()
    context = {
        'form': form
    }
    return render(request, 'cliente.html', context)

def produto(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Produto não cadastrado!')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)

def pedido(request):
    if request.method == 'POST':
        form = PedidoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido Realizado com sucesso!')
            form = PedidoModelForm()
        else:
            messages.error(request, 'Falha na realização do pedido!')
    else:
        form = PedidoModelForm()
    context = {
        'form': form
    }
    return render(request, 'pedido.html', context)

def produto_list(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produto_list.html', context)