# The include() function allows us to include the URLconf of other applications.
# The path() function is used to route URLs to appropriate view functions in your application.
from django.urls import include, path

# Import the urls module from the polls app. 
# This urls module contains the URL configuration specific to the polls app.
from polls import urls as polls_urls

# Import Django's admin module. The admin module provides a default, admin-only interface 
# for interacting with your Django application's models.
from django.contrib import admin

# Define the URL patterns for the project.
# Each URL pattern is represented by a call to the path() function.
# The first argument to path() is a string that specifies the URL pattern.
# The second argument is the view that should be used for that pattern.
# The include() function is used to include the URL configuration from another app (in this case, polls).
# By using include(), you're telling Django to chop off whatever part of the URL matched up to that point and send the remaining string to the included URLconf for further processing.
# When a user visits a URL that matches the pattern 'polls/', Django will send the remaining URL string to the polls.urls URLconf for further processing. 
# The path to 'admin/' sends the user to Django's built-in administration site, if a user types your site's domain followed by /admin/ in their browser, they will be taken to the admin site.
# This URL configuration is the base URL configuration for your entire Django project.
# When a user visits a URL in your web application, Django starts here to figure out what to do.
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]




