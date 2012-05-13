from django.conf import settings
from django.db.models.loading import get_model


def get_profile_model():
    """
    Returns configured user profile model or None if not found
    """
    user_profile_module = getattr(settings, 'USER_PROFILE_MODULE', None)
    if user_profile_module:
        app_label, model_name = user_profile_module.split('.')
        return get_model(app_label, model_name)
    else:
        return None
