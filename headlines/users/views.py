from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.urls import reverse_lazy

# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
