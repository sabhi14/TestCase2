# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountDetails(models.Model):
    account_id = models.IntegerField(db_column='ACCOUNT_ID', primary_key=True)  # Field name made lowercase.
    account_name = models.CharField(db_column='ACCOUNT_NAME', max_length=100)  # Field name made lowercase.
    time_updated = models.DateTimeField(db_column='TIME_UPDATED')  # Field name made lowercase.

    class Meta:
        db_table = 'account_details'


class ProjectDetails(models.Model):
    project_id = models.IntegerField(db_column='PROJECT_ID', primary_key=True)  # Field name made lowercase.
    account = models.ForeignKey(AccountDetails, models.DO_NOTHING, db_column='ACCOUNT_ID')  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=45)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='START_DATE')  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='END_DATE')  # Field name made lowercase.
    time_updated = models.CharField(db_column='TIME_UPDATED', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'project_details'


class ResourceDetails(models.Model):
    resource_id = models.IntegerField(db_column='RESOURCE_ID', primary_key=True)  # Field name made lowercase.
    project = models.ForeignKey(ProjectDetails, models.DO_NOTHING, db_column='PROJECT_ID')  # Field name made lowercase.
    resource_name = models.CharField(db_column='RESOURCE_NAME', max_length=45)  # Field name made lowercase.
    technology = models.CharField(db_column='TECHNOLOGY', max_length=24)  # Field name made lowercase.
    doj = models.DateField(db_column='DOJ')  # Field name made lowercase.
    time_updated = models.DateTimeField(db_column='TIME_UPDATED')  # Field name made lowercase.

    class Meta:
        db_table = 'resource_details'
