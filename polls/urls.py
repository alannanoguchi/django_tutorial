from django.urls import path

from . import views

app_name = 'polls' # add this so that django can differentiate the URL names for other apps

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # recall using the {% url % } tag in templates, the 'name' value is called by this template tag
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]