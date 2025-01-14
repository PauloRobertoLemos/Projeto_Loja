from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProdutoForm
from django.shortcuts import redirect
from .models import Produto
from django.contrib import messages



# Create views
def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('list')
        else:
            messages.error(request, 'Erro ao criar o produto. Verifique os dados e tente novamente.')
    else:
        form = ProdutoForm()
    return render(request, 'create.html', {'form':form})


# list view
def produto_list(request):
    produto = Produto.objects.all()
    return render(request, 'list.html', {'produtos':produto})


# update view
def update_produto(request, pk):
    produto = Produto.objects.get(id=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('list')
        else:
            messages.error(request, 'Erro ao atualizar o produto. Verifique os dados e tente novamente.')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'update.html', {'form':form})

# delete view

def delete_produto(request, pk):
    produto = Produto.objects.get(id=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
    return redirect('list')