
# Meta-Capstone-Project_LittleLemon

Peer-review project as part for the fulfillment of Meta Back-end Developer Capstone Coursework 

## Note : model/view/serializer for Menu is renamed to MenuItem


## Initial Configuration

before initializing my project, please carefully follow the step in order to avoid errors:

- check database username and password settings:
```bash
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '## YOUR DATABASE NAME ##',
        'USER': '## YOUR DATABASE USERNAME ## ',
        'PASSWORD': '## YOUR DATABASE PASSWORD',
        'HOST': '127.0.0.1', 
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}

>> kindly check these settings again for smooth initialization :)
```
    
