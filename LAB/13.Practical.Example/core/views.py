from django.shortcuts import render,redirect
from core.forms import RegisterForm,PasswordResetForm
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from core.utils import send_activation_email,send_reset_password_email
from core.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from core.decorater import login_and_role_required
from django.contrib.auth.forms import PasswordChangeForm ,SetPasswordForm
# Create your views here.

def index(req):
    if req.user.is_authenticated:
        if req.user.is_seller:
            return redirect('seller_dashboard')
        elif req.user.is_customer:
            return redirect('customer_dashboard')
        return redirect('/')
    if req.method == 'POST':
        email=req.POST.get('email')
        password=req.POST.get('password')
        print(email,password)
        if not email or not password:
            messages.error(req,'Both fields are required.')
            return redirect('Home')
        try:
            user=User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(req,'Invalid email or password.')
            return redirect('Home')
        if not user.is_active:
            messages.error(req,'Your account is inactive. Please activate your account')
            return redirect('Home')
        user=authenticate(req,email=email,password=password)
        if user is not None:
            login(req,user)
            if user.is_seller:
                return redirect('seller_dashboard')
            elif user.is_customer:
                return redirect('customer_dashboard')
            else:
                messages.error(req,'You do not have permission to access this area.')
                return redirect('/')
        else:
            messages.error(req,'Invalid email or password')
            return redirect('/')

    return render(req,'core/login.html')

def register(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
            activation_url = f'{settings.SITE_DOMAIN}{activation_link}'  # ✅ Fixed typo

            send_activation_email(user.email, activation_url)  # ✅ Using correct variable

            messages.success(
                req,
                "Registration successful! Please check your email to activate your account."
            )
            return redirect('Home')  # ✅ Removed unnecessary form reset

    else:
        form = RegisterForm()
        
    return render(req, 'core/register.html', {'form': form})



def activate_account(req, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(req, 'This account has already been activated.')
            return redirect('Home')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(req, 'Your account has been activated successfully!')
        else:
            messages.error(req, 'The activation link is invalid or has expired.')

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(req, 'Invalid activation link.')  # ✅ Fixed typo

    return redirect('Home')
# @login_required
@login_and_role_required('seller')
def seller_dashboard(req):
    return render(req,'core/sdashboard.html')
# @login_required
@login_and_role_required('customer')
def customer_dashboard(req):
    return render(req,'core/cdashboard.html')

def forgot(req):
    if req.method=='POST':
        form=PasswordResetForm(req.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            user=User.objects.filter(email=email).first()
            if user:
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
                absolute_reset_url = f'{req.build_absolute_uri(reset_url)}'
                send_reset_password_email(user.email,absolute_reset_url)
            messages.success(req,('we have sent you a password reset link please cheack your email.'))
            return redirect('Home')

    else:
        form=PasswordResetForm()
    return render(req,'core/forgot.html',{'form':form})


def password_reset_confirm(req,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
        if not default_token_generator.check_token(user,token):
            messages.error(req,('This link has expired or is invalid.'))
            return redirect('forgot')
        if req.method=='POST':
            form=SetPasswordForm(user,req.POST)
            if form.is_valid():
                form.save()
                messages.success(req,('Your password has been successfully reset.'))
                return redirect('Home')
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(req,error)
        else:
            form=SetPasswordForm(user)
        return render(req,'core/reset.html',{'form':form,'uidb64':uidb64,'token':token})
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        messages.error(req,('An error occurred. Please try again later.'))
        return redirect('forgot')


    

@login_required
def change_password(req):
    
    if req.method=='POST':
        form=PasswordChangeForm(user=req.user,data=req.POST)
        if form.is_valid():
            form.save()
            logout(req)
            return redirect('Home')
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    messages.error(req,error)
    else:
        form=PasswordChangeForm(user=req.user)
    return render(req,'core/change_password.html')