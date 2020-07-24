from django.shortcuts import render
from django.views import View
from django.contrib import messages


# Create your views here.
class HomeView(View):
    """
    Homepage view, default view of the website
    """
    template_name = "questions/homepage.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
