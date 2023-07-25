from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from petstagram_try.common.forms import CommentForm
from petstagram_try.pets.forms import PetForm, PetDeleteForm
from petstagram_try.pets.models import Pet


@login_required
def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile-details', request.user.pk)

    context = {
        'form': form
    }

    return render(request, template_name='pets/pet-add-page.html', context=context)


@login_required
def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'is_owner': request.user == pet.user,

    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)

    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details-pet', username, pet_slug)

    context = {
        'pet': pet,
        'form': form

    }
    return render(request, template_name='pets/pet-edit-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', request.user.pk)
    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form
    }
    return render(request, template_name='pets/pet-delete-page.html', context=context)
