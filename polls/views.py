from django.shortcuts import render

# Import the HttpResponse class from Django's http module
# This class lets you create HTTP responses that your views can send back to the client
# An HTTP response is what a web server sends back to a browser or client when it receives an HTTP request
from django.http import HttpResponse

# Define a new view function named "index"
# A view in Django is a Python function that takes a web request and returns a web response
# This function takes one parameter: an HttpRequest object, which represents the client's request
# In this case, our view just returns a simple HTTP response containing a string
# In a more complex app, the view might return an HTML document, a redirect, an error message, or any other type of HTTP response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")