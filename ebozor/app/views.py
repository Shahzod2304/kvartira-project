from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class Blog_SinglePageView(TemplateView):
    template_name = "blog_single.html"

class ProjectPageView(TemplateView):
    template_name = "project.html"

class TeamPageView(TemplateView):
    template_name= "team.html"

class BlogPageView(TemplateView):
    template_name= "blog.html"
    
class ContactPageView(TemplateView):
    template_name="contact.html"


