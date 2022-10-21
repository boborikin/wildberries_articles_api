from django.urls import path, re_path
from .views import UploadXLSXView, GetArticleInformationView


urlpatterns = [
    re_path(r'articles/(?P<filename>[^/]+)$', UploadXLSXView.as_view()),
    path("article/", GetArticleInformationView.as_view()),
]
