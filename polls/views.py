# We're importing several necessary modules and classes at the start. 
# Http404 will be used to raise HTTP 404 errors when a question isn't found.
# The render function will be used to produce the final HTML for our views.
# HttpResponse will be used to return basic HTTP responses with string content.
# The loader is used to load templates, but in this script we will stick to using the render function.
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# We import the Question model from the current package. 
# This model represents the questions in our application and is used to interact with the database.
from .models import Question

# This is a basic view function that Django will use to handle requests to the root URL of the polls application.
# A view function takes a web request and returns a web response. 
# Here we are returning an HttpResponse object with a simple string message.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# This index view is a bit more complex. Here we are accessing the database to get the five latest questions.
# We use the order_by method of QuerySets to order the questions by the publication date ('-pub_date').
# The slicing syntax [:5] gets the first five items in the QuerySet.
# We then create a dictionary called context, where the keys are the names we will use in the template,
# and the values are the actual Python objects.
# Finally, we use the render function to create an HttpResponse that fills a template with our context.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# This is the results view function. 
# It takes a question ID as a parameter and creates a response string using that ID.
# Then it returns an HttpResponse object that includes the response string.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# This is the vote view function. 
# It also takes a question ID as a parameter and creates a string message that includes the question ID.
# It returns an HttpResponse object that contains this message.
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# This is the detail view function. 
# It uses the get_object_or_404 function to get a Question object with a specific primary key (pk).
# If a matching Question object doesn't exist, get_object_or_404 raises an Http404 exception.
# It then creates an HttpResponse that renders a template. The template is filled with a context that includes the Question object.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
