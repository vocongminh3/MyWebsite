from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.viewlist, name="view_list"),
    path('detail/<int:question_id>', views.detailView, name="detail"),
    path('<int:question_id>', views.vote, name="vote"),
    path('tailieu', views.tailieu, name="tailieu"),
    path('cv', views.cv, name="cv"),
    path('xstk', views.xstk, name="xstk"),
    path('xstk1', views.xstk1, name="xstk1"),
]
