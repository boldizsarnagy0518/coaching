"""Local prototype defaults; production deployment requires a separate review."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() == "true"
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")
if not SECRET_KEY:
    if not DEBUG:
        raise RuntimeError("DJANGO_SECRET_KEY is required outside local development.")
    from django.core.management.utils import get_random_secret_key

    # Persist a local key without committing a shared development credential.
    secret_dir = BASE_DIR / ".local"
    secret_dir.mkdir(exist_ok=True)
    secret_path = secret_dir / "django-secret"
    try:
        with secret_path.open("x", encoding="utf-8") as secret_file:
            secret_file.write(get_random_secret_key())
    except FileExistsError:
        pass
    SECRET_KEY = secret_path.read_text(encoding="utf-8").strip()

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "training",
    "memory",
    "ops",
]
MIDDLEWARE = [
    "coaching.observability.RequestIdMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "coaching.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"], "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION = "coaching.wsgi.application"
DATABASES = {"default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": Path(os.environ.get("COACHING_DB_PATH", BASE_DIR / "db.sqlite3")),
    "OPTIONS": {
        # The web server and the MCP server share one file: wait for locks instead of failing at once,
        # take the write lock at transaction start, and let readers work while a write is in progress.
        "timeout": 20,
        "transaction_mode": "IMMEDIATE",
        "init_command": "PRAGMA journal_mode=WAL; PRAGMA synchronous=NORMAL;",
    },
}}
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
LANGUAGE_CODE = "hu"
TIME_ZONE = "Europe/Budapest"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_HTTPONLY = True

RUNNING_TESTS = len(sys.argv) > 1 and sys.argv[1] == "test"
LOG_LEVEL = os.environ.get("DJANGO_LOG_LEVEL", "WARNING" if RUNNING_TESTS else "INFO")
LOG_DIR = BASE_DIR / ".local" / "logs"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"request_id": {"()": "coaching.observability.RequestIdFilter"}},
    "formatters": {"plain": {"format": "%(asctime)s %(levelname)s %(name)s [%(request_id)s] %(message)s"}},
    "handlers": {
        # StreamHandler writes to stderr, which keeps the MCP server's stdout protocol clean.
        "console": {"class": "logging.StreamHandler", "filters": ["request_id"], "formatter": "plain"},
    },
    "loggers": {
        "coaching": {"handlers": ["console"], "level": LOG_LEVEL, "propagate": False},
        "django": {"handlers": ["console"], "level": "WARNING", "propagate": False},
    },
}
if os.environ.get("COACHING_LOG_FILE", "true" if DEBUG and not RUNNING_TESTS else "false").lower() == "true":
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOGGING["handlers"]["file"] = {
        "class": "logging.handlers.RotatingFileHandler", "filename": LOG_DIR / "app.log",
        "maxBytes": 2_000_000, "backupCount": 5, "encoding": "utf-8",
        "filters": ["request_id"], "formatter": "plain",
    }
    for logger in LOGGING["loggers"].values():
        logger["handlers"].append("file")

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
