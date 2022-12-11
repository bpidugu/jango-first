from django.urls import path
from . import views


# urlpatterns = [
#     path('notes', views.list),
#     path('notes/<int:pk>', views.detail),
# ]

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notesnew', views.NotesListNewView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
    path('notesnew/<int:pk>', views.NotesDetailNewView.as_view(), name="notes.detail"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]
