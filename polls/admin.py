from django.contrib import admin

from .models import Question, Choice # Must import the Question and Choice model in order to allow admin to change it

# Django Tutorial pt. 7
# admin.StackedInline takes up too much page space so use admin.TabularInline
class ChoiceInline(admin.TabularInline):
    # this tells django "Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices"
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin): # create a model admin class, be sure to add it to the second argument below
    fieldsets =[        # the first element of the each tuple in fieldset is the title of the fieldset
        (None,              {'fields': ['question_text']}), 
        ('Date information', {'fields': ['pub_date']}),
     ] 
    inlines = [ChoiceInline] # added from the above class
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin) # tells the admin that Question objects have an admin interface. Allows admin to change the questions.
