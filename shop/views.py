from django.shortcuts import render
from django.views import View
from django.views.generic import FormView


class IndexView(View):
    def get(self, request):
        return render(request, 'shop/base.html')



class RegistrationFormView(FormView):
    template_name = 'add_user.html'
    form_class = AddUserForm
    success_url = '/login'

    def form_valid(self, form):
        User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
        )
        return super().form_valid(form)