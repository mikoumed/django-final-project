from django.views.generic.edit import FormView
from users.forms import SignUpForm, UpdateProfileForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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



class UpdateProfile(UpdateView):
    redirect_authenticated_user = False
    model = User
    form_class = UpdateProfileForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['user_id'])



    def form_valid(self, form):
        user = User.objects.get(id=self.kwargs['user_id'])
        user.categories.set(form.cleaned_data['categories'])
        user.countries.set(form.cleaned_data['countries'])

        return super(UpdateProfile, self).form_valid(form)




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
