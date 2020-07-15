from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from jsignature.utils import draw_signature
from .forms import SignatureForm
from .models import JSignatureModel


# Create your views here.
def index(request):
    signatures = JSignatureModel.objects.all()
    return render(request, 'index.html', {'signatures': signatures})

def sign(request):
    form = SignatureForm(request.POST)
    if form.is_valid():
        signature = form.cleaned_data.get('signature')
        if signature:
            sign = JSignatureModel(signature=signature)
            sign.save()            
            return HttpResponseRedirect(reverse('joey:index'))
    return render(request, 'sign.html', {'form': SignatureForm()})


def view(request, signature_id):
    signature = JSignatureModel.objects.get(pk=signature_id)
    form = SignatureForm({'signature': signature.signature})
    return render(request, 'view.html', {'form': form})

