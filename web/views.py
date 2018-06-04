from pprint import pprint

from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpRequest,HttpResponseRedirect

from django.urls import reverse
from django.views.generic import TemplateView

from api.models import Movies, Cast, Movies, Images, Videos, Sequals, Series, Seasons, Episodes, People, Actors, Cast, CrewPositions, Crew, Barners, Previews, Plans
from django.contrib.auth.models import User
from .forms import UserForm






def index(request):
    return render(request, 'index.html', {
        'barners': False,
        'request': request,
    })


def home(request):
    # my_partials = urls_by_namespace('partials')
    return render(request, 'dashboard/headers_footers/dashboard_block.html', {
        'is_authenticated': request.user.is_authenticated,
    })
# angular js partials
class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context

def live(request):
    return HttpResponse('<p>In live view</p>')
