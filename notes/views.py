from django.shortcuts import render
from django.http import Http404
# Create your views here.

from .models import Notes

from django.views.generic import ListView, DetailView

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesListNewView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list_new.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
   
class NotesDetailNewView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail_new.html"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})

# def detail(request,pk):
#     try:
#         note_obj = Notes.objects.get(pk = pk)
#     except Notes.DoesNotExist:
#         raise Http404("Notes doesn't exist.")

    
#     return render(request, 'notes/notes_detail.html',{'note': note_obj})

