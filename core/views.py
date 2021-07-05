from core.forms import CommentaryForm, SignUpForm
from core.models import Commentary, Photo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.list import ListView


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "register.html", {"form": form})

    form = SignUpForm()

    return render(request, "register.html", {"form": form})


class TimelineView(LoginRequiredMixin, ListView):
    model = Photo
    paginate_by = 10
    queryset = Photo.objects.filter(approved=True)
    template_name = "home.html"


class SubmitPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ["file"]
    success_url = reverse_lazy("home")
    template_name = "submit_photo.html"

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class PhotoApprovementListView(LoginRequiredMixin, ListView):
    model = Photo
    paginate_by = 1
    queryset = Photo.objects.filter(approved=False)
    template_name = "photo-approvement.html"

    def get(self, request, *args, **kwargs):
        if not request.user.admin:
            return redirect("home")
        return super().get(request, *args, **kwargs)


@login_required()
def approve_photo(request, photo_uuid):
    if not request.user.admin:
        return redirect("home")
    photo = Photo.objects.filter(uuid=photo_uuid).update(approved=True)

    return redirect("photo-approvement")


@login_required()
def repprove_photo(request, photo_uuid):
    if not request.user.admin:
        return redirect("home")
    photo = Photo.objects.filter(uuid=photo_uuid).delete()

    return redirect("photo-approvement")


@login_required()
def like_photo(request, photo_uuid):
    photo = Photo.objects.get(uuid=photo_uuid)

    if request.user not in photo.likes.all():
        photo.likes.add(request.user)
        photo.save()
        return redirect("home")

    photo.likes.remove(request.user)
    photo.save()

    return redirect("home")


class PhotoDetail(LoginRequiredMixin, FormMixin, DetailView):
    model = Photo
    template_name = "photo_detail.html"
    form_class = CommentaryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_likes"] = self.object.likes.count()
        context["comments"] = Commentary.objects.filter(photo=self.object)

        return context

class CreateCommentaryView(LoginRequiredMixin, CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.photo_id = int(self.request._post["photo_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "photo-detail", kwargs={"pk": int(self.request._post["photo_id"])}
        )
