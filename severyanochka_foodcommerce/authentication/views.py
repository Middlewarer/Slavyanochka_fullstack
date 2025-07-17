from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from . import forms

class RegistrationPageView(FormView):
    template_name = 'authentication/register.html'
    form_class = forms.RegistrationForm
    success_url = '/authentication/index/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

def index(request):
    return HttpResponse("<h1>Renderview</h1>")
