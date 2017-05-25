from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Choice ,Question

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class Upload(generic.ListView):
    template_name="polls/upload.html"
    context_object_name='UploadingFile'
    def get_queryset(self):
        return Question.objects.all()
def handle_upload(request):
    print("eecec")
    if request.FILES:
        target_file = request.FILES['myfile']
        with open('polls/uploadfile/aaa.jpg','wb+') as des:
            for chunk in target_file.chunks():
                des.write(chunk)
        return HttpResponse('OK')
    return HttpResponse('failed')

class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"

class ResultsView(generic.DetailView):
    model=Question
    template_name="polls/results.html"
def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You did't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
