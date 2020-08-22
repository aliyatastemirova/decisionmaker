from django.shortcuts import render
from django.views import View
from django.contrib import messages
from formtools.wizard.views import SessionWizardView, WizardView
from django.http import HttpResponseRedirect
from .forms import Question, Answers
from django.forms.formsets import formset_factory


# Create your views here.
# class HomeView(View):
#     """
#     Homepage view, default view of the website
#     """
#     template_name = "questions/homepage.html"
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)


class HomeView(View):
    template_name = "questions/homepage.html"
    form = Question
    QuestionsFormSet = formset_factory(Answers, extra=2)

    def get(self, request, *args, **kwargs):
        form = self.form()
        formset = self.QuestionsFormSet()
        return render(request, self.template_name, {'form': form, "formset": formset})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        formset = self.QuestionsFormSet(request.POST)
        if formset.is_valid() and form.is_valid():
            answer_list = [frm.cleaned_data.get('answer') for frm in formset]
            form = form.cleaned_data
            request.session["answers"] = answer_list
            request.session["question"] = form["question"]
            print(request.session["answers"])
        else:
            form = self.form()
            formset = self.QuestionsFormSet()
        return HttpResponseRedirect('/result/', {'form': form, "formset": formset})


class ResultView(View):
    template_name = "questions/result.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
