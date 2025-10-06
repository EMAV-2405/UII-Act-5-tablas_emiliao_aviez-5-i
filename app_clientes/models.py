from django.db import models

class Cliente(models.Model):
    # Campo para el nombre del cliente
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")

    # Campo para el correo electrónico del cliente, con validación de email
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    # Campo para la edad del cliente
    edad = models.IntegerField(null=True, blank=True, verbose_name="Edad")

    # Método para representar el objeto Cliente como una cadena (útil en el panel de administración)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre'] # Opcional: ordenar clientes por nombre por defe