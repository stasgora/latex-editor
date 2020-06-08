from django.apps import AppConfig


def create_moderator_group(sender, **kwargs):
    from django.contrib.auth.models import Group
    Group.objects.get_or_create(name='Moderatorzy')


class EditorAppConfig(AppConfig):
    name = 'editor_app'

    def ready(self):
        super().ready()
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_moderator_group, sender=self)
