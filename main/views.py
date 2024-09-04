from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306275885',
        'name': 'Muhammad Radhiya Arshq',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)