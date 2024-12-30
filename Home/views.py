from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages


# Create your views here.

# def Home(request):
#     return render(request, "index.html")

def index(request):
     
    return render(request, "index.html")

def about(request):
    # return HttpResponse("this is aboutpage")
    return render(request, "about.html")

def services(request):
    # return HttpResponse("this is services page")
    return render (request, "services.html")

def contact(request):
    # return HttpResponse("this is contacts page")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        institute = request.POST.get("institute")
        problem = request.POST.get("problem")
        agreed = request.POST.get("agreed")

        contact = Contact(name=name, email=email, phone=phone, institute=institute, problem=problem, agreed=agreed, date=datetime.today())

        contact.save()
        messages.success(request, "You form submitted successfully!")

    return render (request, "contact.html")

 
