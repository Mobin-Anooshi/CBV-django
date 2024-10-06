from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView,DetailView ,CreateView,DeleteView,UpdateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib import messages
from .models import  Car
from .forms import CarCreateForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_view
from .serializers import CarSerializers
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView,UpdateAPIView,ListCreateAPIView



class HomeView(View):
    def get(self,request):
        return render(request,'home/index.html')

    def options(self, request, *args, **kwargs):
        response = super().options(request,*args,**kwargs)
        response.headers['host'] = 'local-host'
        response.headers['user'] = request.user
        return response

class Home2View(TemplateView):
    template_name = 'home/index2.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['cars']=Car.objects.all()
        return contex

class Home3View(RedirectView):
    # url = 'http://google.com'
    pattern_name = 'home:home'
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        print('-'*90)
        print('processing your request ... ')
        return super().get_redirect_url(*args,**kwargs)

class Home4View(ListView):
    template_name = 'home/index2.html'
    # model = Car
    # queryset = Car.objects.filter(year__gte=2000)
    context_object_name = 'cars'
    ordering = '-year'
    # allow_empty = False

    def get_queryset(self):
        result = Car.objects.filter(year__gte=2023)
        return result

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'mobin'
        return contex

class Home5View(DetailView):
    template_name = 'home/detail.html'
    model = Car
    # slug_field = 'name'
    # slug_url_kwarg = 'my_slug'

    def get_object(self, queryset=None):
        return Car.objects.get(
            year = self.kwargs['year'],
            name = self.kwargs['name'],
            owner = self.kwargs['owner'],
        )

class Home6View(FormView):
    template_name = 'home/create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        self._create_car(form.cleaned_data)
        messages.success(self.request,'create car successfully','success')
        return super().form_valid(form)


    def _create_car(self,data):
        Car.objects.create(name=data['name'],owner=data['owner'],year=data['year'])


class Home7View(CreateView):
    model = Car
    fields = ['name','year']
    template_name = 'home/create.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = self.request.user.username if self.request.user.username else 'nothing'
        car.save()
        messages.success(self.request,'create car successfully','success')
        return super().form_valid(form)

class Home8View(DeleteView):
    model = Car
    success_url = reverse_lazy('home:home')
    template_name = 'home/delete.html'

class Home9View(UpdateView):
    model = Car
    fields = ['name','year']
    success_url = reverse_lazy('home:home')
    template_name = 'home/update.html'

class AccountsLoginView(auth_view.LoginView):
    template_name = 'home/login.html'
    next_page = reverse_lazy('home:home')

class AccountsLogout(auth_view.LogoutView):
    next_page = reverse_lazy('home:home')

class HomeApiView(ListAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()

class SingleCarView(RetrieveAPIView):
    serializer_class =  CarSerializers
    queryset = Car.objects.all()
    # lookup_field = 'name'

class CarDeleteView(DestroyAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
    lookup_field = 'name'

class CarCreateView(CreateAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()

class CArUpdateView(UpdateAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()

class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
