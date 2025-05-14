from django.apps import AppConfig


class OurstatusMonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ourstatus_monitor'
    verbose_name = 'Add Computer'

    def ready(self):
        # Import signals if you have any signal handlers defined in your app
        try:
            import ourstatus_monitor
        except ImportError:
            pass