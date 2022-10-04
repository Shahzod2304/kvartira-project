from django.urls import path
from .views import HomePageView,AboutPageView,Blog_SinglePageView,ProjectPageView,TeamPageView,BlogPageView,ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog_single/', Blog_SinglePageView.as_view(), name='blog_single'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('project/', ProjectPageView.as_view(), name='project'),
    # path('', ServicePageView.as_view(), name='home'),
    path('team/', TeamPageView.as_view(), name='team'),
    

]