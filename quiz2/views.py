from django.shortcuts import redirect, render

from .models import Answer, Question


def index(request):
    questions = Question.objects.all()
    return render(request, "quiz2/index.html", {"questions": questions})


def question(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method == "POST":
        selected_answer_id = request.POST.get("answer")
        selected_answer = Answer.objects.get(id=selected_answer_id)
        return render(
            request,
            "quiz2/question.html",
            {"question": selected_answer.next_question},
        )

    return render(request, "quiz2/quiz.html", {"question": question})
