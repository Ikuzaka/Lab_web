from django.shortcuts import render
from . import database
from .models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Product
import json

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog.html', context = {
        'products': products,
    })


@require_POST
def toggle_favorite(request):
    data = json.loads(request.body)
    print(data)

    # 2. Access your data by key
    product_id = data.get('product_id')
    product = get_object_or_404(Product, id=product_id)

    # Проверяем, авторизован ли пользователь
    if not request.user.is_authenticated:
        return JsonResponse({
            'success': False,
            'redirect': '/login/'  # Укажите ваш URL для входа
        }, status=401)

    # Переключаем лайк
    if request.user in product.favorite_by.all():
        product.favorite_by.remove(request.user)
        is_favorited = False
    else:
        product.favorite_by.add(request.user)
        is_favorited = True

    return JsonResponse({
        'success': True,
        'is_favorited': is_favorited,
        'favorites_count': product.favorites
    })
def get_likes(request):
    products = Product.objects.all()
    # Создаем словарь {id: count}
    result = {p.id: p.favorite_by.count() for p in products}
    return JsonResponse(result)


