from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterFormView(FormView):
    form_class = UserCreationForm


    success_url = "accounts/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/registration.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class HomePageView(TemplateView):

    template_name = "index\home.html"

#class LoginPageView(TemplateView):
    #template_name = "registration\login.html"
#from django.http import HttpResponse
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class UserProfilePage(DetailView):
    model = User
    template_name = "user/userPage.html"
    slug_field = "username"