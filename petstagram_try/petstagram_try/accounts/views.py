from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram_try.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
from petstagram_try.accounts.models import PetstagramUser
from django.contrib.auth import views as auth_views, login


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')

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


class UserDetailsView(views.DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        profile_image = static('images/person.png')

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)

        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())

        context.update({
            'total_likes_count': total_likes_count,
            'profile_image': profile_image,
        })

        return context


class UserEditView(views.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
