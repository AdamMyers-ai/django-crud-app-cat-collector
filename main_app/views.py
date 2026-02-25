from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
from .forms import FeedingForm
from django.shortcuts import render, redirect


class CatCreate(CreateView):
    model = Cat
    fields = "__all__"
    template_name = "main_app/cat_form.html"


class CatUpdate(UpdateView):
    model = Cat
    fields = ["breed", "description", "age"]
    template_name = "main_app/cat_form.html"


class CatDelete(DeleteView):
    model = Cat
    context_object_name = "cat"
    success_url = "/cats/"
    template_name = "main_app/cat_confirm_delete.html"


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cat_index(request):
    cats = Cat.objects.all()
    return render(request, "cats/index.html", {"cats": cats})


def cat_detail(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    feeding_form = FeedingForm()
    return render(
        request, "cats/detail.html", {"cat": cat, "feeding_form": feeding_form}
    )


def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect("cat-detail", cat_id=cat_id)
