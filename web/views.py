from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Flan, ContactForm, Review
from .forms import ContactFormForm, ContactFormModelForm, ReviewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def index(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes_privados': flanes_privados})

def logout_view(request):
    logout(request)

    return redirect('/')

def contact(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def flan_detail(request, pk):
    flan = get_object_or_404(Flan, pk=pk)
    reviews = flan.reviews.all()
    return render(request, 'flan_detail.html', {'flan': flan, 'reviews': reviews})

@login_required
def add_review(request, pk):
    flan = get_object_or_404(Flan, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.flan = flan
            review.user = request.user
            review.save()
            return redirect('flan_detail', pk=flan.pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def flan_list(request):
    flanes = Flan.objects.all()
    return render(request, 'flan_list.html', {'flanes': flanes})

