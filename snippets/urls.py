from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.SinppetList.as_view()),
    path('snippets/<int:pk>', views.SinppetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
