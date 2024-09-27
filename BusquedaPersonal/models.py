from django.db import models

# Create your models here.
class PersonasModelo(models.Model):
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
    id_ubicacion = models.IntegerField(blank=True, null=True)
    foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'