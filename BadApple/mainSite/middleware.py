from django.urls import resolve

from mainSite.models import WeeklyStats


def simple_stats(get_response):

	def middleware(request):
		dateObj = datetime.today().isocalendar()
		statsObj = WeeklyStats.objects.get_or_create(week = dateObj[1] , year = dateObj[0])[0]

		# `name` is the path name as specified in ./urls.py
		name = resolve(request.path_info).url_name
		method = request.method

		if name == 'home':
			statsObj.homeViews += 1
			statsObj.totalViews += 1
		elif name == 'documentation':
			statsObj.documentationViews += 1
			statsObj.totalViews += 1
		elif name == 'pra' and method == 'GET':
			statsObj.praViews += 1
			statsObj.totalViews += 1
		elif name == 'pra' and method == 'POST':
			statsObj.praSearches += 1
			statsObj.totalInteractions += 1
		elif name == 'oversight':
			statsObj.oversightViews += 1
			statsObj.totalViews += 1
		elif name == 'commission' and method == 'GET':
			statsObj.commissionViews += 1
			statsObj.totalViews += 1
		elif name == 'commission' and method == 'POST':
			statsObj.commissionSearches += 1
			statsObj.totalInteractions += 1
		elif name == 'tip' and method == 'GET':
			statsObj.tipViews += 1
			statsObj.totalViews += 1
		elif name == 'tip' and method == 'POST':
			statsObj.tipSubmissions += 1
			statsObj.totalInteractions += 1
		elif name == 'badApple' and method == 'GET':
			statsObj.badAppleViews += 1
			statsObj.totalViews += 1
		elif name == 'badApple' and method == 'POST':
			statsObj.badAppleSearches += 1
			statsObj.totalInteractions += 1
		elif name == 'officer':
			statsObj.officerViews += 1
			statsObj.totalViews += 1
		elif name == 'report':
			statsObj.reportViews += 1
			statsObj.totalViews += 1
		elif name == 'apiDocumentation':
			statsObj.apiDocumentationViews += 1
			statsObj.totalViews += 1
		elif name == 'apiQuery':
			# TODO: Consider logging these
			pass
		else:
			print('Not properly logging request to path `' + name + '`; consider adding `elif name == "' + name + '": ...` to mainSite.middleware.simple_stats')

		statsObj.save()

		response = get_response(request)
		return response

	return middleware
