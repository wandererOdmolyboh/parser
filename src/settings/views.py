from django.shortcuts import render


def white_page_view(request, subpath=None):
    return render(request, 'white_page.html')
