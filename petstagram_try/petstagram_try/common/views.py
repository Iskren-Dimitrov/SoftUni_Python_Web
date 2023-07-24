from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram_try.common.forms import CommentForm, SearchForm
from petstagram_try.common.models import Like
from petstagram_try.photos.models import Photo


def index(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    if request.user.is_authenticated:

        for photo in all_photos:
            if photo:
                photo.liked_by_user = photo.like_set.filter(user=request.user).exists()

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,

    }
    return render(request, template_name='common/home-page.html', context=context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()

    if liked_object:
        liked_object.delete()

    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('details-photo', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            if request.user.is_authenticated:
                comment.user = request.user  # Assign the authenticated user to the comment
            else:
                comment.user = None  # If anonymous, set user to None
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
