from django.db import models


class History(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    Gender = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Prefer Not to Say')
    )
    gender = models.IntegerField(choices=Gender)
    weight = models.FloatField()
    height = models.FloatField()
    heart_beat_rate = models.IntegerField()
    eye_blink_rate = models.IntegerField()
    emotion = models.CharField(max_length=10)
    speech_rate = models.IntegerField()

    def __str__(self):
        return self.name
