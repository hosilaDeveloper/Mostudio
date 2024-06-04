from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStamp):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Home(TimeStamp):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Gallery(TimeStamp):
    title = models.CharField(max_length=255)
    second_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class About(TimeStamp):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Pricing(TimeStamp):
    title = models.CharField(max_length=255)
    photos = models.CharField(max_length=255)
    processing = models.CharField(max_length=255)
    type_of_camera = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    term = models.CharField(max_length=255)
    price = models.CharField(max_length=255)


class Contact(TimeStamp):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


