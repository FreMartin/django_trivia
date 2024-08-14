import random
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question


from question.models import Question #Paginar las preguntas

def questions(request):

    context = {}
    page_number = request.GET.get('page')   
    questions_list = Question.objects.all() 
    paginator = Paginator(questions_list, 1) 
    page_obj = paginator.get_page(page_number)

    if page_obj.object_list:
        question = page_obj.object_list[0]
        answers = list(question.answers.all())
        random.shuffle(answers)
    else:
        question = None
        answers = []

    context = {
        'question': question,
        'answers' : answers,
        'page_obj': page_obj
    }

    return render(request,'trivia_questions/trivia_questions.html', context)



