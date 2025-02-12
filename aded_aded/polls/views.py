from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    Display the latest 5 poll questions.
    
    :param request: The HTTP request object.
    :return: Rendered template with the latest questions.
    """
    latest_questions = Question.objects.order_by('-pub_date')[:5]  # Latest 5 questions
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})

@login_required
def detail(request, question_id):
    """
    Display a specific question and its choices.
    
    :param request: The HTTP request object.
    :param question_id: The ID of the question to retrieve.
    :return: Rendered template with the question details.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required
def vote(request, question_id):
    """
    Handle user voting for a specific question.
    
    :param request: The HTTP request object.
    :param question_id: The ID of the question being voted on.
    :return: Redirects to the results page after voting or re-renders the question page on error.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)

@login_required
def results(request, question_id):
    """
    Display the results of a poll question.
    
    :param request: The HTTP request object.
    :param question_id: The ID of the question whose results are displayed.
    :return: Rendered template showing the question results.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
