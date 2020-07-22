from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import SignatureForm, ConsultationForm
from .models import JSignatureModel, Client, Consultation, Questionnaire
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages



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


# new addition
def submit_questionnaire(request):
    if request.method == 'POST':
        client = request.POST['name']
        client_temp = request.POST['temp']
        has_mask = request.POST['has_mask']
        covid_diagnosed = request.POST['covid_diagnosed']
        covid_test_type = request.POST['test_type']
        covid_test_date = request.POST['test_date']
        covid_test_results = request.POST['test_results']
        has_symptoms = request.POST['has_symptoms']
        has_been_to_high_risk_zone = request.POST['high_risk_zone'] 
        has_close_contact_with_suspect = request.POST['contact_with_suspect']
        is_clinically_vulnerable = request.POST['is_clinically_vulnerable']
        has_vulnerable_disease = request.POST['has_vulnerable_disease']
        self_quarantine = request.POST['to_self_quarantine']
        has_traveled = request.POST['has_traveled']
        client_questions = request.POST['client_questions']
        report_agreement = request.POST['agreement']

        q = Questionnaire(
            client=client,
            client_temp=client_temp,
            has_mask=has_mask,
            covid_diagnosed=covid_diagnosed,
            covid_test_type=covid_test_type,
            covid_test_date=covid_test_date,
            covid_test_results=covid_test_results,
            has_symptoms=has_symptoms,
            has_been_to_high_risk_zone=has_been_to_high_risk_zone,
            has_close_contact_with_suspect=has_close_contact_with_suspect,
            is_clinically_vulnerable=is_clinically_vulnerable,
            has_vulnerable_disease=has_vulnerable_disease,
            self_quarantine=self_quarantine,
            has_traveled=has_traveled,
            client_questions=client_questions,
            report_agreement=report_agreement
            )
        q.save()
        messages.add_message(request, messages.SUCCESS, 'Questionnaire Completed')
        # redirect to consultation
    return HttpResponseRedirect(reverse('joey:index'))