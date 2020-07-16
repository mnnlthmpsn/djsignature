from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import SignatureForm, ConsultationForm
from .models import JSignatureModel, Client, Consultation
from django.core.exceptions import ObjectDoesNotExist


# # Create your views here.
# def index(request):
#     signatures = JSignatureModel.objects.all()
#     return render(request, 'index.html', {'signatures': signatures})

# def sign(request):
#     form = SignatureForm(request.POST)
#     if form.is_valid():
#         signature = form.cleaned_data.get('signature')
#         if signature:
#             sign = JSignatureModel(signature=signature)
#             sign.save()            
#             return HttpResponseRedirect(reverse('joey:index'))
#     return render(request, 'sign.html', {'form': SignatureForm()})


# def view(request, signature_id):
#     signature = JSignatureModel.objects.get(pk=signature_id)
#     form = SignatureForm({'signature': signature.signature})
#     return render(request, 'view.html', {'form': form})

def create_consultation(signature):
    # Create Consultation
    consultation = Consultation(client_signature=signature)
    consultation.save()    
    return consultation

def index(request):
    form = ConsultationForm()
    return render(request, 'index.html', {'form': form})

def save_signature(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)

        if form.is_valid():
            # extract fields from form
            client_name = form.cleaned_data.get('client')
            signature = form.cleaned_data.get('signature')

            try:
                client = Client.objects.get(client=client_name)

                # if client exists

                # create signature
                client_signature = JSignatureModel(client=client, signature=signature)
                client_signature.save()

                # pass signature to create consultation fxn
                consultation = create_consultation(client_signature)
                return render(request, 'success.html', {'consultation': consultation})

            # if client does not exist 
            except ObjectDoesNotExist:
                # create client
                client = Client(client=client_name)
                client.save()

                # create signature
                client_signature = JSignatureModel(client=client, signature=signature)
                client_signature.save()

                # pass to consultation fxn
                consultation = create_consultation(client_signature)
                return render(request, 'success.html', {'consultation': consultation})
        return render(request, 'index.html', {'form': ConsultationForm()})
    return HttpResponseRedirect(reverse('joey:index'))