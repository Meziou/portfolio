from django.shortcuts import render
from .models  import Home, About, Profile, Category, Skills, Portfolio
# Create your views here.

def index(request):
    #Home
    home = Home.objects.latest('updated')

     # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    #Portfolio
    portfolios = Portfolio.objects.all()

    #Skills
    categories = Category.objects.all()
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }
    return render(request, 'index.html', context)