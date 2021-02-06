from django.urls import path
from . import views

urlpatterns = [
				path('' , views.home , name = 'home'),
				path('PRA/' , views.pra , name = 'pra'),
				path('Oversight/' , views.oversight , name = 'oversight'),
				path('Commission/<slug:slug>/' , views.commission , name = 'commission')
			]
