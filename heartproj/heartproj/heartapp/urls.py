
from django.urls import path
#import views.py to urls
from.import views
#add login page and signin page with path with the function naem created in view
urlpatterns = [
    path('login/',views.loginn,name='lin'),
    path('signup/',views.signup,name='sup'),
]