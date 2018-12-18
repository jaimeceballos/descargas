from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect
# Create your views here.

def home(request):
    form = FileUploadForm()
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    archivos = FileUpload.objects.all()
    return render(request,'home.html',{'form':form,'archivos':archivos})