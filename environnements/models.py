from django.db import models

class Environnement(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, db_index=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Type(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, db_index=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Status(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    STATUS_RESULT = (
        ('O', 'Ok'),
        ('K', 'Ko'),
        ('E', 'En cours'),
        ('A', 'A faire'),
    )
    result = models.CharField(max_length=1, choices=STATUS_RESULT)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    environnement = models.ForeignKey(Environnement, on_delete=models.CASCADE)
    date_exec = models.DateField()
    def __str__(self):
        return self.environnement + "_" + self.type + "_" + self.result + "_" + self.date_exec