
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Temple

class Add_temple(CreateView):
    model = Temple
    fields = "__all__"


class List_temple(ListView):
    model = Temple

class Detail_temple(DetailView):
    model = Temple


class Update_temple(UpdateView):
    model = Temple

    fields = "__all__"
    success_url = "/"

class Delete_temple(DeleteView):
    model = Temple
    success_url = "/"
    template_name = "temple/Temple_confirm.html"
