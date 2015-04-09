from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from punchTaskApp.contributors.forms import ContributorForm

def contributor_new(request, template='contributors/contributor_new.html'):
    if request.method == 'POST':
        form = ContributorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # Create the User record
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # Create Contributor Record
            # Process payment (via Stripe)
            # Auto login the user
            return HttpResponseRedirect('/success/')
    else:
        form = ContributorForm()

    return render(request, template, {'form':form})
