from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteModelForm

def note_list_view(request):
    form = NoteModelForm()
    if request.method == "POST":
        form = NoteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note-list")

    todo_list = Note.objects.filter(finished=False)
    finished_list = Note.objects.filter(finished=True)
    context = {
        "form": form,
        "todo_list": todo_list,
        "finished_list": finished_list
    }
    return render(request, "note_list.html", context)


def finish_item(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.finished = True
    note.save()
    return redirect("note-list")


def recover_item(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.finished = False
    note.save()
    return redirect("note-list")


def delete_item(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("note-list")