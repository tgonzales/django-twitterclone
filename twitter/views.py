from django.views.generic import RedirectView, TemplateView, CreateView, FormView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import UserCreateForm, UserStatusForm
from .models import Twitter

class HomeView(TemplateView):
    template_name = 'twitter/index.html'

class HomeTwitts(RedirectView):
    def get_redirect_url(self):	
        if self.request.user.is_authenticated():
            return reverse('status')
        else:
            return reverse('add-user')

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'twitter/user_form.html'
    success_url = reverse_lazy('home')

class UserStatusView(CreateView):
    model = Twitter	
    form_class = UserStatusForm
    template_name = 'twitter/status_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserStatusView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserStatusView, self).get_context_data(**kwargs)
        context['status_pub'] = self.model.objects.all().order_by('-creation_date')
        return context

        


