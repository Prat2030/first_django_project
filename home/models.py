from django.db import models

# Create your models here.
#  makemigrations : means that create changes and store it in a file.
#  migrate : means that apply the changes in the file that are pending by makemigrations.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(null=True, blank=True)
    # time = models.TimeField()

    def __str__(self):       # To take headings of the models do thisf
        return self.name
