from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import Question, Answers
from django.forms.formsets import formset_factory
import random


class HomeView(View):
    """
    Homepage view, the default view of the page. In order to allow a user add many answers we need two separate forms
    for the question and for answers
    """
    template_name = "questions/homepage.html"
    form = Question
    AnswersFormSet = formset_factory(Answers, extra=2)

    def get(self, request, *args, **kwargs):
        """
        Questions and answers are stored in request.session, which is flushed when the page is loading, so that a user
        can ask about new things
        """
        request.session.flush()
        form = self.form()  # Question form
        formset = self.AnswersFormSet()  # Answers formset
        return render(request, self.template_name, {'form': form, "formset": formset})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        formset = self.AnswersFormSet(request.POST)
        if formset.is_valid() and form.is_valid():
            answer_list = [frm.cleaned_data.get('answer') for frm in formset]  # get list of answers from clean formset
            form = form.cleaned_data  # get clean question form
            request.session["answers"] = answer_list  # store answers in session
            request.session["question"] = form["question"]  # store the question in session
        else:
            form = self.form()
            formset = self.AnswersFormSet()
        return HttpResponseRedirect('/result/', {'form': form, "formset": formset})


class ResultView(View):
    """
    Results page that shows the asked question and the chosen answer
    """
    template_name = "questions/result.html"

    def get(self, request, *args, **kwargs):
        if "answers" not in request.session.keys():  # in case someone tries to open /result directly
            return HttpResponseRedirect('/')
        else:
            answers = request.session["answers"]  # retrieve data from the session
            question = request.session["question"]
            chosen_answer = random.choice(answers)  # randomly choose an option for the user
            context = {
                "answer": chosen_answer,
                "question": question
            }
            return render(request, self.template_name, {"context": context})
