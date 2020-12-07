from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from django.contrib.auth import get_user_model
from .forms import Form, UserRegisterForm


@login_required
def index(request):
    current_user = request.user
    ctx = {
        'friends': current_user.friends.all(),
        'not_friends': get_user_model().objects.exclude(friends=current_user).exclude(id=current_user.id),
        'hide_home': True
    }
    return render(request, 'app/index.html', ctx)


@login_required
def remove_friend(request, pk):
    friend_to_remove = get_user_model().objects.get(pk=pk)
    request.user.friends.remove(friend_to_remove)
    return redirect('index')


@login_required
def add_friend(request, pk):
    friend_to_add = get_user_model().objects.get(pk=pk)
    request.user.friends.add(friend_to_add)
    return redirect('index')


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'app/user_detail.html'
    context_object_name = "user"


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
