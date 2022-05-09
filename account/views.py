from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

from account.forms import *
from jobapp.permission import user_is_employee 
from jobapp.models import Resume
import os.path


def get_success_url(request):

    """
    Handle Success Url After LogIN

    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('jobapp:home')



def employee_registration(request):

    """
    Handle Employee Registration

    """
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context={
        
            'form':form
        }

    return render(request,'account/employee-registration.html',context)


def employer_registration(request):

    """
    Handle Employee Registration 

    """

    form = EmployerRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context={
        
            'form':form
        }

    return render(request,'account/employer-registration.html',context)


@login_required(login_url=reverse_lazy('accounts:login'))
@user_is_employee
def employee_edit_profile(request, id=id):

    """
    Handle Employee Profile Update Functionality

    """

    user = get_object_or_404(User, id=id)
    form = EmployeeProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form = form.save()
        messages.success(request, 'Your Profile Was Successfully Updated!')
        return redirect(reverse("account:edit-profile", kwargs={
                                    'id': form.id
                                    }))
    context={
        
            'form':form
        }

    return render(request,'account/employee-edit-profile.html',context)


def resume_page(request,id):

     return render(request,'account/resume-upload.html')




def user_logIn(request):

    """
    Provides users to logIn

    """

    form = UserLoginForm(request.POST or None)
    

    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_url(request))
    context = {
        'form': form,
    }

    return render(request,'account/login.html',context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')


def handle_uploaded_file(f,request):

    ext = f.name.split('.')[-1]
    new_name = f'{request.user.email}.{ext}'
    

    with open('static/resume/'+new_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return new_name


def upload_job_resume(request):

    try:
        if request.method == 'POST':
            new_name = handle_uploaded_file(request.FILES['resume'],request)
            print(new_name)
            found = Resume.objects.filter(user_email=request.user.email).exists()
            if found:
                exist_record = Resume.objects.get(user_email=request.user.email)
                exist_record.resume = new_name 
                exist_record.save()
            else:
                Resume.objects.create(user_email=request.user.email,resume=new_name)
                 

            messages.success(
              request, 'You are successfully posted your resume! .')
            return redirect('/')
            # return render(request,'account/in.html')
          
            

            
           
            
    

    except Exception as e:
        print(e)
        messages.error(
            request, 'error occurred .')
        
        
        return redirect('/')

        
def resume_delete(request):

    try:
        
            # new_name = handle_uploaded_file(request.FILES['resume'],request)
            
            found = Resume.objects.filter(user_email=request.user.email).exists()
            print(found)
            if found:
                exist_record = Resume.objects.get(user_email=request.user.email)
                 
                exist_record.delete()
            
                 

            messages.success(
              request, 'You are successfully deleted your resume! .')
            return redirect('/')
            # return render(request,'account/in.html')
          
            

            
           
            
    

    except Exception as e:
        print(e)
        messages.error(
            request, 'error occurred .')
        
        
        return redirect('/')


        
    