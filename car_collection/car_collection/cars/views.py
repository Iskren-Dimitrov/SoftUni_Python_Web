from django.shortcuts import render, redirect

from car_collection.cars.forms import CarCreateForm, CarEditForm, CarDeleteForm, ProfileCreateForm, ProfileEditForm
from car_collection.cars.models import Car, Profile


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
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

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    form = ProfileEditForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile_edit')

    context = {
        'form': form,
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'POST':
        Car.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index')
    return render(request, 'profile/profile-delete.html')


def car_create(request):
    form = CarCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()
    form = CarEditForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()
    form = CarDeleteForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car/car-delete.html', context)
