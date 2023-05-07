
from django.urls import path
#import views.py to urls
from.import views
#add login page and signin page with path with the function naem created in view
urlpatterns = [
    path('',views.homepage1,name='home1'),
    path('homepage2',views.homepage2,name='home2'),
    path('login',views.loginn,name='lin'),
    path('signup',views.signup,name='sup'),
    path('predict',views.predict,name='predict'),
]