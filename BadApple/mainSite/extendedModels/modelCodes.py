from django.utils.translation import gettext_lazy as _


# Types of Oversight Commissions:
COMMISSIONS = [
					('0' , _('Police Review Boards and Commissions')),
					('1' , _('Sheriff Review Boards and Commissions'))
				]

# Types of Oversight Commission Complaint Forms:
COMPLAINT_FORMS = [
					('0' , _('Complaint Form')),
					('1' , _('Complaint Form Menu')),
					('2' , _('Printable Complaint Form')),
					('a' , _('Complaint Form in Spanish')),
					('2a' , _('Printable Complaint Form in Spanish'))
				]

# Alpha-3 Country Codes (maximum length = 3):
COUNTRIES = [
				('USA' , 'United States of America')
			]

# Types of Investigative Report Findings:
FINDINGS = [
				('0' , _('Sustained')),
				('1' , _('Not Sustained')),
				('2' , _('Exonerated')),
				('3' , _('Unfounded'))
			]

# PRA Template Subjects:
PRA_SUBJECTS = [
				('0' , _('Body Worn Cameras')),
				('1' , _('Unmanned Aerial Vehicles (Drones)')),
				('2' , _('Facial Recognition')),
				('3' , _('Thermographic Cameras (FLIR)')),
				('4' , _('License Plate Readers')),
				('5' , _('Federal MOUs (Memoranda of Understanding)')),
				('6' , _('Predictive Policing')),
				('7' , _('Gunshot Detection Microphones (ShotSpotter)')),
				('8' , _('Social Media Monitoring')),
				('9' , _('IMSI-Catcher Equipment (Stingray)')),
				('10' , _('Police Misconduct - Based on the Officer\'s Name')),
				('11' , _('Police Misconduct - Based on the Incident'))
			]

# Alpha-3 Country Codes + Alpha-2 Territory Codes (maximum length = 6):
STATES_TERRITORIES_PROVINCES = [
								('USA-AL' , 'Alabama, USA'),
								('USA-AK' , 'Alaska, USA'),
								('USA-AS' , 'American Samoa, USA'),
								('USA-AZ' , 'Arizona, USA'),
								('USA-AR' , 'Arkansas, USA'),
								('USA-CA' , 'California, USA'),
								('USA-CO' , 'Colorado, USA'),
								('USA-CT' , 'Connecticut, USA'),
								('USA-DE' , 'Delaware, USA'),
								('USA-DC' , 'District of Columbia, USA'),
								('USA-FL' , 'Florida, USA'),
								('USA-GA' , 'Georgia, USA'),
								('USA-GU' , 'Guam, USA'),
								('USA-HI' , 'Hawaii, USA'),
								('USA-ID' , 'Idaho, USA'),
								('USA-IL' , 'Illinois, USA'),
								('USA-IN' , 'Indiana, USA'),
								('USA-IA' , 'Iowa, USA'),
								('USA-KS' , 'Kansas, USA'),
								('USA-KY' , 'Kentucky, USA'),
								('USA-LA' , 'Louisiana, USA'),
								('USA-ME' , 'Maine, USA'),
								('USA-MD' , 'Maryland, USA'),
								('USA-MA' , 'Massachusetts, USA'),
								('USA-MI' , 'Michigan, USA'),
								('USA-MN' , 'Minnesota, USA'),
								('USA-MS' , 'Mississippi, USA'),
								('USA-MO' , 'Missouri, USA'),
								('USA-MT' , 'Montana, USA'),
								('USA-NE' , 'Nebraska, USA'),
								('USA-NV' , 'Nevada, USA'),
								('USA-NH' , 'New Hampshire, USA'),
								('USA-NJ' , 'New Jersey, USA'),
								('USA-NM' , 'New Mexico, USA'),
								('USA-NY' , 'New York, USA'),
								('USA-NC' , 'North Carolina, USA'),
								('USA-ND' , 'North Dakota, USA'),
								('USA-MP' , 'Northern Mariana Islands, USA'),
								('USA-OH' , 'Ohio, USA'),
								('USA-OK' , 'Oklahoma, USA'),
								('USA-OR' , 'Oregon, USA'),
								('USA-PA' , 'Pennsylvania, USA'),
								('USA-PR' , 'Puerto Rico, USA'),
								('USA-RI' , 'Rhode Island, USA'),
								('USA-SC' , 'South Carolina, USA'),
								('USA-SD' , 'South Dakota, USA'),
								('USA-TN' , 'Tennessee, USA'),
								('USA-TX' , 'Texas, USA'),
								('USA-UT' , 'Utah, USA'),
								('USA-VT' , 'Vermont, USA'),
								('USA-VI' , 'Virgin Islands, USA'),
								('USA-VA' , 'Virginia, USA'),
								('USA-WA' , 'Washington, USA'),
								('USA-WV' , 'West Virginia, USA'),
								('USA-WI' , 'Wisconsin, USA'),
								('USA-WY' , 'Wyoming, USA')
							]

# Topics for submitted tips:
TIP_TOPICS = [
			('0' , _('PRA Templates')),
			('1' , _('Oversight Commissions')),
			('2' , _('Bad Apple Database')),
			('3' , _('Report Police Misconduct')),
			('4' , _('Ask a Question')),
			('5' , _('Media Inquiry')),
			('6' , _('Other'))
		]
