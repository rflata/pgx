from django.db import models

# Create your models here.


class Activity(models.Model):
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_id = models.AutoField(db_column='\ufeffid', primary_key=True)
    level = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class Drug(models.Model):
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_id = models.IntegerField(db_column='\ufeffid', primary_key=True)
    generic_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug'


class Gene(models.Model):
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_id = models.IntegerField(db_column='\ufeffid', primary_key=True)
    symbol = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gene'


class Recommendation(models.Model):
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_id = models.AutoField(db_column='\ufeffid', primary_key=True)
    gene = models.ForeignKey(Gene, models.DO_NOTHING,
                             db_column='gene', blank=True, null=True)
    activity = models.ForeignKey(
        Activity, models.DO_NOTHING, db_column='activity', blank=True, null=True)
    drug = models.ForeignKey(Drug, models.DO_NOTHING,
                             db_column='drug', blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommendation'
