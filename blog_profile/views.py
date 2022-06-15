from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import UpdateUserForm
from django.urls import reverse_lazy

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='tasks')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'edit_profile.html', {'user_form': user_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('tasks')
