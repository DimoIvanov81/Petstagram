from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30, default="Unnamed")

    personal_photo = models.URLField(blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)

    slug = models.SlugField(blank=True, null=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        super().save(*args, *kwargs)

    def __str__(self):
        return self.name
