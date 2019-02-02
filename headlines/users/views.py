from django.views.generic.edit import FormView
from users.forms import SignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import User
from django.http import HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login


class SignUp(FormView):
    redirect_authenticated_user = False
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = User.objects.create_user(
            username = form.cleaned_data['username'],
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password1']
        )

        user.categories.set(form.cleaned_data['categories'])
        user.countries.set(form.cleaned_data['countries'])

        return super(SignUp, self).form_valid(form)





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
