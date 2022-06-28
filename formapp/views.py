from distutils.command.upload import upload
from distutils.log import error
from django.shortcuts import render
from formapp.forms import StudentForm
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from formapp.functions import handle_uploaded_file  
from formapp.forms import FormUpload 
from .models import UploadForm
  

def form_request(request):
    # Check the form is submitted or not
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            #return render(request, "upload.html")
            return HttpResponse("Login Successful")

        else:
            return HttpResponseNotFound('Error')
    else:
        student = StudentForm()
        return render(request, "form.html", {'form': student})

# Create your views here.

def index(request):  
    if request.method == 'POST':  
        upload = FormUpload(request.POST, request.FILES)  
        if upload.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            model_instance = upload.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        upload = FormUpload()  
        return render(request,"upload.html",{'form':upload})  


def uploadinfo(request):
    file = UploadForm.objects.all()
    print("Myoutput",file)
    return render(request,'show.html',{'show': file})