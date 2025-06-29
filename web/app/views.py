from django.shortcuts import render

from app.forms import ContactForm
# from app.models import Contact

# Create your views here.
def index(request):
    con = ContactForm()
    return render(request, 'index.html', {'form': con})