from django.views.generic import TemplateView


class LandingView(TemplateView):
    template_name = 'public/landing.html'
