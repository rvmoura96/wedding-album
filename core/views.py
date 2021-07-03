from core.forms import SignUpForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "register.html", {"form": form})

    form = SignUpForm()
    return render(request, "register.html", {"form": form})


def login(request):
    return render(request, "login.html")
