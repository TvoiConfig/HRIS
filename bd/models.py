from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Staff(models.Model):
    CHOICE_TYPE = (
        ('1', 'Полная ставка'),
        ('0.5', 'Неполная'),
    )

    name = models.CharField(max_length=50, verbose_name="ФИО")
    type = models.CharField(max_length=50, choices=CHOICE_TYPE, default='1', verbose_name="Ставка")
    character = models.TextField(max_length=100, verbose_name="Должность")
    image = models.ImageField(null=True, blank=True, upload_to="image/")

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'список сотрудников'

    def __str__(self):
        return self.name





class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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






class office(models.Model):
    number = models.CharField('Наименование отдела', default="", max_length=20)

    class Meta:
        # managed = False
        db_table = 'offices'
        verbose_name = 'отдел'
        verbose_name_plural = 'отделы'

    def __str__(self):
        return f'{self.number}'


class Application(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата и Время')
    auth_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Работник')
    number_cab = models.ForeignKey(office, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name='Выберите отдел')
    description = models.CharField('Зарплата', max_length=20)
    worker = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Выберите сотрудника',
    )


    class Meta:
        # managed = False
        db_table = 'applications'
        verbose_name = 'Выдача'
        verbose_name_plural = 'Выдачи'

    def __str__(self):
        return f'{self.id} Отдел.{self.number_cab} Заявитель {self.auth_user}'