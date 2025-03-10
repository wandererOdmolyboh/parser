from django.urls import path
from .views import InstagramScraperView

urlpatterns = [
    path('scrape/', InstagramScraperView.as_view(), name='scrape')
]
