from django.urls import include
from polls import urls as polls_urls

# In mysite/urls.py

# Import Django's built-in admin module
# This module provides an admin site where authenticated users can create, update, and delete database records
from django.contrib import admin

# Import the include function and path function from Django's urls module
# The include function lets us include the URL configurations of other apps in this project's URL configuration
# The path function lets us define routes, just like in the app's URL configuration
from django.urls import include, path

# Define the URL patterns for the project using a list named urlpatterns
# Each item in the list represents a different route
# The first route begins with 'polls
urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]



