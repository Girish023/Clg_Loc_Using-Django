from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class DjangoVarity(models.Model):
    DJANGO_TYPE_CHOICE=[
        ('ML','MACHINE'),
        ('LR','LEARNING'),
        ('AI','ARTIFICIAL'),
        ('DS','DATA'),
        ('SC','SCIENCE')
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Djangos/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=DJANGO_TYPE_CHOICE)
    description=models.TextField(default='')

    def __str__(self):
        return self.name

    



#One to many 

class PojectReview(models.Model):
    project=models.ForeignKey(DjangoVarity,on_delete=models.CASCADE,related_name="reviews")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comments=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.Django_details.name} '


#Many to many

class subjects(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    sub_variety=models.ManyToManyField(DjangoVarity,related_name='subjects')


    def __str__(self) :
        return self.name
    

#One to one

class Certificate(models.Model):
    Certi=models.OneToOneField(DjangoVarity,on_delete=models.CASCADE,related_name='Certificatess')
    certificate_number=models.CharField(max_length=100)
    issued_data=models.DateTimeField(default=timezone.now)
    valid_untill=models.DateTimeField()


    def __str__(self) :
        return f'Certificate for {self.name.Django_details}'