from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse

from .models import Question1,Choice1


def index(request):
    # mydata = Question.objects.all().values()
    mydata = Question1.objects.values_list('question_text')
    latest_question_list = Question1.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    # return HttpResponse(latest_question_list)
    # for q in mydata:
    #     return HttpResponse(q)

    # output = ', '.join([q.pub_date for q in latest_question_list])
    # return HttpResponse(output)

def detail(request, question_id):
    try:
        question = Question1.objects.get(pk=question_id)
    except Question1.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
from django.shortcuts import get_object_or_404, render




def results(request, question_id):
    question=get_object_or_404(Question1, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question1, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice1.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("results", args=(question.id,)))