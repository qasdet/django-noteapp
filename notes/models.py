from django.db import models
from django.shortcuts import reverse


LABEL_CHOICES = (
    ('P', 'primary'),
    ('SE', 'secondary'),
    ('S', 'success'),
    ('DA', 'danger'),
    ('W', 'warning'),
    ('I', 'info'),
    ('L', 'light'),
    ('D', 'dark'),
)


class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_finish_item_url(self):
        return reverse("finish-note-item", kwargs={"pk": self.pk})
    
    def get_recover_item_url(self):
        return reverse("recover-note-item", kwargs={"pk": self.pk})
    
    def get_delete_item_url(self):
        return reverse("delete-note-item", kwargs={"pk": self.pk})
