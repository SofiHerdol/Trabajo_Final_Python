from django.shortcuts import render
from animal_app.forms import AnimalForm, ShelterForm, PersonForm, NewContactNumber
from animal_app.models import Animals, AnimalShelter, Person, ContactNumber
from django.views.generic import UpdateView, DeleteView
# Create your views here.


def put_up_for_adoption(request):
    if request.method == "GET":
        context = {
            "form": AnimalForm()
        }
        return render(request, "putup-adoption.html", context=context)

    elif request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            Animals.objects.create(
                name = form.cleaned_data["name"],
                age = form.cleaned_data["age"],
                breed = form.cleaned_data["breed"],
                exotic = form.cleaned_data["exotic"],
                baby = form.cleaned_data["baby"],
            )
            context = {
                "message": "¡Aviso creado!"
            }
            return render(request, "putup-adoption.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": AnimalForm()
            }
            return render(request, "putup-adoption.html", context=context)

def animal_list(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_animals = Animals.objects.filter(name__icontains=search)
    else:
        all_animals = Animals.objects.all()
    context = {
        "adoptions":all_animals,
    }
    return render(request, "animal-list.html", context = context)

def create_shelter(request):
    if request.method == "GET":
        context = {
            "form": ShelterForm()
        }
        return render(request, "create-shelter.html", context=context)
    elif request.method == "POST":
        form = ShelterForm(request.POST)
        if form.is_valid():
            AnimalShelter.objects.create(
                name = form.cleaned_data["name"],
                street = form.cleaned_data["street"],
                number= form.cleaned_data["number"],
                postal_code = form.cleaned_data["postal_code"],
                province = form.cleaned_data["province"],
                shelter_type = form.cleaned_data["shelter_type"],
            )
            context = {
                "message": "¡Refugio creado!"
            }
            return render(request, "create-shelter.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": ShelterForm()
            }
            return render(request, "create-shelter.html", context=context)

def shelter_list(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_shelters = AnimalShelter.objects.filter(name_icontains=search)
    else:
        all_shelters = AnimalShelter.objects.all()
    context = {
        "shelters":all_shelters,
    }
    return render(request, "shelter-list.html", context = context)

def create_profile(request):
    if request.method == "GET":
        context = {
            "form": PersonForm()
        }
        return render(request, "create-profile.html", context=context)
    elif request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(
                name = form.cleaned_data["name"],
                age = form.cleaned_data["age"],
                dni= form.cleaned_data["dni"],
                house_type = form.cleaned_data["house_type"],
            )
            context = {
                "message": "¡Perfil creado!"
            }
            return render(request, "create-profile.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": PersonForm()
            }
            return render(request, "create-profile.html", context=context)

def profile_list(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_profiles = Person.objects.filter(name_icontains=search)
    else:
        all_profiles= Person.objects.all()
    context = {
        "profiles":all_profiles,
    }
    return render(request, "profile-list.html", context = context)

def contact_number(request):
    if request.method == "GET":
        context = {
            "form": NewContactNumber()
        }
        return render(request, "adopted.html", context=context)
    elif request.method == "POST":
        form = NewContactNumber(request.POST)
        if form.is_valid():
            ContactNumber.objects.create(
                contact_number = form.cleaned_data["contact_number"],
            )
            context = {
                "message": "¡En breves nos estaremos comunicando con vos para darte más información!"
            }
            return render(request, "adopted.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": NewContactNumber()
            }
            return render(request, "adopted.html", context=context)

class AnimalDelete(DeleteView):
    model = Animals
    template_name = "delete-animal.html"
    success_url = "/animal-list/"

class AnimalUpdate(UpdateView):
    model = Animals
    fields = ["name", "age", "breed", "gender", "adopted", "exotic", "baby"]
    template_name = "update-animal.html"
    success_url = "/animal-list/"




















