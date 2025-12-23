from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Product, Category
from .forms import ProductForm, RegisterForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('product_list')

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Registration successful')
        return redirect('product_list')

    return render(request, 'auth/register.html', {'form': form})


@login_required
def product_list(request):
    products = Product.objects.select_related('category').order_by('category__name', '-created_at')

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    if query:
        products = products.filter(name__icontains=query)

    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    # Pagination: 10 products per page
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'products': page_obj,
        'categories': categories,
        'total_products': paginator.count
    })


@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        product = form.save(commit=False)
        product.created_by = request.user
        product.save()
        messages.success(request, 'Product added successfully')
        return redirect('product_list')

    return render(request, 'products/product_form.html', {'form': form})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if form.is_valid():
        form.save()
        messages.success(request, 'Product updated successfully')
        return redirect('product_list')

    return render(request, 'products/product_form.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, created_by=request.user)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('product_list')

    return render(request, 'products/product_confirm_delete.html', {'product': product})
