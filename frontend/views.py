from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required


@login_required
@user_only
def homepage(request):
    context = {
        'activate_homepage': 'active'
    }
    return render(request, 'frontend/homepage.html', context)


