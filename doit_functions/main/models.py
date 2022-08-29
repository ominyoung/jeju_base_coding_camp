from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    # 작성한 User의 아이디 => fk로 처리해야함
    user_id = models.CharField(max_length=20, blank=False)

    title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    star = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    companyName = models.CharField(max_length=40)
    licenseDate = models.CharField(max_length=30)
