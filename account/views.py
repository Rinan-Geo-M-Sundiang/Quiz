from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.utils import timezone
from datetime import timedelta
from account.models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileCreationForm
from .models import Profile
from django.contrib import messages  # For showing error messages


User = get_user_model()


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SuperUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = SuperUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            is_superuser = form.cleaned_data.get('is_superuser')
            if is_superuser:
                user.is_superuser = True
                user.is_staff = True
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = SuperUserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            is_superuser = form.cleaned_data.get('is_superuser')
            if is_superuser:
                user.is_superuser = True
                user.is_staff = True
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Make sure 'home' is defined in your urls.py
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('view_profile')  # Redirect to view_profile after successful login
        else:
            messages.error(request, 'Invalid username or password')  # Show error message

    return render(request, 'account/login.html')  # Render login page on GET or auth failure


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'availability', 'last_donation_date']
    template_name = 'account/profile_update.html'
    success_url = '/profile/'

    def form_valid(self, form):
        profile = form.instance
        if profile.availability and (timezone.now().date() - profile.last_donation_date).days < 56:
            form.add_error('availability', 'You must wait 56 days between donations.')
            return super().form_invalid(form)
        return super().form_valid(form)

@login_required
def profile_creation(request):
    # Check if the user already has a profile
    if hasattr(request.user, 'profile'):
        # Redirect to the profile page if the user already has a profile
        return redirect('view_profile')

    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            # Save the profile but don't commit yet
            profile = form.save(commit=False)
            # Assign the logged-in user to the profile
            profile.user = request.user
            profile.save()
            # Redirect to the profile view or some other success page
            return redirect('view_profile')  # Replace 'view_profile' with the actual profile view URL name
    else:
        form = ProfileCreationForm()

    return render(request, 'account/profile_creation.html', {'form': form})

@login_required
def home(request):
    return redirect('view_profile')


@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'account/view_profile.html', {'profile': profile})
# Create your views here.
