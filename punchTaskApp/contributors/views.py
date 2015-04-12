from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from punchTaskApp.contributors.forms import ContributorForm
from punchTaskApp.contributors.models import Contributor

def contributor_new(request, template='contributors/contributor_new.html'):
    if request.method == 'POST':
        form = ContributorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Create the User record
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # Create Contributor Record
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            cont = Contributor(city=city, state=state, user_rec=user)
            cont.save()
            # Process payment (via Stripe)
            # Auto login the user
            a_u = authenticate(username=username, password=password)
            if a_u is not None:
                if a_u.is_active:
                    login(request, a_u)
                    return HttpResponseRedirect(reverse('task_list'))
                else:
                    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))
            else:
                return HttpResponseRedirect(reverse('cont_new'))
        
    else:
        form = ContributorForm()

    return render(request, template, {'form':form})
