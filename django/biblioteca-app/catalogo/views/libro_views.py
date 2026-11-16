from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from catalogo.forms.libro_form import Libroform
from catalogo.models import Categoria, Libro


@login_required
@permission_required('catalogo.view_libro', raise_exception=True)
def libro_list(request):
    pista = request.GET.get('pista', '').strip()
    categoria_id = request.GET.get('categoria_id', '').strip()
    libros = Libro.objects.prefetch_related('autores').select_related('categoria')
    if pista:
        libros = libros.filter(
            Q(titulo__icontains=pista) | Q(autores__nombre__icontains=pista) |
            Q(autores__apellido__icontains=pista) | Q(categoria__nombre__icontains=pista)
        ).distinct()
    if categoria_id:
        libros = libros.filter(categoria_id=categoria_id)
    return render(request, 'catalogo/libros/libro_list.html', {
        'libros': libros, 'categorias': Categoria.objects.all(),
        'pista': pista, 'categoria_id': categoria_id,
    })


@login_required
@permission_required('catalogo.add_libro', raise_exception=True)
def create_libro(request):
    form = Libroform(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('libro_list')
    return render(request, 'catalogo/libros/libro_form.html', {'form': form})


@login_required
@permission_required('catalogo.change_libro', raise_exception=True)
def update_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = Libroform(request.POST or None, instance=libro)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('libro_list')
    return render(request, 'catalogo/libros/libro_form.html', {'form': form})


@login_required
@permission_required('catalogo.delete_libro', raise_exception=True)
def delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro_list')
    return render(request, 'catalogo/libros/libro_confirm_delete.html', {'libro': libro})
