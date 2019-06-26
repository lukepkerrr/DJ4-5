from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    form = ReviewForm

    if 'reviewed_products' not in request.session:
        request.session['reviewed_products'] = []

    if product.id in request.session['reviewed_products']:
        is_review_exist = True
    else:
        is_review_exist = False
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                Review.objects.create(text=form.cleaned_data['text'], product=product)
                old_session = request.session['reviewed_products']
                old_session.append(product.id)
                request.session['reviewed_products'] = old_session

    context = {
        'form': form,
        'product': product,
        'reviews': Review.objects.filter(product=product),
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)
