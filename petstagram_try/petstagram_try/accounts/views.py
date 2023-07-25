import pet as pet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram_try.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
from petstagram_try.accounts.models import PetstagramUser
from django.contrib.auth import views as auth_views, login, get_user_model

from petstagram_try.pets.models import Pet

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'
    profile_image = static('images/person.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['profile_image'] = self.get_profile_image()
        context['pets'] = self.request.user.pet_set.all()

        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())

        context.update({
            'total_likes_count': total_likes_count,
        })

        return context


class UserEditView(views.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
