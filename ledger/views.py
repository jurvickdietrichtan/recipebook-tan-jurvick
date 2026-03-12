from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy



from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from django import forms

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

@login_required

def login(request):
    return render(request, "login.html")

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}
    return render(request, "ledger/recipe_detail.html", context)

def index(request):
    return HttpResponse('Sorry bro.')

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html", context)

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["name"]
    template_name = "ledger/recipe_add.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ["image", "description"]
    template_name = "ledger/add_image.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs["pk"]
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_pk'] = self.kwargs['pk']
        return context







