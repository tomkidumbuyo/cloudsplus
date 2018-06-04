from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    # my_partials = urls_by_namespace('partials')
    return render(request, 'admin_dashboard/headers_footers/dashboard_block.html', {
        'is_authenticated': request.user.is_authenticated,
    })

class PartialGroupView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        # update the context
        return context
