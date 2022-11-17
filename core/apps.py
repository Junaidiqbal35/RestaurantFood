from django.apps import AppConfig
from django.dispatch import receiver
from fieldsignals import pre_save_changed


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from core.models import TableReservation

        @receiver(pre_save_changed, sender=TableReservation, fields=['approved'])
        def update_reservation_status(sender, instance, **kwargs):
            print(instance.email)
            approved = instance.approved
            print(approved)
