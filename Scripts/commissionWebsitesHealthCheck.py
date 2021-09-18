# A script to keep the Bad Apple Oversight Commission Database up-to-date by
# automatically checking the health of all of the links contained within and
# highlighting links with unexpected responses for manual review

from datetime import datetime
from getpass import getpass
import requests

# Complete location codes list, taken from https://github.com/P5vc/BadAppleBackend/blob/main/BadApple/mainSite/extendedModels/modelCodes.py
STATES_TERRITORIES_PROVINCES = ['USA-AL' , 'USA-AK' , 'USA-AS' , 'USA-AZ' , 'USA-AR' , 'USA-CA' , 'USA-CO' , 'USA-CT' , 'USA-DE' , 'USA-DC' , 'USA-FL' , 'USA-GA' , 'USA-GU' , 'USA-HI' , 'USA-ID' , 'USA-IL' , 'USA-IN' , 'USA-IA' , 'USA-KS' , 'USA-KY' , 'USA-LA' , 'USA-ME' , 'USA-MD' , 'USA-MA' , 'USA-MI' , 'USA-MN' , 'USA-MS' , 'USA-MO' , 'USA-MT' , 'USA-NE' , 'USA-NV' , 'USA-NH' , 'USA-NJ' , 'USA-NM' , 'USA-NY' , 'USA-NC' , 'USA-ND' , 'USA-MP' , 'USA-OH' , 'USA-OK' , 'USA-OR' , 'USA-PA' , 'USA-PR' , 'USA-RI' , 'USA-SC' , 'USA-SD' , 'USA-TN' , 'USA-TX' , 'USA-UT' , 'USA-VT' , 'USA-VI' , 'USA-VA' , 'USA-WA' , 'USA-WV' , 'USA-WI' , 'USA-WY']

apiKey = getpass('Please paste your API key, then press enter:\t').strip()

allResponses = []
totalCommissions = 0
counter = 0
for location in STATES_TERRITORIES_PROVINCES:
	counter += 1
	print('Making API Query (' , counter , '/' , len(STATES_TERRITORIES_PROVINCES) , ')...' , sep = '')
	response = requests.get('https://BadApple.tools/API/Oversight/' , headers = {'API-Key' : apiKey , 'State' : location})
	if ((response.status_code == 200) and (response.json()['statusCode'] == 200)):
		if (not(allResponses)):
			if ((response.json()['remainingQueries'] - (len(STATES_TERRITORIES_PROVINCES) - 1)) < 0):
				print('You do not have sufficient API query credits to run this script.\n' , len(STATES_TERRITORIES_PROVINCES) , ' credits are needed, however you only have ' , response.json()['remainingQueries'] , ' left.\n' , 'Please try again once your weekly query limit resets.\nExiting...' , sep = '')
				exit()
		allResponses.append(response)
		totalCommissions += len(response.json()['results'])
	else:
		print('Error' , results['statusCode'] , 'occurred while attempting to make the API request.\nExiting...')
		exit()

counter = 0
unexpectedResponses = []
for response in allResponses:
	for commission in response.json()['results']:
		counter += 1
		print('(' , counter , '/' , totalCommissions ,  ') Checking ' , commission['name'] , '...' , sep = '')
		notedPages = []
		if (commission['website']):
			try:
				pageResponse = requests.get(commission['website'] , timeout = 30)
				if (pageResponse.status_code != 200):
					notedPages.append(['Main Website' , str(pageResponse.status_code) , commission['website']])
			except:
				notedPages.append(['Main Website' , 'Timeout (>30s)' , commission['website']])
		if (commission['complaintInfo1']):
			try:
				pageResponse = requests.get(commission['complaintInfo1'] , timeout = 30)
				if (pageResponse.status_code != 200):
					notedPages.append(['Complaint Information 1' , str(pageResponse.status_code) , commission['complaintInfo1']])
			except:
				notedPages.append(['Complaint Information 1' , 'Timeout (>30s)' , commission['complaintInfo1']])
		if (commission['complaintInfo2']):
			try:
				pageResponse = requests.get(commission['complaintInfo2'] , timeout = 30)
				if (pageResponse.status_code != 200):
					notedPages.append(['Complaint Information 2' , str(pageResponse.status_code) , commission['complaintInfo2']])
			except:
				notedPages.append(['Complaint Information 2' , 'Timeout (>30s)' , commission['complaintInfo2']])
		if (commission['complaintForm']):
			try:
				pageResponse = requests.get(commission['complaintForm'] , timeout = 30)
				if (pageResponse.status_code != 200):
					notedPages.append(['Complaint Form' , str(pageResponse.status_code) , commission['complaintForm']])
			except:
				notedPages.append(['Complaint Form' , 'Timeout (>30s)' , commission['complaintForm']])
		if (commission['alternateComplaintForm']):
			try:
				pageResponse = requests.get(commission['alternateComplaintForm'] , timeout = 30)
				if (pageResponse.status_code != 200):
					notedPages.append(['Alternate Complaint Form' , str(pageResponse.status_code) , commission['alternateComplaintForm']])
			except:
				notedPages.append(['Alternate Complaint Form' , 'Timeout (>30s)' , commission['alternateComplaintForm']])
		if (commission['membersPage']):
			try:
				pageResponse = requests.get(commission['membersPage'] , timeout = 30)
				if (pageResponse.status_code != 200):
					notedPages.append(['Members Page' , str(pageResponse.status_code) , commission['membersPage']])
			except:
				notedPages.append(['Members Page' , 'Timeout (>30s)' , commission['membersPage']])
		if (commission['faqPage']):
			try:
				pageResponse = requests.get(commission['faqPage'] , timeout = 30)
				if (pageResponse.status_code != 200):
					notedPages.append(['FAQ Page' , str(pageResponse.status_code) , commission['faqPage']])
			except:
				notedPages.append(['FAQ Page' , 'Timeout (>30s)' , commission['faqPage']])
		if (notedPages):
			unexpectedResponses.append([commission['name'] , commission['commissionID'] , notedPages])

if (unexpectedResponses):
	resultsString = (str(len(unexpectedResponses)) + ' commissions\' websites did not respond with a 200 ("Success") status code.\n\nThis could be because the page was removed, moved to a different location,\nenforces "https" or "www" when the URL in our database only has "http", etc.\nIt could also be a false positive.\nManual review is requested for these websites.\n\nRESULTS:\n')
	for site in unexpectedResponses:
		resultsString += ('\nCommission Name:\t\t' + site[0] + '\nCommission Page URL:\t\thttps://BadApple.tools/Commission/' + site[1] + '/\nPages With Unexcpected Responses:\n')
		for page in site[2]:
			resultsString += ('\t' + page[0] + ' (' + page[1] + '):\t\t' + page[2] + '\n')

	resultsFileName = ('Results_' + datetime.now().strftime('%b_%d_%Y_%H%M') + '.txt')
	with open(resultsFileName , 'w') as resultsFile:
		resultsFile.write(resultsString)

	print(resultsString , '\n\nThese results have been saved in the current directory to "' , resultsFileName , '".' , sep = '')
else:
	print('Yay! No unexpected responses were detected.')
