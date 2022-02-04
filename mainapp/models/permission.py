from django.db.models import Model


class Access(Model):
    """
    This model is used to create content type for generic permissions
    """

    class Meta:
        app_label = "mainapp"
