from django.urls import path
from mainSite import views

urlpatterns = [
				path('' , views.home , name = 'home'),
				path('LearnMore' , views.documentation , name = 'documentation'),
				path('PRA/' , views.pra , name = 'pra'),
				path('Oversight/' , views.oversight , name = 'oversight'),
				path('Commission/<slug:slug>/' , views.commission , name = 'commission')
			]
