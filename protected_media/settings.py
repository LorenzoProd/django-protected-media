from django.conf import settings
from django.utils.module_loading import import_string

if not hasattr(settings, "PROTECTED_MEDIA_ROOT") and not hasattr(settings, "BASE_DIR"):
    raise RuntimeError("The default value for PROTECTED_MEDIA_ROOT requires BASE_DIR to be an available setting.")

# Filesystem location to store protected media.
PROTECTED_MEDIA_ROOT = getattr(
    settings, "PROTECTED_MEDIA_ROOT", "%s/protected/" % settings.BASE_DIR
)

# The URL prefix used by protected media
PROTECTED_MEDIA_URL = getattr(
    settings, "PROTECTED_MEDIA_URL", "/protected/"
)

# An alternative prefix to use with servers like Nginx, where we want to
# disambiguate requests routed to Django and internal redirects to serve
# files.
PROTECTED_MEDIA_LOCATION_PREFIX = getattr(
    settings, "PROTECTED_MEDIA_LOCATION_PREFIX", PROTECTED_MEDIA_URL
)

# The server used to server the media. Django will always perform the
# authorisation.
PROTECTED_MEDIA_SERVER = getattr(
    settings, "PROTECTED_MEDIA_SERVER", "django"
)

# Controls whether the protected media are served as downloads. If True, the
# Content-Disposition flag will be set.
PROTECTED_MEDIA_AS_DOWNLOADS = False

# Default permission check function for protected media
# This setting allows users to define their own business logic for media access permissions.
# The function should accept two arguments: `user` and `path`, and return `True` if the user has
# the required access permissions, or `False` otherwise.
PROTECTED_MEDIA_CHECK_PERMISSION_FUNCTION = getattr(
    settings, "PROTECTED_MEDIA_CHECK_PERMISSION_FUNCTION", lambda user, path: True
)
