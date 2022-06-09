from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class band(models.Model):
    
    def __str__(self):
        return f'{self.name}'
    
    class Genre(models.TextChoices):
        HIP_HOP='HP'
        SOUL='SL'
        ROCK='RK'
        METAL='ML'

    name=models.fields.CharField(max_length=110)
    genre=models.fields.CharField(choices=Genre.choices,null=True,max_length=5)
    biography=models.fields.CharField(max_length=1000)
    year_formed=models.fields.IntegerField(validators=[MinValueValidator(1970),MaxValueValidator(2040)],default=1970)
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True,blank=True)
 

class Listing(models.Model):
    class Type(models.TextChoices):
        disques='RECORDS'
        vêtements='CLOTHINGS'
        affiches='POSTERS'
    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=500)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(validators=[MinValueValidator(1950),MaxValueValidator(2050)])
    type=models.fields.CharField(choices=Type.choices,max_length=30)
    band=models.ForeignKey(band,on_delete=models.SET_DEFAULT,default=3)