# HeltG 
## A web application which helps people in their daily fitness upkeep. This application helps people to perform exercises more efficiently. Moreover, to make sure that they are not compromising exercises, the application provides gym equipment rental services from owners who are willing to rent them. Also, it sends out notifications to remind people of their daily exercise routine


The clean, fast and right way to start a new Django `4.0.5` powered website.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing

lease feel free to fix bugs, improve things, provide documentation. Just send a pull request.
