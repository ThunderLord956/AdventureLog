from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.forms import ValidationError
from django_resized import ResizedImageField

ADVENTURE_TYPES = [
    ('visited', 'Visited'),
    ('planned', 'Planned'),
]


# Assuming you have a default user ID you want to use
default_user_id = 1  # Replace with an actual user ID

User = get_user_model()


class Adventure(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, default=default_user_id)
    type = models.CharField(max_length=100, choices=ADVENTURE_TYPES)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    activity_types = ArrayField(models.CharField(
        max_length=100), blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = ResizedImageField(force_format="WEBP", quality=75, null=True, blank=True, upload_to='images/')
    date = models.DateField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.collection:
            if self.collection.is_public and not self.is_public:
                raise ValidationError('Adventures associated with a public collection must be public. Collection: ' + self.trip.name + ' Adventure: ' + self.name)
            if self.user_id != self.collection.user_id:
                raise ValidationError('Adventures must be associated with collections owned by the same user. Collection owner: ' + self.collection.user_id.username + ' Adventure owner: ' + self.user_id.username)

    def __str__(self):
        return self.name

class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, default=default_user_id)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # if connected adventures are private and collection is public, raise an error
    def clean(self):
        if self.is_public and self.pk:  # Only check if the instance has a primary key
            for adventure in self.adventure_set.all():
                if not adventure.is_public:
                    raise ValidationError('Public collections cannot be associated with private adventures. Collection: ' + self.name + ' Adventure: ' + adventure.name)

    def __str__(self):
        return self.name