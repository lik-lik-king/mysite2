# polls/urls.py

# First, we're importing the necessary modules:
from django.urls import path  # Django's function for defining URL routes
from . import views  # The views module of the current app (polls)

# Here we define the name of our app. This is useful when we're using namespacing for our app's URLs.
app_name = 'polls'  

# Define the URL patterns for the app in a list named "urlpatterns". 
# Each item in the list represents a different route. 
# Routes determine how URLs map to views, i.e., which function to call for a given URL.
urlpatterns = [
    # The first path function creates a route for the empty string (''), which in this case represents 
    # the root URL of the app. The second argument is the function to call when this URL is requested - 
    # here it's views.index. The name 'index' allows referring to this view in other parts of Django.
    path('', views.index, name='index'), 

    # The following paths are dynamic and take an argument 'question_id'. Django will match a number in the 
    # URL and pass it as 'question_id' to the given view. This is done by using angle brackets around the variable part.
    path('<int:question_id>/', views.detail, name='detail'),

    # A similar concept is applied for the 'results' and 'vote' views. The same 'question_id' will be passed into them.
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

