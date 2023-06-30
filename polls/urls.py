# In polls/urls.py

# Import the path function from Django's urls module
# This function lets you define routes for your app
# A route is a URL pattern that is associated with a view
# When a client requests a URL that matches a route, Django calls the associated view function
from django.urls import path

# Import the views module from the current directory (the polls app)
# This allows us to access the views we defined in views.py
from . import views

# Define the URL patterns for this app using a list named urlpatterns
# Each item in the list represents a different route
# In this case, we have just one route: the empty string ('')
# The empty string represents the root URL of this app
# When the client requests the root URL of this app, Django will call the "index" view and return its response to the client
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
