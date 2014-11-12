from django.db import models

# Create your models here.

class Inventory(models.Model):
    resume = models.CharField(max_length=200)
    date = models.DateTimeField('date')

    # def __unicode__(self):  # Python 3: def __str__(self):
    #     return self.resume
    
    def __init__(self, *args, **kwargs):
        super(Inventory, self).__init__(*args, **kwargs)
