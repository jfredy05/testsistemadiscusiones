from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from apps.discuss.models import Question, Tag

class UserDetailView(DetailView):

	model = User
	template_name = 'user_detail.html'
	context_object_name = 'user'
	slug_field = 'username'

	def get_context_data(self, **kwargs):
		contexto = super(UserDetailView, self).get_context_data(**kwargs)
		questions = Question.objects.filter(user = contexto['object']).order_by('created')
		tags = [question.tag.all() for question in questions]
		contexto['ques_tags'] = zip(questions, tags)

		# redes sociales
		print '/'*40
		print contexto['object']
		facebook = contexto['object'].social_auth.filter(provider='facebook')
		print '*'*90
		print facebook
		if facebook:
			contexto['facebook'] = facebook[0].extra_data['id']

		twitter = contexto['object'].social_auth.filter(provider='twitter')
		print '='*90
		print twitter
		if twitter:
			contexto['twitter'] = twitter[0].extra_data['access_token']['screen_name']
		return contexto