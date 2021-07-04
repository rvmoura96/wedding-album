from core.forms import SignUpForm
from core.models import Photo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "register.html", {"form": form})

    form = SignUpForm()

    return render(request, "register.html", {"form": form})


@login_required()
def home(request):
    return render(request, "home.html")


class SubmitPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ["file"]
    success_url = reverse_lazy("home")
    template_name = "submit_photo.html"
