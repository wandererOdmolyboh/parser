from .manage_celery import celery_app

__all__ = ('celery_app',)
default_app_config = 'applications.background_tasks.admin.BackgroundTasksConfig'
