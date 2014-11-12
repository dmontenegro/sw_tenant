# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Inventory

import forms

class CreateInventoryView(CreateView):

    model = Inventory
    template_name = 'edit_inventory.html'
    form_class = forms.InventoryForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse_lazy('index'))

    
