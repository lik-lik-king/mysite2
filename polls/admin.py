# Import the necessary Django modules. 
# The "admin" module is needed to customize Django's default admin interface.
from django.contrib import admin

# Import the "Question" model from the models module of the current directory (".models").
# This model defines the structure of the "Question" objects in the database which includes attributes like 
# 'question_text' and 'pub_date'. By importing this model, we are able to interface with the "Question" 
# data stored in our database.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# The previous implementation of QuestionAdmin class was as follows:
#
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']
#
# This setup displayed 'pub_date' and 'question_text' on the same line in the admin form. 
# However, we wanted these two fields to be separated into different fieldsets for better organization 
# and readability. Therefore, this implementation was replaced with the updated version below.

# Define a new class named "QuestionAdmin" which inherits from "admin.ModelAdmin".
# This class allows customization of how the "Question" model appears and behaves in the admin interface.
class QuestionAdmin(admin.ModelAdmin):
    # 'fieldsets' is a list of tuples, each representing a group (or "fieldset") of fields on the admin form.
    #
    # Each tuple contains two elements: 
    #   1) The title of the fieldset as a string (or None if no title is desired), and 
    #   2) A dictionary specifying options for the fieldset. The dictionary's 'fields' key is associated with a 
    #      list of fields to include in this fieldset.
    #
    # In this example, 'question_text' will appear in its own fieldset with no title, and 'pub_date' 
    # will appear in a fieldset titled 'Date information'. This setup provides better organization of the 
    # "Question" fields in the admin form.
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# Finally, register the "Question" model with the Django admin interface, specifying the custom admin class "QuestionAdmin". 
# When an admin user views or edits "Question" objects, they'll see the custom fieldsets defined above.
# This registration replaces the previous version, where the "Question" model was registered without 
# a custom admin class, which resulted in a less-organized display of fields.
list_display = ('question_text', 'pub_date', 'was_published_recently')
list_filter = ['pub_date']
search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
