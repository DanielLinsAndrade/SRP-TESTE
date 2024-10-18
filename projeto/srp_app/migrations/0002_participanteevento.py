# Generated by Django 4.2.5 on 2024-08-05 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("srp_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ParticipanteEvento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "data_criacao",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "data_atualizacao",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização"
                    ),
                ),
                (
                    "presenca",
                    models.BooleanField(default=False, verbose_name="Presença"),
                ),
                (
                    "evento",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="srp_app.evento",
                        verbose_name="Evento",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
                (
                    "usuario_atualizacao",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_requests_modified",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário de atualização",
                    ),
                ),
                (
                    "usuario_criacao",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_requests_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário de criação",
                    ),
                ),
            ],
            options={
                "verbose_name": "Participante do evento",
                "verbose_name_plural": "Participantes do evento",
            },
        ),
    ]
