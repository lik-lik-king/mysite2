# Django's include() and path() functions are imported to include the URLconf of other applications
# and route URLs to the appropriate view functions.
from django.urls import include, path

# The URLs module from the polls app is imported. This module contains URL configuration for the polls app.
from polls import urls as polls_urls

# Django's admin module is imported. It provides a built-in, administration interface for the application's models.
from django.contrib import admin

# The URL patterns for the project are defined.
# Each URL pattern is represented by a call to the path() function.
# The first argument to path() is a string specifying the URL pattern, while the second argument is the view for the pattern.

# The include() function includes the URL configuration from the polls app.
# It tells Django to remove the part of the URL up to that point and send the remaining string to the included URLconf.
# When a user visits a URL matching the 'polls/' pattern, Django will redirect the remaining URL string to the polls.urls URLconf.

# The path to 'admin/' directs users to Django's built-in admin site. Typing the domain followed by /admin/ in a browser navigates to this site.

# This is the base URL configuration for the Django project.
# Django starts here when determining what to do when a user visits a URL in the web application.

# The line "Not Found: / [30/Jun/2023 19:43:48] "GET / HTTP/1.1" 404 2165" means that a request was made to the root URL ("/") of your server and a page wasn't found. 
# This is normal if you haven't defined a view for the root URL ("/") in your urls.py file.

# To navigate to the polls section of your project, enter "<your_server_address>/polls/" in your web browser.
# Replace "<your_server_address>" with the actual server address (for example, "127.0.0.1:8000/polls/" in a local development server).

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]





