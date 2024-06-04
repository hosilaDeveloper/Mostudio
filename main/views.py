from django.shortcuts import render
from .models import Home, Gallery, About, Pricing, Category, Contact

# Create your views here.


def home_view(request):
    home = Home.objects.all().order_by('id')[:3]
    category = Category.objects.all()
    context = {
        'home': home,
        'category': category
    }
    return render(request, 'index.html', context)


def gallery_view(request):
    gallery = Gallery.objects.all()
    context = {
        'galleryy': gallery
    }
    return render(request, 'gallery.html', context)


def about_view(request):
    about = About.objects.all()
    context = {
        'abouts': about
    }
    return render(request, 'about.html', context)


def pricing_view(request):
    pricing = Pricing.objects.all()
    context = {
        'pricings': pricing
    }
    return render(request, 'pricing.html', context)


def contact_view(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contact.html', context)


