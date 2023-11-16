from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from . import models
from . import forms


class IndexView(generic.View):
    def get(self, request):
        return render(request, 'index.html', self.get_context_data())

    def get_context_data(self):
        context = {
            'new_applications': models.Application.get_new_applications(),
            'accept_applications': models.Application.get_accept_applications(),
            'accept_applications_count': models.Application.get_accept_applications_count(),
            'done_applications': models.Application.get_done_applications(),
            'applications_count': models.Application.get_count(),
        }

        return context

class RegisterView(generic.CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')