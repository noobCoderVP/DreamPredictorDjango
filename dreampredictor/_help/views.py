from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def Contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html', {'form': ContactForm()})
    else:
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, 'Query sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Fill the form correctly!')
            return redirect('home')
