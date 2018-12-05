"""
Django settings for myweb project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-ae#0t0qiqlzduq%x+3&k6d6s#1+czw9c2a)$pv^=vcwss*9kg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'blog',
    'useroperations',
    'reading_statistics',
    'comment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates')
        ],
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

WSGI_APPLICATION = 'myweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS  = [
    os.path.join(BASE_DIR,'static')
]

PAGENATOR_BLOG_COUNT = 5
PAGENATOR_DISPLAY_LIST_SIZE = 7

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#ckeditor 富文本上传文件配置

CKEDITOR_UPLOAD_PATH = 'upload/'
#ckeditor 配置wigget

CKEDITOR_CONFIGS = {
    'default':{
         'toolbar':'custom',
        'toolbar_custom':[
            ['Blod','Italic','UnderLine','Strike','Subscript','Superscript'],
            ['ImageButton'],
            ['TextColor','BGColor','RemoveFormat'],
            ['NumberedList','BulletedList'],
            ['Smiley','SpecialChar','Blockquote'],
            ['Source'],
        ],
        'width':'auto',
        'height':'180',
        'tabSpaces':4,
        'removePlugins':'elementspath',
        'resize_enabled':False,
    },
    'comment_ckeditor':{
        'toolbar':'custom',
        'toolbar_custom':[
            ['Blod','Italic','UnderLine','Strike','Subscript','Superscript'],
            ['ImageButton'],
            ['TextColor','BGColor','RemoveFormat'],
            ['NumberedList','BulletedList'],
            ['Smiley','SpecialChar','Blockquote'],
        ],
        'width':'auto',
        'height':'180',
        'tabSpaces':4,
        'removePlugins':'elementspath',
        'resize_enabled':False,
    }
}

#login_required 跳转
# contrib.auth 下要 LOGIN_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'