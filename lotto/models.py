from django.db import models
from django.utils import timezone
import random


class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]')
    text = models.CharField(max_length=255)
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()

    def __str__(self):
        return '%s %s' % (self.name, self.text)

    def generate(self):
        self.lottos = ""
        origin = list(range(1, 46))
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
        self.update_date = timezone.now()
        self.save()


class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    name = models.CharField(max_length=30)


class Member(models.Model):
    id = models.CharField(max_length=20,
                          primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)