# BadAppleBackend

A collaboration between [Priveasy](https://Priveasy.org) and the [Aaron Swartz Day Police Surveillance Project](https://www.aaronswartzday.org/psp/), [Bad Apple](https://BadApple.tools) provides valuable tools and resources with the aim of holding law enforcement accountable and putting an end to police misconduct.

------------

## Overview

This repository contains all of the production code powering the Bad Apple web application and database. Bad Apple exclusively uses open source technologies known for their security and efficiency. That's why we chose [Django](https://www.djangoproject.com/), [PostgreSQL](https://www.postgresql.org/), and [NginX](https://nginx.org/en/)—among many others—to run our services. For a breakdown of the main contents of this repository, see below:

### License

- [LICENSE](https://github.com/P5vc/BadAppleBackend/blob/main/LICENSE)
  - Bad Apple uses a Creative Commons Attribution Share Alike 4.0 International license

### Settings/Configuration

> Note: If you are looking for the server set-up and configuration, check out our [ServerConfigurations](https://github.com/P5vc/ServerConfigurations) repository

- [base.py](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/BadApple/settings/base.py)
  - Base, Django settings and configuration
- [nginx.conf](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/config/nginx.conf)
  - NginX configuration
- [uwsgi.ini](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/config/uwsgi.ini)
  - uWSGI configuration

### Web Application

- [mainSite](https://github.com/P5vc/BadAppleBackend/tree/main/BadApple/mainSite)
  - Base directory for the Django application
- [views.py](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/views.py)
  - Responsible for processing all HTTP requests
- [forms.py](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/forms.py)
  - Defines all of our web forms
- [urls.py](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/urls.py)
  - Defines our URL patterns

### Web Design

> Note: Soon, we will make available a separate repository containing non-minified/compressed resources and static versions of each web page, used by us internally to model new content.

- [templates](https://github.com/P5vc/BadAppleBackend/tree/main/BadApple/mainSite/templates)
  - The HTML templates used to render each web page
- [css](https://github.com/P5vc/BadAppleBackend/tree/main/BadApple/mainSite/static/css)
  - All of our stylesheets
- [img](https://github.com/P5vc/BadAppleBackend/tree/main/BadApple/mainSite/static/img)
  - The images used on the website

### Database

- [models.py](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/models.py)
  - Our database configuration
- [tasks.py](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/tasks.py)
  - Asynchronous database cleanup and maintenance tasks
- [admin.py](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/admin.py)
  - Our database admin portal

### Translations

- [locale](https://github.com/P5vc/BadAppleBackend/tree/main/BadApple/locale)
  - Base translations directory
- [django.po](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/locale/es/LC_MESSAGES/django.po)
  - Spanish language translations file
