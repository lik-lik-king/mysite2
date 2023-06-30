from django.http import Http404
from django.shortcuts import render

# Import the HttpResponse class from Django's http module
# This class lets you create HTTP responses that your views can send back to the client
# An HTTP response is what a web server sends back to a browser or client when it receives an HTTP request
from django.http import HttpResponse

from django.template import loader

from .models import Question

# Define a new view function named "index"
# A view in Django is a Python function that takes a web request and returns a web response
# This function takes one parameter: an HttpRequest object, which represents the client's request
# In this case, our view just returns a simple HTTP response containing a string
# In a more complex app, the view might return an HTML document, a redirect, an error message, or any other type of HTTP response
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Define the index view function
# This function takes a web request and returns a web response
def index(request):
    # Retrieve the latest 5 question instances from the database
    # order_by('-pub_date') orders the instances by publication date in descending order
    # The slicing syntax [:5] limits the QuerySet to the first 5 items
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    # Define the context as a dictionary
    # The keys are the template variable names that will be replaced with actual values
    # In this case, 'latest_question_list' will be replaced with the actual latest_question_list
    context = {'latest_question_list': latest_question_list}
    
    # Return an HttpResponse that renders the specified template ('polls/index.html')
    # The template will be filled with the given context
    # The context variables in the template will be replaced with the actual values from the context dictionary
    # The render function does all these tasks for us
    return render(request, 'polls/index.html', context)


# This function handles the results view for a specific question.
# It takes two parameters: the request object and the question_id.
# It defines a response string with a placeholder for the question_id.
# It returns an HttpResponse object with the response string, where the placeholder is replaced with the question_id.

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# This function handles the vote view for a specific question.
# It takes two parameters: the request object and the question_id.
# It returns an HttpResponse object with a message that includes the question_id.

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})