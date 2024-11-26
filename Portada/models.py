from django.db import models

from django.db import models

class Directorio(models.Model):
    nombre = models.CharField(max_length=255)
    carpeta_padre = models.ForeignKey('self', null=True, blank=True, related_name='subdirectorios', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

