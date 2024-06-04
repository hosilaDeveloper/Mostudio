from django.urls import path
from .views import home_view, about_view, gallery_view, pricing_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('gallery/', gallery_view, name='gallery'),
    path('pricing', pricing_view, name='pricing'),
    path('contact/', contact_view, name='contact'),
]
