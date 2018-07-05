from django.db import models

class Group(models.Model):
    groupIndex = models.AutoField(db_column='groupIndex', primary_key=True)
    groupName = models.CharField(db_column='groupName', unique=True, max_length=50)
    essIndex24 = models.CharField(db_column='essIndex24', max_length=1024)
    essIndex5 = models.CharField(db_column='essIndex5', max_length=1024)
    apType = models.PositiveIntegerField(db_column='apType')
    active = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'tb_group'

