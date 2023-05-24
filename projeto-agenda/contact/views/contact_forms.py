from django.shortcuts import render

from contact.forms import ContactForm
from contact.models import Contact

def create(request):

    if request.method == 'POST':
        context = {
            'form': ContactForm(data=request.POST)
        }
        
        return render(
            request,
            'contact/create.html',
            context
        )


    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )

