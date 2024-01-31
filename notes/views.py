# In notes/views.py
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render, redirect

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})

def note_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

@require_POST
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('index')

def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})

def about(request):
    return render(request, 'notes/about.html')
