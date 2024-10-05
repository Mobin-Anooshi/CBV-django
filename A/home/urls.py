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
    # path('5/',views.Home6View.as_view(),),
]
