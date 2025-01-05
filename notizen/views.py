from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import NoteForm

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notizen.html', {'notes': notes})


@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notiz_erstellen.html', {'form': form})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notiz_bearbeiten.html', {'form': form, 'note': note})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notiz_löschen.html', {'note': note})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'detailansicht.html', {'note': note})
