
import html
import requests

from django.http import JsonResponse


from answer.models import Answer
from level.models import Level
from question.models import Question

def fetch_and_store_trivia_questions():
    url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=hard&type=multiple"
    response = requests.get(url)
    data = response.json()  # Convertir la respuesta a JSON

    # Obtener o crear el nivel de dificultad
    level, created = Level.objects.get_or_create(name='medium')

    for item in data['results']:
        question_text = html.unescape(item['question']) 
        correct_answer_text = html.unescape(item['correct_answer'])
        incorrect_answers_text = html.unescape(item['incorrect_answers'])

        # Crear la pregunta
        question = Question.objects.create(
            level=level,
            text=question_text,
            correct_answer=correct_answer_text,
            incorrect_answers=incorrect_answers_text
        )

        # Crear las respuestas
        Answer.objects.create(question=question, text=correct_answer_text, is_correct=True)
        for answer_text in incorrect_answers_text:
            Answer.objects.create(question=question, text=answer_text, is_correct=False)




def fetch_and_store(request):
    fetch_and_store_trivia_questions()
    return JsonResponse({'status': 'success'})
