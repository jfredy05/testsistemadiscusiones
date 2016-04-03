from django.shortcuts import render
from django.views.generic import ListView

from apps.discuss.models import Question

class IndexView(ListView):
	template_name = 'index.html'
	queryset = Question.objects.all()[:5]

	def get_queryset(self):
		tags = [question.tag.all() for question in self.queryset]
		return zip(self.queryset, tags)