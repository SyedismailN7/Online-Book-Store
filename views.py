from django.shortcuts import render
from .models import Subscriber

def subscribe(request):
    message = None

    if request.method == "POST":
        email = request.POST.get("email")

        if not Subscriber.objects.filter(email=email).exists():
            Subscriber.objects.create(email=email)
            message = "Thank you! You are now subscribed."
        else:
            message = "You have already subscribed."

    return render(request, "newsletter.html", {"message": message})
