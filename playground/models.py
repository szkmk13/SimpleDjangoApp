from django.db import models

from django.db.models import CASCADE


class Person(models.Model):
    name = models.TextField(max_length=30, unique=True)

    def __str__(self):
        return str(self.name)

    def sum_photos(self):
        sum = 0
        for x in Score.objects.filter(owner=self.id):
            sum += x.photos
        return sum

    def sum_messages(self):
        sum = 0
        for x in Score.objects.filter(owner=self.id):
            sum += x.messages
        return sum

    def sum_reactions(self):
        sum = 0
        for x in Score.objects.filter(owner=self.id):
            sum += x.reactions
        return sum

    def sum_feet(self):
        sum = 0
        for x in Score.objects.filter(owner=self.id):
            sum += x.feet
        return sum

    def sum_word(self):
        try:
            return Word.objects.filter(sender=self).order_by('-count').first().message
        except AttributeError:
            return 0

    def sum_word_count(self):
        try:
            return Word.objects.filter(sender=self).order_by('-count').first().count
        except AttributeError:
            return 0


class Word(models.Model):
    sender = models.ForeignKey(Person, on_delete=CASCADE)
    message = models.CharField(max_length=30)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.message + " " + str(self.count)

    def increase_count(self):
        self.count += 1
        self.save()


class ChatMessage(models.Model):
    sender = models.ForeignKey(Person, on_delete=CASCADE)
    message = models.CharField(max_length=200, default="")
    send_at = models.DateTimeField(auto_now_add=False)
    reactions = models.ManyToOneRel(Person, field_name="reactions", to="a")


class Score(models.Model):
    owner = models.ForeignKey(Person, on_delete=CASCADE)
    messages = models.PositiveSmallIntegerField(default=0)
    photos = models.PositiveSmallIntegerField(default=0)
    reactions = models.PositiveSmallIntegerField(default=0)
    feet = models.PositiveSmallIntegerField(default=0)
    date_from = models.DateField()
    date_to = models.DateField()
