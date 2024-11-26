from django.db import models
from django.urls import reverse

# Create your models here.
class PersonasModelo(models.Model):
    dni = models.CharField(primary_key=True, max_length=32, db_collation='utf8mb3_spanish_ci')
    apellidos = models.CharField(max_length=50, db_collation='utf8mb3_spanish_ci')
    nombre = models.CharField(max_length=50, db_collation='utf8mb3_spanish_ci')
    externo = models.BooleanField()
    responsable = models.IntegerField()
    cientifico = models.IntegerField()
    superusuario = models.IntegerField(db_comment='superusuario de vehículos')
    baja = models.BooleanField()
    carnet = models.IntegerField()
    superusuario_intranet = models.IntegerField()
    directorio = models.BooleanField(db_comment='1 si aparece en el directorio web, 0 en caso contrario')
    no_persona = models.BooleanField()
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

    def get_absolute_url(self):
        return reverse('editar_persona', args=[self.dni])     
            
    class Meta:
        managed = True
        db_table = 'personas'
        
class VidaLaboral(models.Model):
    persona = models.ForeignKey(PersonasModelo, models.DO_NOTHING, db_column='persona')
    responsable = models.ForeignKey(PersonasModelo, models.DO_NOTHING, db_column='responsable', related_name='vidalaboral_responsable_set')
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)
    motivo_baja = models.CharField(max_length=22, blank=True, null=True)
   # salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
   # indemnizacion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
   # trienios = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
   #referencia = models.CharField(max_length=64, blank=True, null=True, db_comment='Columna código -> proyectos')
    dedicacion = models.CharField(max_length=8)
 #   exclusiva = models.IntegerField()
    
    ''' id_departamento = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='id_departamento')
    id_cuerpo_categoria = models.ForeignKey(CuerposCategorias, models.DO_NOTHING, db_column='id_cuerpo_categoria', blank=True, null=True)
    nivel = models.CharField(max_length=2, blank=True, null=True)
    id_tipo = models.ForeignKey(Tipos, models.DO_NOTHING, db_column='id_tipo')
    id_subtipo = models.ForeignKey(Subtipos, models.DO_NOTHING, db_column='id_subtipo')
    id_area_funcional = models.ForeignKey(AreasFuncionales, models.DO_NOTHING, db_column='id_area_funcional')
    id_puesto = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='id_puesto')
    observaciones = models.CharField(max_length=128, blank=True, null=True)
    '''
    class Meta:
        managed = True  
        db_table = 'vida_laboral'