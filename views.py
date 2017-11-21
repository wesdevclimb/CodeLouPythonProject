from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from . import models


class BookList(ListView):
    model = models.Book


class BookCreate(CreateView):
    model = models.Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = models.Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = models.Book
    success_url = reverse_lazy('book_list')


class FoodDescriptionList(ListView):
    model = models.FoodDescription


class FoodDescriptionCreate(CreateView):
    model = models.FoodDescription
    fields = [ 'com_name', 'protein_factor', 'fat_factor', 'cho_factor']
    success_url = reverse_lazy('fooddescription_list')


class FoodDescriptionUpdate(UpdateView):
    model = models.FoodDescription
    fields = [ 'com_name', 'protein_factor', 'fat_factor', 'cho_factor']
    success_url = reverse_lazy('fooddescription_list')


class FoodDescriptionDelete(DeleteView):
    model = models.FoodDescription
    success_url = reverse_lazy('fooddescription_list')