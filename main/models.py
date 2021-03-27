# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Advertise(models.Model):
    id = models.BigAutoField(primary_key=True)
    categories = models.ForeignKey('Categories', models.DO_NOTHING)
    advertise_template = models.ForeignKey('AdvertiseTemplate', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='fk_advertise_user', blank=True, null=True)
    clients = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING, blank=True, null=True)
    start_issue = models.PositiveIntegerField(blank=True, null=True)
    end_issue = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    sort_order = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_paid = models.IntegerField()
    active = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    format = models.CharField(max_length=10, blank=True, null=True)
    newspaper_content = models.TextField(blank=True, null=True)
    imagefile = models.CharField(db_column='imageFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    views = models.IntegerField()
    who_created = models.ForeignKey('User', models.DO_NOTHING, related_name='fk_advertise_created', db_column='who_created', blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advertise'


class AdvertiseHasCategories(models.Model):
    advertise = models.ForeignKey(Advertise, models.DO_NOTHING)
    categories = models.ForeignKey('Categories', models.DO_NOTHING)
    advertise_template = models.ForeignKey('AdvertiseTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advertise_has_categories'


class AdvertiseHesFields(models.Model):
    id = models.BigAutoField(primary_key=True)
    advertise_template_fields = models.ForeignKey('AdvertiseTemplateFields', models.DO_NOTHING)
    advertise = models.ForeignKey(Advertise, models.DO_NOTHING)
    field_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'advertise_hes_fields'


class AdvertiseHesFieldsTranslate(models.Model):
    advertise_hes_fields = models.OneToOneField(AdvertiseHesFields, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    translate = models.TextField()

    class Meta:
        managed = False
        db_table = 'advertise_hes_fields_translate'
        unique_together = (('advertise_hes_fields', 'language'),)


class AdvertiseTemplate(models.Model):
    name = models.CharField(max_length=255)
    place_adv = models.ForeignKey('PlaceAdv', models.DO_NOTHING)
    type = models.CharField(max_length=6)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    price_description = models.CharField(max_length=255, blank=True, null=True)
    persent = models.IntegerField()
    template = models.TextField(blank=True, null=True)
    block_width = models.PositiveSmallIntegerField(blank=True, null=True)
    block_height = models.PositiveSmallIntegerField(blank=True, null=True)
    limit_long = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    status = models.IntegerField()
    base_lang = models.ForeignKey('Language', models.DO_NOTHING, db_column='base_lang', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advertise_template'


class AdvertiseTemplateFields(models.Model):
    advertise_template = models.ForeignKey(AdvertiseTemplate, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    requre = models.IntegerField()
    type = models.CharField(max_length=8)
    order = models.IntegerField()
    show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'advertise_template_fields'


class AdvertiseTemplateFieldsTranslate(models.Model):
    advertise_template_fields = models.OneToOneField(AdvertiseTemplateFields, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advertise_template_fields_translate'
        unique_together = (('advertise_template_fields', 'language'),)


class AdvertiseTemplateServices(models.Model):
    advertise_template = models.OneToOneField(AdvertiseTemplate, models.DO_NOTHING, primary_key=True)
    services = models.ForeignKey('Services', models.DO_NOTHING)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'advertise_template_services'
        unique_together = (('advertise_template', 'services'),)


class AdvertiseTemplateTranslate(models.Model):
    advertise_template = models.OneToOneField(AdvertiseTemplate, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advertise_template_translate'
        unique_together = (('advertise_template', 'language'),)


class AdvertiseTmpsort(models.Model):
    advertise = models.ForeignKey(Advertise, models.DO_NOTHING)
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'advertise_tmpsort'


class Area(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'area'


class AreaTranslate(models.Model):
    area = models.OneToOneField(Area, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'area_translate'
        unique_together = (('area', 'language'),)


class AuthAssignment(models.Model):
    item_name = models.OneToOneField('AuthItem', models.DO_NOTHING, db_column='item_name', primary_key=True)
    user_id = models.CharField(max_length=64)
    created_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_assignment'
        unique_together = (('item_name', 'user_id'),)


class AuthItem(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(primary_key=True, max_length=64)
    type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    rule_name = models.ForeignKey('AuthRule', models.DO_NOTHING, db_column='rule_name', blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_item'


class AuthItemChild(models.Model):
    parent = models.OneToOneField(AuthItem, models.DO_NOTHING, db_column='parent', primary_key=True)
    child = models.ForeignKey(AuthItem, models.DO_NOTHING, related_name='auth_item_child_ibfk_2', db_column='child')

    class Meta:
        managed = False
        db_table = 'auth_item_child'
        unique_together = (('parent', 'child'),)


class AuthRule(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    data = models.TextField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_rule'


class Categories(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories'


class CategoriesTranslate(models.Model):
    categories = models.OneToOneField(Categories, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categories_translate'
        unique_together = (('categories', 'language'),)


class Clients(models.Model):
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    registration_date = models.DateTimeField()
    registration_ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Discont(models.Model):
    advertise_template = models.ForeignKey(AdvertiseTemplate, models.DO_NOTHING)
    issues = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=9)
    discont_value = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'discont'


class ExtendAdvertiseTemplate(models.Model):
    advertise = models.OneToOneField(Advertise, models.DO_NOTHING, primary_key=True)
    advertise_template = models.ForeignKey(AdvertiseTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'extend_advertise_template'
        unique_together = (('advertise', 'advertise_template'),)


class FilemanagerMediafile(models.Model):
    filename = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    url = models.TextField()
    alt = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbs = models.TextField(blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filemanager_mediafile'


class FilemanagerMediafileTag(models.Model):
    mediafile = models.ForeignKey(FilemanagerMediafile, models.DO_NOTHING)
    tag = models.ForeignKey('FilemanagerTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filemanager_mediafile_tag'


class FilemanagerOwners(models.Model):
    mediafile = models.OneToOneField(FilemanagerMediafile, models.DO_NOTHING, primary_key=True)
    owner_id = models.IntegerField()
    owner = models.CharField(max_length=255)
    owner_attribute = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'filemanager_owners'
        unique_together = (('mediafile', 'owner_id', 'owner', 'owner_attribute'),)


class FilemanagerTag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'filemanager_tag'


class Invoices(models.Model):
    total_sum = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=8)
    created_at = models.IntegerField()
    clients = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class InvoicesHasAdvertise(models.Model):
    invoices = models.OneToOneField(Invoices, models.DO_NOTHING, primary_key=True)
    advertise = models.ForeignKey(Advertise, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'invoices_has_advertise'
        unique_together = (('invoices', 'advertise'),)


class Language(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=15)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'language'


class Migration(models.Model):
    version = models.CharField(primary_key=True, max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration'


class PlaceAdv(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=19)
    link = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=3)
    description = models.TextField(blank=True, null=True)
    resource = models.ForeignKey('Resource', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'place_adv'


class PlaceAdvHasCategories(models.Model):
    place_adv = models.OneToOneField(PlaceAdv, models.DO_NOTHING, primary_key=True)
    categories = models.ForeignKey(Categories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'place_adv_has_categories'
        unique_together = (('place_adv', 'categories'),)


class PlaceAdvTranslate(models.Model):
    place_adv = models.OneToOneField(PlaceAdv, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey(Language, models.DO_NOTHING)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'place_adv_translate'
        unique_together = (('place_adv', 'language'),)


class Profile(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    public_email = models.CharField(max_length=255, blank=True, null=True)
    gravatar_email = models.CharField(max_length=255, blank=True, null=True)
    gravatar_id = models.CharField(max_length=32, blank=True, null=True)
    avatar = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    ethnicity = models.CharField(max_length=255, blank=True, null=True)
    work_place = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'


class Resource(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resource'


class ResourceTranslate(models.Model):
    resource = models.OneToOneField(Resource, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey(Language, models.DO_NOTHING)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'resource_translate'
        unique_together = (('resource', 'language'),)


class Services(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=8)
    for_adv = models.CharField(max_length=6)
    radius_of_action = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'services'


class ServicesHasAdvertise(models.Model):
    services = models.ForeignKey(Services, models.DO_NOTHING)
    advertise = models.ForeignKey(Advertise, models.DO_NOTHING)
    advertise_template = models.ForeignKey(AdvertiseTemplate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_has_advertise'


class ServicesTranslate(models.Model):
    services = models.OneToOneField(Services, models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey(Language, models.DO_NOTHING)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'services_translate'
        unique_together = (('services', 'language'),)


class Settings(models.Model):
    name = models.CharField(unique=True, max_length=255)
    svalue = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'


class SocialAccount(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    provider = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_account'
        unique_together = (('provider', 'client_id'),)


class Token(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    code = models.CharField(max_length=32)
    created_at = models.IntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'token'
        unique_together = (('user', 'code', 'type'),)


class User(models.Model):
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    password_hash = models.CharField(max_length=60)
    auth_key = models.CharField(max_length=32)
    confirmed_at = models.IntegerField(blank=True, null=True)
    unconfirmed_email = models.CharField(max_length=255, blank=True, null=True)
    blocked_at = models.IntegerField(blank=True, null=True)
    registration_ip = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    flags = models.IntegerField()
    last_login_at = models.IntegerField(blank=True, null=True)
    maxad = models.PositiveSmallIntegerField(db_column='maxAd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class UserHasAdvertiseTemplate(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    advertise_template = models.ForeignKey(AdvertiseTemplate, models.DO_NOTHING)
    maxad = models.SmallIntegerField(db_column='maxAd')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_has_advertise_template'
        unique_together = (('user', 'advertise_template'),)
