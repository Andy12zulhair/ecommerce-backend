"""
Django settings for backend_project project.
"""

from pathlib import Path
import os  # <-- 1. TAMBAHKAN INI
import dj_database_url # <-- 2. TAMBAHKAN INI

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 3. BACA SECRET_KEY DARI RAILWAY
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tq&f9m_2m$+jar8(4w70i#9@@5%=f_vj-kto(l1@$ydkilcv^t')

# 4. BACA DEBUG DARI RAILWAY (Akan 'False' di server)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# 5. TAMBAHKAN HOSTS ANDA
# (Ganti 'railway.app' dan 'vercel.app' dengan URL Anda setelah deploy)
ALLOWED_HOSTS = [
    'ecommerce-backend-production.up.railway.app', # <-- Ganti dengan URL Railway Anda
    'ecommerce-frontend.vercel.app',  # <-- Ganti dengan URL Vercel Anda
    'localhost',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # APPS BARU
    'rest_framework',
    'django_filters',
    'corsheaders',
    'api',  # APP KITA
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Letakkan di atas
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# 6. GANTI SELURUH BLOK DATABASE DENGAN INI
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# 7. PERBARUI CORS UNTUK PRODUKSI
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173", 
    "https://ecommerce-frontend.vercel.app", # <-- Ganti dengan URL Vercel Anda
]

# 8. TAMBAHKAN INI UNTUK KEAMANAN
CSRF_TRUSTED_ORIGINS = [
    "https://ecommerce-backend-production.up.railway.app", # <-- Ganti dengan URL Railway Anda
    "https://ecommerce-frontend.vercel.app", # <-- Ganti dengan URL Vercel Anda
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
#