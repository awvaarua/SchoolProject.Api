from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from professors import views

urlpatterns = [
    url(r'^professors/$', views.ProfessorList.as_view()),
    url(r'^professors/(?P<pk>[0-9]+)/$', views.ProfessorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
