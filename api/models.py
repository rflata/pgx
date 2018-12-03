# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    # Field name made lowercase.
    activityid = models.AutoField(db_column='ActivityID', primary_key=True)
    # Field name made lowercase.
    metabolism = models.CharField(db_column='Metabolism', max_length=40)

    class Meta:
        managed = False
        db_table = 'Activity'


class Drug(models.Model):
    # Field name made lowercase.
    drugid = models.AutoField(db_column='DrugID', primary_key=True)
    # Field name made lowercase.
    name_brand = models.CharField(
        db_column='Name_Brand', unique=True, max_length=50, blank=True, null=True)
    # Field name made lowercase.
    generic = models.CharField(
        db_column='Generic', unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Drug'


class Gene(models.Model):
    # Field name made lowercase.
    geneid = models.IntegerField(db_column='GeneID', primary_key=True)
    # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', unique=True, max_length=50)
    # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)

    class Meta:
        managed = False
        db_table = 'Gene'


class Patient(models.Model):
    # Field name made lowercase.
    patientid = models.AutoField(db_column='PatientID', primary_key=True)
    # Field name made lowercase.
    first = models.CharField(db_column='First', max_length=30)
    # Field name made lowercase.
    last = models.CharField(db_column='Last', max_length=45)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50)
    # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=40)
    # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)
    # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=50)
    # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Patient'


class PatientGenetics(models.Model):
    # Field name made lowercase.
    patientid = models.ForeignKey(
        Patient, models.DO_NOTHING, db_column='PatientID', primary_key=True)
    # Field name made lowercase.
    geneid = models.ForeignKey(Gene, models.DO_NOTHING, db_column='GeneID')
    # Field name made lowercase.
    activityid = models.ForeignKey(
        Activity, models.DO_NOTHING, db_column='ActivityID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Patient_Genetics'
        unique_together = (('patientid', 'geneid'),)


class Prescriber(models.Model):
    # Field name made lowercase.
    prescriberid = models.AutoField(db_column='PrescriberID', primary_key=True)
    # Field name made lowercase.
    first = models.CharField(db_column='First', max_length=30)
    # Field name made lowercase.
    last = models.CharField(db_column='Last', max_length=45)
    # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=20)
    # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50)
    # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=40)
    # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)
    # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=50)
    # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Prescriber'


class Prescription(models.Model):
    # Field name made lowercase.
    prescriptionid = models.AutoField(
        db_column='PrescriptionID', primary_key=True)
    # Field name made lowercase.
    prescriberid = models.ForeignKey(
        Prescriber, models.DO_NOTHING, db_column='PrescriberID')
    # Field name made lowercase.
    patientid = models.ForeignKey(
        Patient, models.DO_NOTHING, db_column='PatientID')
    # Field name made lowercase.
    drugid = models.ForeignKey(Drug, models.DO_NOTHING, db_column='DrugID')
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    # Field name made lowercase.
    dose = models.CharField(db_column='Dose', max_length=30)

    class Meta:
        managed = False
        db_table = 'Prescription'


class Recommendation(models.Model):
    # Field name made lowercase.
    recommendationid = models.AutoField(
        db_column='RecommendationID', primary_key=True)
    # Field name made lowercase.
    geneid = models.ForeignKey(Gene, models.DO_NOTHING, db_column='GeneID')
    # Field name made lowercase.
    drugid = models.ForeignKey(Drug, models.DO_NOTHING, db_column='DrugID')
    # Field name made lowercase.
    activityid = models.ForeignKey(
        Activity, models.DO_NOTHING, db_column='ActivityID')
    # Field name made lowercase.
    recommendation = models.CharField(
        db_column='Recommendation', max_length=50)

    class Meta:
        managed = False
        db_table = 'Recommendation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
