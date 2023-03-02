from config import settings
from products.models import Category
from django.core.cache import cache


def cache_categories():
    queryset = Category.objects.all()
    if settings.CACHE_ENABLED:
        key = f'all_category'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)
        return cache_data