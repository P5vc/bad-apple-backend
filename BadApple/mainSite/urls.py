from django.urls import path
from mainSite import views

urlpatterns = [
				path('' , views.home , name = 'home'),
				path('LearnMore/' , views.documentation , name = 'documentation'),
				path('PRA/' , views.pra , name = 'pra'),
				path('Oversight/' , views.oversight , name = 'oversight'),
				path('Commission/<slug:slug>/' , views.commission , name = 'commission'),
				path('Tip/' , views.tip , name = 'tip'),
				path('BadAppleDatabase/' , views.badApple , name = 'badApple'),
				path('Officer/<slug:slug>/' , views.officer , name = 'officer'),
				path('Report/<slug:slug>/' , views.report , name = 'report'),
				path('API/<slug:slug>/' , views.apiQuery , name = 'apiQuery')
			]
