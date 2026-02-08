from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import LockerLoginForm, LockerVerifyForm
from .models import LockerUser, LockerFile, VerificationToken

def locker_login_view(request):
    # Matches Image 2 template initially
    if request.method == 'POST':
        form = LockerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Generate and save verification token
            verification = VerificationToken.objects.create(email=email)
            
            # Send email (ensure EMAIL settings are configured in settings.py)
            send_mail(
                'Your Curato Locker Code',
                f'Your 6-digit verification code is: {verification.token}',
                settings.DEFAULT_FROM_EMAIL or 'noreply@curato.online',
                [email],
                fail_silently=False,
            )
            
            # Store email in session temporarily for the next step
            request.session['locker_auth_email'] = email
            return redirect('lockerApp:verify')
    else:
        form = LockerLoginForm()

    # Using locker.html for the initial login screen as per Image 2 structure
    return render(request, 'locker.html', {'form': form, 'step': 'login'})

def locker_verify_view(request):
    # Matches verifyLocker.html template implied by file list
    email = request.session.get('locker_auth_email')
    if not email:
        return redirect('lockerApp:login')

    if request.method == 'POST':
        form = LockerVerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            
            try:
                # Check lastest valid token for this email
                token_obj = VerificationToken.objects.filter(email=email).latest('created_at')
                if token_obj.is_valid and token_obj.token == code:
                    # Success! Get or create user
                    user, created = LockerUser.objects.get_or_create(email=email)
                    
                    # Set authorized session
                    request.session['locker_user_id'] = user.id
                    del request.session['locker_auth_email'] # Clean up temp session
                    
                    return redirect('lockerApp:dashboard')
                else:
                     form.add_error('code', "Invalid or expired code.")
            except VerificationToken.DoesNotExist:
                 form.add_error('code', "No verification request found.")

    else:
        form = LockerVerifyForm(initial={'email': email})

    return render(request, 'verifyLocker.html', {'form': form, 'email': email})

def locker_dashboard_view(request):
    # Matches Image 0 template
    user_id = request.session.get('locker_user_id')
    if not user_id:
        return redirect('lockerApp:login')
    
    user = LockerUser.objects.get(id=user_id)
    files = user.files.all()

    context = {
        'user_email': user.email,
        'files': files
    }
    # Using the template shown in Image 0
    return render(request, 'locker.html', context)
