# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "mssql",
#         "NAME": "zz",
#         "USER": "SA",
#         "PASSWORD": "Admin123@",
#         "HOST": "127.0.0.1",
#         "PORT": "1444",
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}