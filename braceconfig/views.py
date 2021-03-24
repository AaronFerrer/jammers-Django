from django.shortcuts import render

# Create your views here.
from braceconfig.models import Deformity, Patient, Surgeon, RxInstance
'''
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_patients = Patient.objects.all().count() 

    # The 'all()' is implied by default.
    num_surgeons = Surgeon.objects.count()

    context = {
        'num_patients': num_patients,
        'num_surgeons': num_surgeons,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
'''
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from braceconfig.forms import BraceOne, BraceTwo, BraceThree, BraceFour, BraceFive, BraceSix
from django.views import generic

class PtListView(generic.ListView):
    model = Patient


def index(request):
    """View function for home page of site."""

   

    context = {
         
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    
class PtDetailView(generic.DetailView):
    model = Patient

#from django.forms import formset_factory
#from braceconfig.forms import rxForm



def calculate_surgeon(request,pk):
    patient_instance = get_object_or_404(RxInstance, pk = pk)

    # Post: Process the form data
    if request.method == 'POST':

        # Create a form instance
        form1 = BraceOne(request.POST)
        form2 = BraceTwo(request.POST)
        form3 = BraceThree(request.POST)
        form4 = BraceFour(request.POST)
        form5 = BraceFive(request.POST)
        form6 = BraceSix(request.POST)

        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid():
            patient_instance.brace_one = form1.cleaned_data['brace_one']
            patient_instance.brace_two = form2.cleaned_data['brace_two']
            patient_instance.brace_three = form3.cleaned_data['brace_three']
            patient_instance.brace_four = form4.cleaned_data['brace_four']
            patient_instance.brace_five = form5.cleaned_data['brace_five']
            patient_instance.brace_six = form6.cleaned_data['brace_six']

            patient_instance.save()

            return HttpResponseRedirect(request.path_info)

    else:
        form1 = BraceOne(initial={'brace_one': 200})
        form2 = BraceTwo(initial={'brace_two': 200})
        form3 = BraceThree(initial={'brace_three': 200})
        form4 = BraceFour(initial={'brace_four': 200})
        form5 = BraceFive(initial={'brace_five': 200})
        form6 = BraceSix(initial={'brace_six': 200})
        pass

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
        'form6': form6,
        'patient_instance': patient_instance
    }

    return render(request, 'braceconfig/calculate_surgeon.html',context)



