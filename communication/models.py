from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models


class Event(models.TextChoices):
    CHUVA_EXCESSIVA = ("CHUVA_EXCESSIVA", "CHUVA_EXCESSIVA")
    GEADA = ("GEADA", "GEADA")
    GRANIZO = ("GRANIZO", "GRANIZO")
    SECA = ("SECA", "SECA")
    VENDAVAL = ("VENDAVAL", "VENDAVAL")
    RAIO = ("RAIO", "RAIO")


class Communication(models.Model):
    class Meta:
        db_table = "communication"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    owner_name = models.CharField(
        max_length=250,
    )
    owner_email = models.EmailField(max_length=250)
    owner_cpf = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                "^([0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[-][0-9]{2})$",
                message="Try the following pattern: XXX.XXX.XXX-XX",
            )
        ],
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField(max_length=50)
    date = models.DateField()
    event = models.CharField(
        max_length=50,
        choices=Event.choices,
    )

    def __str__(self):
        return f"{self.owner_name}: {self.event}"
