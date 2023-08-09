from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class People(models.Model):\

    GENDER_CHOICES = [
        ("Female", "Female"),
        ("Male", "Male")
    ]

    POSITION_CHOICES = [
        ("Developer", "Developer"),
        ("Designer", "Designer"),
        ("Assistant", "Assistant")
    ]

    LANGUAGE_CHOICES = (
        ('English', 'English'),
        ('Mandarin', 'Mandarin'),
        ('Japanese', 'Japanese'),
        ('Korean', 'Korean')
    )

    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=64, choices=GENDER_CHOICES)
    age = models.IntegerField()
    position = models.CharField(max_length=64, choices=POSITION_CHOICES)
    language = MultiSelectField(max_length =64, choices=LANGUAGE_CHOICES)
    salary = models.IntegerField()
    _time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-_time']
        verbose_name = '人員列表'
        verbose_name_plural = '人員列表'