#from mysite import settings
#from django.core.management import setup_environ
#setup_environ(settings)
from django.conf import settings
settings.configure()
from polls.models import Question,Choice
counter=0
for x in Question.objects.all():
    counter=1
    print(x.id,x.question_text)
    for i in range(7):
        x.choice_set.create(choice_text="The %d choice"%i,votes=counter)
        x.save()