from django.shortcuts import render, redirect

from plants_try.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm
from plants_try.web.models import Plant, Profile


def index(request):
    return render(request, 'common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants,
    }

    return render(request, 'common/catalogue.html', context)


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('index')

    return render(request, 'profile/delete-profile.html')


def plant_create(request):
    form = PlantCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'plant/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'plant': plant,
    }

    return render(request, 'plant/plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    form = PlantEditForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'plant': plant,
        'form': form,
    }

    return render(request, 'plant/edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    form = PlantDeleteForm(request.POST or None, instance=plant)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'plant': plant,
        'form': form,
    }

    return render(request, 'plant/delete-plant.html', context)
