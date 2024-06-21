from django.shortcuts import render

def contact(request):
    return render(request,"first_app/contact.html")


def about(request):
    return render(request,"first_app/about.html")
