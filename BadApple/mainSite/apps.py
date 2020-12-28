from django.contrib.admin.apps import AdminConfig
from django.apps import AppConfig

class CustomAdminConfig(AdminConfig):
	default_site = 'mainSite.admin.CustomAdminSite'



class MainsiteConfig(AppConfig):
    name = 'mainSite'
