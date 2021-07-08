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

## API Overview

Bad Apple does have an API available for use by other human rights organizations and developers looking for programmatic access to our databases. This API is simple to use, easy to implement, and follows many design standards: it accepts RESTful queries and returns beautifully-formatted JSON.

If you would like an API key, send a request to [Admin@BadApple.tools](mailto:Admin@BadApple.tools), and let us know who you are or what organization you represent, why you need access, what you plan to use our API for, and how many queries per week you expect to make.

Bad Apple provides rate-limited API access for free to qualifying developers of our choosing. However, if your use case requires making an extensive number of API queries, we may ask you to help cover the cost of the extra load placed on our servers. We may also require you to adhere to other security measures, such as providing us with a static IP address that we may pre-authorize to send a large number of queries.

### API Key

Once you receive your API key, be sure to store it in a secure location. This key will need to be sent along with all HTTP requests, and will be used to authenticate and uniquely identify you. If this key is ever leaked, it's important to notify us as soon as possible so that we may disable it and generate you a new one. If you fail to notify us in time, a malicious actor could use your key irresponsibly and get your account banned.

## API Documentation

### Authenticating a Request

The Bad Apple API only accepts authenticated, HTTP GET requests. To authenticate a request, you must provide an HTTP header with the key `API-Key` and a value matching that of your API key.

#### Examples of Properly-Authenticated Requests

Curl:

```bash
curl -X GET -H "API-Key: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" "https://BadApple.tools/API/Oversight"
```

Python:

```python3
import requests
response = requests.get('https://BadApple.tools/API/Oversight' , headers = {'API-Key' : 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'})
print(response.json())
```

### Filtering Data

Filters must be included with each GET request in the form of HTTP headers. Filters allow us to reduce network bandwidth, memory usage, and processing power, in order to keep our services quick and efficient for everyone. Under each service heading below, you will find a full list of each filter available, along with the corresponding HTTP header, accepted input format, examples, and any extra notes that may be necessary.

> **Please Note:** For a filter to be valid, unless a separate format has been explicitly defined, it must contain a minimum of two URL-safe characters, and no more than 100.

### Responses

All responses will be returned in JSON format, and contain the `statusCode` key. If a query is made successfully, a response containing a status code equal to `200` will be returned. If you receive a response containing any status code other than `200`, it is likely that your request contained an error, and should be examined before being resent.

Properly-authenticated requests will also receive `statusMessage` and `remainingQueries` items in their response. For successful requests, the status message will always be `Success`. If any error occurs while processing your request, the status message is a great place look for information on what went wrong. `remainingQueries` will show you how many queries you have left before your weekly cap is met. Keep in mind that even unsuccessful queries will count against your query limit.

All authenticated requests will contain a `results` list containing all of the objects matching their query. If no objects match your query, or your request was invalid, this list will be empty.

### Querying PRA Templates

URL: `https://BadApple.tools/API/PRA/`

#### Filters

| Header | Inclusion | Description | Format |
|:----------|:----------|:----------|:----------|
| `State` | **Required** | The state of the desired PRA template(s) | A six-character code as listed [here](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/extendedModels/modelCodes.py) in `STATES_TERRITORIES_PROVINCES` |
| `Subject` | **Required** | The subject of the desired PRA template(s) | A one-character or two-character code as listed [here](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/extendedModels/modelCodes.py) in `PRA_SUBJECTS` |

#### Example Query Headers

```json
{
	"API-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"State" : "USA-MA",
	"Subject" : "0"
}
```

```json
{
	"API-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"State" : "USA-CA",
	"Subject" : "10"
}
```

#### Example Response

### Querying Oversight Commissions

URL: `https://BadApple.tools/API/Oversight/`

#### Filters

| Header | Inclusion | Description | Format |
|:----------|:----------|:----------|:----------|
| `State` | **Required** | The state of the desired oversight commission(s) | A six-character code as listed [here](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/extendedModels/modelCodes.py) in `STATES_TERRITORIES_PROVINCES` |
| `City` | *Optional* | The city of the desired oversight commission(s) | String |

#### Example Query Headers

```json
{
	"API-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"State" : "USA-MA",
	"City" : "Boston"
}
```

```json
{
	"API-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"State" : "USA-CA",
}
```

#### Example Response

### Querying Bad Apple Database

URL: `https://BadApple.tools/API/BA/`

#### Filters

| Header | Description | Format |
|:----------|:----------|:----------|
| `First` | The first name of the officer about whom the report is written | String |
| `Last` | The last name of the officer about whom the report is written | String |
| `City` | The city for which the report was commissioned | String |
| `State` | The state in which the report was commissioned | A six-character code as listed [here](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/extendedModels/modelCodes.py) in `STATES_TERRITORIES_PROVINCES` |
| `Incident-Year` | The year in which the incident occurred | Four, consecutive integers |
| `Policy` | The category of the policies over which the report contained findings | A one-character or two-character code as listed [here](https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/extendedModels/modelCodes.py) in `POLICY_CATEGORIES` |

#### Example Query Headers

```json
{
	"API-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"First" : "Alex",
	"Last" : "Smith"
}
```

```json
{
	"API-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"Incident-Year" : "2008",
	"Policy" : "0"
}
```

```json
{
	"API-Key" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"Policy" : "38",
	"City" : "Berk",
	"State" : "USA-CA"
}
```