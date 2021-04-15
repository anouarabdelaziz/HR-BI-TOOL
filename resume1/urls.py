from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('recruit/', views.recruit, name='recruit'),
    path('consult/', views.consult, name='consult'),
    path('skills/<str:pk>/', views.skills, name='skills')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)