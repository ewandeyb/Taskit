Guide in how i implemented the backend:
Firstly, install dependencies through requirements.txt
Then configure the settings:
**Installed Apps**
- add restframework
- add api
**Databases**
- postgresql
**REST FRAMEWORK**
- add
```
'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
```

run python manage.py startapp api here configure in the following order:
- model
- views
- urls
- serializers