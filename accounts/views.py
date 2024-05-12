from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from .forms import LoginForm, SignupForm, EditProfileForm
from .models import CustomUser, PasswordResetToken


def accounts(requests):
    return redirect('profile')

def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
        else: # the form is invalid there is an issue/s
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
        
    else: # the user method is get  
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"{user.username} has logged in successfully")
            return redirect('profile')

        else: # the form is invalid there is an issue/s
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    else: # the user method is get  
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', context={'user':request.user})

@login_required
def EditProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field} : {error}")
    else:
        form = EditProfileForm(instance=request.user)
    
    return render(request, 'accounts/editProfile.html', context={'form': form, 'user':request.user})

def ForgetPassword(request):
    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(email=request.POST.get('email'))
        except CustomUser.DoesNotExist:
            messages.error(request, "It looks like the email you provided us is not in our database would you like to signup")
            return render(request, 'accounts/reset_passwrod/forgetPassword.html')


        token = get_random_string(length=32)
        expires_at = timezone.now() + timezone.timedelta(minutes=30)

        PasswordResetToken.objects.create(user=user, token=token, expires_at=expires_at)

        # send email 
        reset_link = request.build_absolute_uri(f"/accounts/reset-password/{token}")
        html_message = render_to_string(template_name='accounts/Emails/reset_password.html', context={'reset_link': reset_link, 'user': user})
        subject = "Reset password request"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        email = EmailMessage(subject=subject, body=html_message, from_email=email_from, to=recipient_list)
        email.content_subtype = 'html'

        try:
            email.send(fail_silently=False)
            return render(request, 'accounts/reset_passwrod/reset-email-sent.html')
        
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
            messages.error(request, f"{e}")
        

    return render(request, 'accounts/reset_passwrod/forgetPassword.html')

def ResetPassword(request, token):
    try:
        reset_token = PasswordResetToken.objects.get(token=token)
    except PasswordResetToken.DoesNotExist:
        return render(request, 'accounts/reset_passwrod/invalid_token.html') # invalid token     

    if reset_token.is_expired():
        return render(request,'accounts/reset_passwrod/invalid_token.html') # token is expired

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confrim_password = request.POST.get('confirm_new_password')

        if new_password != confrim_password:
            messages.error(request, "Passwords must be the same")
            return render(request, 'accounts/reset_passwrod/reset_password.html')
        try:
            reset_token.user.set_password(new_password)
        except Exception as  e:
            messages.error(request, f"{e}")
            return render(request, 'accounts/reset_passwrod/reset_password.html')

        reset_token.user.save()

        reset_token.delete()
        return render(request, 'accounts/reset_passwrod/password_changed.html') # new password saved successfuly
    
    return render(request, 'accounts/reset_passwrod/reset_password.html')