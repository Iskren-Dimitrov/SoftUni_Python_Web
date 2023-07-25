from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic as views
from petstagram_try.common.forms import CommentForm
from petstagram_try.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram_try.photos.models import Photo


class PhotoAddView(LoginRequiredMixin, views.CreateView):
    template_name = 'photos/photo-add-page.html'
    form_class = PhotoCreateForm

    def get_success_url(self):
        return reverse('details-photo', kwargs={
            'pk': self.object.pk
        })

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object

        return context


# @login_required
# def add_photo(request):
#     form = PhotoCreateForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         photo = form.save(commit=False)
#         photo.user = request.user
#         photo.save()
#         form.save_m2m()
#         return redirect('index')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, template_name='photos/photo-add-page.html', context=context)


# def details_photo(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     likes = photo.like_set.all()
#     comments = photo.comment_set.all()
#     comment_form = CommentForm()
#     photo_is_liked_by_user = likes.filter(user=request.user)
#
#     context = {
#         'photo': photo,
#         'likes': likes,
#         'comment_form': comment_form,
#         'comments': comments,
#         'photo_is_liked_by_user': photo_is_liked_by_user,
#
#     }
#
#     return render(request, template_name='photos/photo-details-page.html', context=context)

@login_required
def details_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        "photo": photo,
        "likes": photo.like_set.count(),
        "comments": photo.comment_set.all(),
        "comment_form": comment_form,
        'is_owner': request.user == photo.user,

    }

    return render(
        request,
        'photos/photo-details-page.html',
        context=context
    )


def edit_photo(request, pk):
    photo = Photo.objects.filter(pk=pk) \
        .get()
    form = PhotoEditForm(request.POST or None, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('details-photo', pk)

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')
