from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Snack

# Create your views here.
class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack

class SnackDetailView(DetailView):
  pass

class SnackCreateView(CreateView):
  pass

class SnackUpdateView(UpdateView):
  pass

class SnackDeteletView(DeleteView):
  pass

