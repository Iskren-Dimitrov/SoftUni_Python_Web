from django.shortcuts import render, redirect

from Fruitipedia.fruit.forms import CreateFruitForm, EditFruitPage, DeleteFruitForm, CreateProfileForm, EditProfileForm
from Fruitipedia.fruit.models import Fruit, Profile


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('index')
    fruits = Fruit.objects.all()
    return render(request, 'common/dashboard.html', {'fruits': fruits})


def profile_create(request):
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('dashboard')

    context = {
        'form': form

    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    fruits = Fruit.objects.all()
    return render(request, 'profile/details-profile.html', {'fruits': fruits})


def profile_edit(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()

        return redirect('profile-details')

    context = {
        'form': form

    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('index')

    return render(request, 'profile/delete-profile.html')


def fruit_create(request):
    form = CreateFruitForm(request.POST or None)
    if form.is_valid():
        form.save()

        return redirect('dashboard')

    context = {
        'form': form

    }

    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    return render(request, 'fruit/details-fruit.html', {'fruit': fruit})


def fruit_edit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = EditFruitPage(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, "fruit/edit-fruit.html", context)


def fruit_delete(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = DeleteFruitForm(instance=fruit)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'fruit/delete-fruit.html', context)
