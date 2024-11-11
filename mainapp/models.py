from django.db import models

# Create your models here.
class contactModel(models.Model):
    contact_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=225)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=250)
    message=models.TextField(max_length=2000)
    contact_date=models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table ='contact_details'