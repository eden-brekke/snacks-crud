from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Snack

# Create your views here.
class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack

class SnackCreateView(CreateView):
  template_name = 'snack_create.html'
  model = Snack
  fields = ['title', 'purchaser', 'description']

class SnackUpdateView(UpdateView):
  template_name = 'snack_update.html'
  model = Snack
  fields = ['title', 'purchaser', 'description']


class SnackDeteletView(DeleteView):
  pass

