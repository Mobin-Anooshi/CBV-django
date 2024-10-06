from django.urls import path
from . import views


app_name='home'
urlpatterns = [
    path('',views.HomeView.as_view(),name ='home'),
    path('1/',views.Home2View.as_view(),),
    path('2/',views.Home3View.as_view(),),
    path('3/',views.Home4View.as_view(),),
    path('4/<int:year>/<str:name>/<str:owner>/',views.Home5View.as_view(),name='car_detail'),
    path('5/',views.Home6View.as_view(),name='car_create'),
    path('6/',views.Home7View.as_view(),),
    path('7/<int:pk>/',views.Home8View.as_view(),name='car_delete'),
    path('8/<int:pk>/',views.Home9View.as_view(),name='car_update'),
    path('accounts/login',views.AccountsLoginView.as_view(),name='login'),
    path('accounts/logout/',views.AccountsLogout.as_view(),name='logout'),
    path('api/',views.HomeApiView.as_view()),
    path('api/<int:pk>',views.SingleCarView.as_view()),
    path('api/delete/<str:name>/',views.CarDeleteView.as_view()),
    path('api/create/',views.CarCreateView.as_view()),
    path('api/update/<int:pk>/',views.CArUpdateView.as_view()),
    path('api/a/',views.CarListCreateView.as_view()),

]
