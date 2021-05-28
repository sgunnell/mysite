# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ac(models.Model):
    mark = models.TextField(unique=True, blank=True, null=True)
    registration_type_id = models.TextField(blank=True, null=True)
    model_id = models.TextField(blank=True, null=True)
    manufacturer_id = models.TextField(blank=True, null=True)
    manufacturers_serial_number = models.TextField(blank=True, null=True)
    manufacturer_serial_compressed = models.TextField(blank=True, null=True)
    reg_basis_id = models.TextField(blank=True, null=True)
    ac_category_id = models.TextField(blank=True, null=True)
    date_of_import = models.TextField(blank=True, null=True)
    engine_manuf_e = models.TextField(blank=True, null=True)
    powerglider_flag = models.TextField(blank=True, null=True)
    engine_category_id = models.TextField(blank=True, null=True)
    number_of_engines = models.TextField(blank=True, null=True)
    number_of_seats = models.TextField(blank=True, null=True)
    air_weight_kilos = models.TextField(blank=True, null=True)
    sale_reported = models.TextField(blank=True, null=True)
    issue_date = models.TextField(blank=True, null=True)
    effective_date = models.TextField(blank=True, null=True)
    ineffective_date = models.TextField(blank=True, null=True)
    registered_purpose_id = models.TextField(blank=True, null=True)
    flight_authority_id = models.TextField(blank=True, null=True)
    manufacture_or_assembly = models.TextField(blank=True, null=True)
    country_asse_id = models.TextField(blank=True, null=True)
    date_manufacture_assembly = models.TextField(blank=True, null=True)
    country_base_id = models.TextField(blank=True, null=True)
    base_province_state_id = models.TextField(blank=True, null=True)
    city_airport_id = models.TextField(blank=True, null=True)
    type_certificate_id = models.TextField(blank=True, null=True)
    registration_auth_status_id = models.TextField(blank=True, null=True)
    multiple_owner_flag = models.TextField(blank=True, null=True)
    modified_date = models.TextField(blank=True, null=True)
    mode_s_transponder_binary = models.TextField(blank=True, null=True)
    physical_file_region_id = models.TextField(blank=True, null=True)
    ex_military_mark = models.TextField(blank=True, null=True)
    trimmed_mark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AC'


class AcCategory(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)
    type_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AC_CATEGORY'


class City(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CITY'


class CountryAsse(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)
    name_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COUNTRY_ASSE'


class CountryBase(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)
    name_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COUNTRY_BASE'


class EngineCategory(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)
    type_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ENGINE_CATEGORY'


class FileRegion(models.Model):
    region = models.TextField(unique=True, blank=True, null=True)
    region_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FILE_REGION'


class FlightAuthority(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)
    type_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FLIGHT_AUTHORITY'


class Manufacturer(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)
    common_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MANUFACTURER'


class Model(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MODEL'


class Owner(models.Model):
    mark = models.TextField(blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    trade_name = models.TextField(blank=True, null=True)
    street_name = models.TextField(blank=True, null=True)
    street_name2 = models.TextField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    province_or_state_id = models.IntegerField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    type_of_owner_id = models.IntegerField(blank=True, null=True)
    active_flag = models.TextField(blank=True, null=True)
    care_of = models.TextField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    owner_name_old_format = models.TextField(blank=True, null=True)
    mail_recipient = models.TextField(blank=True, null=True)
    trimmed_mark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OWNER'


class Ownership(models.Model):
    owner_id = models.IntegerField(blank=True, null=True)
    mark_id = models.AutoField(blank=True, null=True)
    type_of_owner_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OWNERSHIP'


class OwnerType(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)
    type_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OWNER_TYPE'


class ProvState(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)
    name_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROV_STATE'


class Region(models.Model):
    region_e = models.TextField(unique=True, blank=True, null=True)
    region_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REGION'


class RegisteredPurpose(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)
    type_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REGISTERED_PURPOSE'


class RegBasis(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)
    type_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REG_BASIS'


class RegStatus(models.Model):
    status = models.TextField(unique=True, blank=True, null=True)
    status_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REG_STATUS'


class RegType(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)
    type_f = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REG_TYPE'


class TypeCertNum(models.Model):
    type = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TYPE_CERT_NUM'
