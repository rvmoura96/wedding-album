from django.shortcuts import render

from core.forms import SignUpForm

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            return render(request, 'batata.html')
    form = SignUpForm()
    return render(request, 'register.html', {"form": form})
