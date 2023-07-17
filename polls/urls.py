from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("details/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("results/<int:question_id>/", views.results, name="results"),
    # path('', views.IndexView.as_view(), name='index'),
    # path('details/<int:question_id>/', views.DetailView.as_view(), name='detail'),
    # path('results/<int:question_id>/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

]