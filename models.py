# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AreasFuncionales(models.Model):
    nombre = models.CharField(max_length=64, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'areas_funcionales'


class AsociacionesFinanciacionCategoria(models.Model):
    id_financiacion = models.IntegerField()
    id_categoria = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asociaciones_financiacion_categoria'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargos(models.Model):
    nombre = models.CharField(max_length=20, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'cargos'


class CargosInfo(models.Model):
    desde = models.DateField()
    hasta = models.DateField()
    id_cargo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cargos_info'


class Convenios(models.Model):
    anyo = models.CharField(max_length=4, db_collation='utf8mb3_general_ci')
    titulo = models.CharField(max_length=128, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'convenios'


class Credenciales(models.Model):
    dni = models.OneToOneField('Personas', models.DO_NOTHING, db_column='dni', primary_key=True)
    pass_sha1 = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'credenciales'


class CuerposCategorias(models.Model):
    nombre = models.CharField(max_length=16)
    nivel_min = models.IntegerField(blank=True, null=True)
    nivel_max = models.IntegerField(blank=True, null=True)
    id_tipo = models.ForeignKey('Tipos', models.DO_NOTHING, db_column='id_tipo')

    class Meta:
        managed = False
        db_table = 'cuerpos_categorias'


class Departamentos(models.Model):
    nombre_corto = models.CharField(max_length=10, db_collation='utf8mb3_general_ci')
    nombre_largo = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'departamentos'


class DestinatariosAvisos(models.Model):
    destinatario = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'destinatarios_avisos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
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
    id = models.BigAutoField(primary_key=True)
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


class GruposInvestigacion(models.Model):
    id_departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_departamento')
    nombre = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'grupos_investigacion'


class Personas(models.Model):
    dni = models.CharField(primary_key=True, max_length=32, db_collation='utf8mb3_spanish_ci')
    apellidos = models.CharField(max_length=50, db_collation='utf8mb3_spanish_ci')
    nombre = models.CharField(max_length=50, db_collation='utf8mb3_spanish_ci')
    externo = models.IntegerField()
    responsable = models.IntegerField()
    cientifico = models.IntegerField()
    superusuario = models.IntegerField(db_comment='superusuario de vehículos')
    baja = models.IntegerField()
    carnet = models.IntegerField()
    superusuario_intranet = models.IntegerField()
    directorio = models.IntegerField(db_comment='1 si aparece en el directorio web, 0 en caso contrario')
    no_persona = models.IntegerField(blank=True, null=True)
    nif = models.CharField(unique=True, max_length=10, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    nie = models.CharField(unique=True, max_length=11, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    nrp = models.CharField(max_length=20, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    nss = models.CharField(max_length=14, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    sexo = models.CharField(max_length=1, db_collation='utf8mb3_spanish_ci')
    fecha_nacimiento = models.DateField(blank=True, null=True)
    pais_nacimiento = models.CharField(max_length=32, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    mail_institucional = models.CharField(max_length=64, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    mail_alternativo = models.CharField(max_length=64, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    telefono_personal_fijo = models.CharField(max_length=12, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    telefono_personal_movil = models.CharField(max_length=12, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    codigo_postal = models.CharField(max_length=5, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    domicilio = models.CharField(max_length=64, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    localidad_domicilio = models.CharField(max_length=50, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    provincia_domicilio = models.CharField(max_length=50, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    talla_ropa = models.CharField(max_length=16, blank=True, null=True)
    talla_zapatos = models.CharField(max_length=16, blank=True, null=True)
    id_ubicacion = models.IntegerField(blank=True, null=True)
    fecha_caducidad_carnet = models.DateField(blank=True, null=True)
    enlace = models.CharField(max_length=256, db_collation='utf8mb3_spanish_ci', blank=True, null=True)
    foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'


class Puestos(models.Model):
    nombre = models.CharField(max_length=128, db_collation='utf8mb3_general_ci')
    grupo = models.CharField(max_length=16, db_collation='utf8mb3_general_ci')
    titulacion_exigida = models.CharField(max_length=128, db_collation='utf8mb3_general_ci')
    mostrar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'puestos'


class Roles(models.Model):
    usuario = models.ForeignKey(Personas, models.DO_NOTHING, db_column='usuario')
    aplicacion = models.CharField(max_length=64)
    rol = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'roles'


class Salarios(models.Model):
    id_convenio = models.IntegerField()
    id_categoria = models.IntegerField()
    tiempo = models.DecimalField(max_digits=10, decimal_places=0)
    seguridad_social = models.DecimalField(max_digits=10, decimal_places=0)
    anyo = models.CharField(max_length=4, db_collation='utf8mb3_general_ci')
    paga = models.DecimalField(max_digits=10, decimal_places=0)
    desde = models.DateField(blank=True, null=True)
    hasta = models.DateField(blank=True, null=True)
    anulado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salarios'


class Subtipos(models.Model):
    nombre = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')
    cargoias = models.IntegerField(db_column='cargoIAS')  # Field name made lowercase.
    id_tipo = models.IntegerField(db_comment='Clave foránea a tipo')
    anulado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subtipos'


class TelefonoMovil(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Personas, models.DO_NOTHING, db_column='usuario')
    responsable = models.ForeignKey(Personas, models.DO_NOTHING, db_column='responsable', related_name='telefonomovil_responsable_set')
    reducido = models.IntegerField()
    numero = models.IntegerField()
    imei = models.CharField(max_length=16, blank=True, null=True)
    internet = models.IntegerField()
    baja = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'telefono_movil'


class Tipos(models.Model):
    nombre = models.CharField(max_length=32, db_collation='utf8mb3_general_ci')

    class Meta:
        managed = False
        db_table = 'tipos'


class Trienios(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    cuantia = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'trienios'


class UsuarioExtension(models.Model):
    usuario = models.ForeignKey(Personas, models.DO_NOTHING, db_column='usuario')
    responsable = models.ForeignKey(Personas, models.DO_NOTHING, db_column='responsable', related_name='usuarioextension_responsable_set')
    extension = models.IntegerField()
    exterior = models.CharField(max_length=9, blank=True, null=True)
    anulada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario_extension'


class VidaLaboral(models.Model):
    persona = models.ForeignKey(Personas, models.DO_NOTHING, db_column='persona')
    responsable = models.ForeignKey(Personas, models.DO_NOTHING, db_column='responsable', related_name='vidalaboral_responsable_set')
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)
    motivo_baja = models.CharField(max_length=22, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    indemnizacion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trienios = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    referencia = models.CharField(max_length=64, blank=True, null=True, db_comment='Columna código -> proyectos')
    dedicacion = models.CharField(max_length=8)
    exclusiva = models.IntegerField()
    id_departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_departamento')
    id_cuerpo_categoria = models.ForeignKey(CuerposCategorias, models.DO_NOTHING, db_column='id_cuerpo_categoria', blank=True, null=True)
    nivel = models.CharField(max_length=2, blank=True, null=True)
    id_tipo = models.ForeignKey(Tipos, models.DO_NOTHING, db_column='id_tipo')
    id_subtipo = models.ForeignKey(Subtipos, models.DO_NOTHING, db_column='id_subtipo')
    id_area_funcional = models.ForeignKey(AreasFuncionales, models.DO_NOTHING, db_column='id_area_funcional')
    id_puesto = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='id_puesto')
    observaciones = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vida_laboral'
