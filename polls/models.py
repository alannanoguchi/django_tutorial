import datetime # adds the datetime module

from django.db import models
from django.utils import timezone # adds django's time-zone-related utilities 

# Models are the database layout, with additional metadata
# each model is represented by a class that subclasses django.db.models.Model
# each nodel has a number of class variables, each of which represents a database field in the model
# each field is represented by an instance of a Field class - e.g., CharField for character fields


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): # returns the questions
        return self.question_text 


    def was_published_recently(self): # added with the above datetime and timezones imports
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self): # returns the choices
        return self.choice_text




# Use: [ $ python3 manage.py shell] to enter the interactive mode
# >>> from polls.models import Choice, Question # import these model classes
# >>> Question.objects.all() # shows all of the questions

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
# >>> from django.utils import timezone
# >>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
# >>> q.save()

# >>> Question.objects.filter(id=1) # filters the question to the one that matches the id=1
# >>> from django.utils import timezone
# >>> current_year = timezone.now().year
# >>> Question.objects.get(pub_date__year=current_year)
# >>> q = Question.objects.get(pk=1)
# >>> q.choice_set.all()
# >>> q.choice_set.create(choice_text="Not much", votes=0)
# >>> q.choice_set.create(choice_text="The sky", votes=0)
# >>> c = q.choice_set.create(choice_text='Just hacking', votes=0)
# >>> q.choice_set.count()
# >>> c = q.choice_set.filter(choice_text__startwith='Just hacking')
# >>> c.delete()

# To change the question text in the shell: follow the above 
# >>> q = Question.objects.get(question_text="What's new?")
# >>> q.question_text = "What's up?"
# >>> q.save()
# >>> Question.objects.all()

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
# >>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
# >>> q.choice_set.all()

# Create three choices.
# >>> q.choice_set.create(choice_text='Not much', votes=0)
# >>> q.choice_set.create(choice_text='The sky', votes=0)
# >>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)