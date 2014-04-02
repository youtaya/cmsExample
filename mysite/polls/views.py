from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import Poll, choice
import logging

from django.views import generic

logger = logging.getLogger(__name__)

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}

	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/results.html', {'poll': poll})

# class IndexView(generic.ListView):
# 	template_name='polls/index.html'
# 	context_object_name='latest_poll_list'
# 
# 	def get_queryset(self):
# 		return Poll.objects.order_by('-pub_date')[:5]
# 
# class DetailView(generic.DetailView):
# 	model = Poll
# 	template_name='polls/detail.html'
# 
# class ResultsView(generic.DetailView):
# 	model = Poll
# 	template_name='polls/results.html'

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	logger.debug("post content %s" %request.POST)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'poll':p,
			'error_message': "You din't select a choice",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))