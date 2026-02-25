from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from .models import Cats


class CatCreate(CreateView):
    model = Cats
    fields = "__all__"
    template_name = "main_app/cat_form.html"
    success_url = "/cats/"


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cat_index(request):
    cats = Cats.objects.all()
    return render(request, "cats/index.html", {"cats": cats})


def cat_detail(request, cat_id):
    cat = get_object_or_404(Cats, id=cat_id)
    return render(request, "cats/detail.html", {"cat": cat})
