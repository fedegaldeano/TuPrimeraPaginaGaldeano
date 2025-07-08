from django.db import models

ESTADOS_LICITACION = [
    ('pendiente', 'Pendiente'),
    ('en_curso', 'En curso'),
    ('finalizada', 'Finalizada'),
    ('anulada', 'Anulada'),
]

class EmpresaLicitante(models.Model):
    nombre = models.CharField(max_length=100)
    cuit = models.CharField(max_length=20)
    direccion = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Licitacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS_LICITACION)
    empresa = models.ForeignKey(EmpresaLicitante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.estado})"

class Licitador(models.Model):
    nombre = models.CharField(max_length=100)
    cuit = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Oferta(models.Model):
    licitador = models.ForeignKey(Licitador, on_delete=models.CASCADE)
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    propuesta_tecnica = models.TextField()
    propuesta_economica = models.TextField()
    fecha_presentacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Oferta de {self.licitador} para {self.licitacion}"
