from django.db import models

class Account(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField()
    def __str__(self):
        return self.nom

class Video(models.Model):
    nom = models.CharField(max_length=100)
    matn = models.TextField(max_length=1000)
    video = models.FileField(blank=True)
    sana = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom



class Pleylist(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(blank=True)
    def __str__(self):
        return self.nom

class Obuna(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class History(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Like(models.Model):
    sana = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)



