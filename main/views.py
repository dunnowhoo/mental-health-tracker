from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm': '23062754246',
        'name': 'Fauzan Putra Sanjaya',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
