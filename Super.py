##############################################
#              Ultis_Gaurav                  #
#          ALL code by Gaurav.Shukla         #
#               v:0.1(01/03/2023)            #
#              CC0 license applies           #
##############################################
import time  # gives access to the time module
import speech_recognition as sr  # gives access to the Speech recognition module
import pyttsx3  # gives access to the Pyttsx3 module
from chatterbot import ChatBot  # gives access to the Chatterbot module
from chatterbot.trainers import ChatterBotCorpusTrainer  # gives access to the chatterbot trainer dataset
from random import *
countries = [
    {'timezones': ['Europe/Andorra'], 'code': 'AD', 'continent': 'Europe', 'name': 'Andorra',
     'capital': 'Andorra la Vella'},
    {'timezones': ['Asia/Kabul'], 'code': 'AF', 'continent': 'Asia', 'name': 'Afghanistan', 'capital': 'Kabul'},
    {'timezones': ['America/Antigua'], 'code': 'AG', 'continent': 'North America', 'name': 'Antigua and Barbuda',
     'capital': "St. John's"},
    {'timezones': ['Europe/Tirane'], 'code': 'AL', 'continent': 'Europe', 'name': 'Albania', 'capital': 'Tirana'},
    {'timezones': ['Asia/Yerevan'], 'code': 'AM', 'continent': 'Asia', 'name': 'Armenia', 'capital': 'Yerevan'},
    {'timezones': ['Africa/Luanda'], 'code': 'AO', 'continent': 'Africa', 'name': 'Angola', 'capital': 'Luanda'},
    {'timezones': ['America/Argentina/Buenos_Aires', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy',
                   'America/Argentina/Tucuman', 'America/Argentina/Catamarca', 'America/Argentina/La_Rioja',
                   'America/Argentina/San_Juan', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos',
                   'America/Argentina/Ushuaia'], 'code': 'AR', 'continent': 'South America', 'name': 'Argentina',
     'capital': 'Buenos Aires'},
    {'timezones': ['Europe/Vienna'], 'code': 'AT', 'continent': 'Europe', 'name': 'Austria', 'capital': 'Vienna'},
    {'timezones': ['Australia/Lord_Howe', 'Australia/Hobart', 'Australia/Currie', 'Australia/Melbourne',
                   'Australia/Sydney', 'Australia/Broken_Hill', 'Australia/Brisbane', 'Australia/Lindeman',
                   'Australia/Adelaide', 'Australia/Darwin', 'Australia/Perth'], 'code': 'AU', 'continent': 'Oceania',
     'name': 'Australia', 'capital': 'Canberra'},
    {'timezones': ['Asia/Baku'], 'code': 'AZ', 'continent': 'Asia', 'name': 'Azerbaijan', 'capital': 'Baku'},
    {'timezones': ['America/Barbados'], 'code': 'BB', 'continent': 'North America', 'name': 'Barbados',
     'capital': 'Bridgetown'},
    {'timezones': ['Asia/Dhaka'], 'code': 'BD', 'continent': 'Asia', 'name': 'Bangladesh', 'capital': 'Dhaka'},
    {'timezones': ['Europe/Brussels'], 'code': 'BE', 'continent': 'Europe', 'name': 'Belgium', 'capital': 'Brussels'},
    {'timezones': ['Africa/Ouagadougou'], 'code': 'BF', 'continent': 'Africa', 'name': 'Burkina Faso',
     'capital': 'Ouagadougou'},
    {'timezones': ['Europe/Sofia'], 'code': 'BG', 'continent': 'Europe', 'name': 'Bulgaria', 'capital': 'Sofia'},
    {'timezones': ['Asia/Bahrain'], 'code': 'BH', 'continent': 'Asia', 'name': 'Bahrain', 'capital': 'Manama'},
    {'timezones': ['Africa/Bujumbura'], 'code': 'BI', 'continent': 'Africa', 'name': 'Burundi', 'capital': 'Bujumbura'},
    {'timezones': ['Africa/Porto-Novo'], 'code': 'BJ', 'continent': 'Africa', 'name': 'Benin', 'capital': 'Porto-Novo'},
    {'timezones': ['Asia/Brunei'], 'code': 'BN', 'continent': 'Asia', 'name': 'Brunei Darussalam',
     'capital': 'Bandar Seri Begawan'},
    {'timezones': ['America/La_Paz'], 'code': 'BO', 'continent': 'South America', 'name': 'Bolivia',
     'capital': 'Sucre'},
    {'timezones': ['America/Nassau'], 'code': 'BS', 'continent': 'North America', 'name': 'Bahamas',
     'capital': 'Nassau'},
    {'timezones': ['Asia/Thimphu'], 'code': 'BT', 'continent': 'Asia', 'name': 'Bhutan', 'capital': 'Thimphu'},
    {'timezones': ['Africa/Gaborone'], 'code': 'BW', 'continent': 'Africa', 'name': 'Botswana', 'capital': 'Gaborone'},
    {'timezones': ['Europe/Minsk'], 'code': 'BY', 'continent': 'Europe', 'name': 'Belarus', 'capital': 'Minsk'},
    {'timezones': ['America/Belize'], 'code': 'BZ', 'continent': 'North America', 'name': 'Belize',
     'capital': 'Belmopan'},
    {'timezones': ['America/St_Johns', 'America/Halifax', 'America/Glace_Bay', 'America/Moncton', 'America/Goose_Bay',
                   'America/Blanc-Sablon', 'America/Montreal', 'America/Toronto', 'America/Nipigon',
                   'America/Thunder_Bay', 'America/Pangnirtung', 'America/Iqaluit', 'America/Atikokan',
                   'America/Rankin_Inlet', 'America/Winnipeg', 'America/Rainy_River', 'America/Cambridge_Bay',
                   'America/Regina', 'America/Swift_Current', 'America/Edmonton', 'America/Yellowknife',
                   'America/Inuvik', 'America/Dawson_Creek', 'America/Vancouver', 'America/Whitehorse',
                   'America/Dawson'], 'code': 'CA', 'continent': 'North America', 'name': 'Canada',
     'capital': 'Ottawa'},
    {'timezones': ['Africa/Kinshasa', 'Africa/Lubumbashi'], 'code': 'CD', 'continent': 'Africa',
     'name': 'Democratic Republic of the Congo', 'capital': 'Kinshasa'},
    {'timezones': ['Africa/Brazzaville'], 'code': 'CG', 'continent': 'Africa', 'name': 'Republic of the Congo',
     'capital': 'Brazzaville'},

    {'timezones': ['America/Santiago', 'Pacific/Easter'], 'code': 'CL', 'continent': 'South America', 'name': 'Chile',
     'capital': 'Santiago'},

    {'timezones': ['Asia/Shanghai', 'Asia/Harbin', 'Asia/Chongqing', 'Asia/Urumqi', 'Asia/Kashgar'], 'code': 'CN',
     'continent': 'Asia', 'name': "People's Republic of China", 'capital': 'Beijing'},

    {'timezones': ['America/Havana'], 'code': 'CU', 'continent': 'North America', 'name': 'Cuba', 'capital': 'Havana'},
    {'timezones': ['Atlantic/Cape_Verde'], 'code': 'CV', 'continent': 'Africa', 'name': 'Cape Verde',
     'capital': 'Praia'},
    {'timezones': ['Asia/Nicosia'], 'code': 'CY', 'continent': 'Asia', 'name': 'Cyprus', 'capital': 'Nicosia'},
    {'timezones': ['Europe/Prague'], 'code': 'CZ', 'continent': 'Europe', 'name': 'Czech Republic',
     'capital': 'Prague'},
    {'timezones': ['Europe/Berlin'], 'code': 'DE', 'continent': 'Europe', 'name': 'Germany', 'capital': 'Berlin'},
    {'timezones': ['Africa/Djibouti'], 'code': 'DJ', 'continent': 'Africa', 'name': 'Djibouti',
     'capital': 'Djibouti City'},
    {'timezones': ['Europe/Copenhagen'], 'code': 'DK', 'continent': 'Europe', 'name': 'Denmark',
     'capital': 'Copenhagen'},
    {'timezones': ['America/Dominica'], 'code': 'DM', 'continent': 'North America', 'name': 'Dominica',
     'capital': 'Roseau'},
    {'timezones': ['America/Santo_Domingo'], 'code': 'DO', 'continent': 'North America', 'name': 'Dominican Republic',
     'capital': 'Santo Domingo'},
    {'timezones': ['America/Guayaquil', 'Pacific/Galapagos'], 'code': 'EC', 'continent': 'South America',
     'name': 'Ecuador', 'capital': 'Quito'},
    {'timezones': ['Europe/Tallinn'], 'code': 'EE', 'continent': 'Europe', 'name': 'Estonia', 'capital': 'Tallinn'},
    {'timezones': ['Africa/Cairo'], 'code': 'EG', 'continent': 'Africa', 'name': 'Egypt', 'capital': 'Cairo'},
    {'timezones': ['Africa/Asmera'], 'code': 'ER', 'continent': 'Africa', 'name': 'Eritrea', 'capital': 'Asmara'},
    {'timezones': ['Africa/Addis_Ababa'], 'code': 'ET', 'continent': 'Africa', 'name': 'Ethiopia',
     'capital': 'Addis Ababa'},
    {'timezones': ['Europe/Helsinki'], 'code': 'FI', 'continent': 'Europe', 'name': 'Finland', 'capital': 'Helsinki'},
    {'timezones': ['Pacific/Fiji'], 'code': 'FJ', 'continent': 'Oceania', 'name': 'Fiji', 'capital': 'Suva'},
    {'timezones': ['Europe/Paris'], 'code': 'FR', 'continent': 'Europe', 'name': 'France', 'capital': 'Paris'},
    {'timezones': ['Africa/Libreville'], 'code': 'GA', 'continent': 'Africa', 'name': 'Gabon', 'capital': 'Libreville'},
    {'timezones': ['Asia/Tbilisi'], 'code': 'GE', 'continent': 'Asia', 'name': 'Georgia', 'capital': 'Tbilisi'},
    {'timezones': ['Africa/Accra'], 'code': 'GH', 'continent': 'Africa', 'name': 'Ghana', 'capital': 'Accra'},
    {'timezones': ['Africa/Banjul'], 'code': 'GM', 'continent': 'Africa', 'name': 'The Gambia', 'capital': 'Banjul'},
    {'timezones': ['Africa/Conakry'], 'code': 'GN', 'continent': 'Africa', 'name': 'Guinea', 'capital': 'Conakry'},
    {'timezones': ['Europe/Athens'], 'code': 'GR', 'continent': 'Europe', 'name': 'Greece', 'capital': 'Athens'},
    {'timezones': ['America/Guatemala'], 'code': 'GT', 'continent': 'North America', 'name': 'Guatemala',
     'capital': 'Guatemala City'},
    {'timezones': ['America/Guatemala'], 'code': 'GT', 'continent': 'North America', 'name': 'Haiti',
     'capital': 'Port-au-Prince'},
    {'timezones': ['Africa/Bissau'], 'code': 'GW', 'continent': 'Africa', 'name': 'Guinea-Bissau', 'capital': 'Bissau'},
    {'timezones': ['America/Guyana'], 'code': 'GY', 'continent': 'South America', 'name': 'Guyana',
     'capital': 'Georgetown'},
    {'timezones': ['America/Tegucigalpa'], 'code': 'HN', 'continent': 'North America', 'name': 'Honduras',
     'capital': 'Tegucigalpa'},
    {'timezones': ['Europe/Budapest'], 'code': 'HU', 'continent': 'Europe', 'name': 'Hungary', 'capital': 'Budapest'},
    {'timezones': ['Asia/Jakarta', 'Asia/Pontianak', 'Asia/Makassar', 'Asia/Jayapura'], 'code': 'ID',
     'continent': 'Asia', 'name': 'Indonesia', 'capital': 'Jakarta'},
    {'timezones': ['Europe/Dublin'], 'code': 'IE', 'continent': 'Europe', 'name': 'Republic of Ireland',
     'capital': 'Dublin'},
    {'timezones': ['Asia/Jerusalem'], 'code': 'IL', 'continent': 'Asia', 'name': 'Israel', 'capital': 'Jerusalem'},
    {'timezones': ['Asia/Calcutta'], 'code': 'IN', 'continent': 'Asia', 'name': 'India', 'capital': 'New Delhi'},
    {'timezones': ['Asia/Baghdad'], 'code': 'IQ', 'continent': 'Asia', 'name': 'Iraq', 'capital': 'Baghdad'},
    {'timezones': ['Asia/Tehran'], 'code': 'IR', 'continent': 'Asia', 'name': 'Iran', 'capital': 'Tehran'},

    {'timezones': ['Europe/Rome'], 'code': 'IT', 'continent': 'Europe', 'name': 'Italy', 'capital': 'Rome'},
    {'timezones': ['America/Jamaica'], 'code': 'JM', 'continent': 'North America', 'name': 'Jamaica',
     'capital': 'Kingston'},
    {'timezones': ['Asia/Amman'], 'code': 'JO', 'continent': 'Asia', 'name': 'Jordan', 'capital': 'Amman'},
    {'timezones': ['Asia/Tokyo'], 'code': 'JP', 'continent': 'Asia', 'name': 'Japan', 'capital': 'Tokyo'},
    {'timezones': ['Africa/Nairobi'], 'code': 'KE', 'continent': 'Africa', 'name': 'Kenya', 'capital': 'Nairobi'},
    {'timezones': ['Asia/Bishkek'], 'code': 'KG', 'continent': 'Asia', 'name': 'Kyrgyzstan', 'capital': 'Bishkek'},
    {'timezones': ['Pacific/Tarawa', 'Pacific/Enderbury', 'Pacific/Kiritimati'], 'code': 'KI', 'continent': 'Oceania',
     'name': 'Kiribati', 'capital': 'Tarawa'},
    {'timezones': ['Asia/Pyongyang'], 'code': 'KP', 'continent': 'Asia', 'name': 'North Korea', 'capital': 'Pyongyang'},
    {'timezones': ['Asia/Seoul'], 'code': 'KR', 'continent': 'Asia', 'name': 'South Korea', 'capital': 'Seoul'},
    {'timezones': ['Asia/Kuwait'], 'code': 'KW', 'continent': 'Asia', 'name': 'Kuwait', 'capital': 'Kuwait City'},
    {'timezones': ['Asia/Beirut'], 'code': 'LB', 'continent': 'Asia', 'name': 'Lebanon', 'capital': 'Beirut'},
    {'timezones': ['Europe/Vaduz'], 'code': 'LI', 'continent': 'Europe', 'name': 'Liechtenstein', 'capital': 'Vaduz'},
    {'timezones': ['Africa/Monrovia'], 'code': 'LR', 'continent': 'Africa', 'name': 'Liberia', 'capital': 'Monrovia'},
    {'timezones': ['Africa/Maseru'], 'code': 'LS', 'continent': 'Africa', 'name': 'Lesotho', 'capital': 'Maseru'},
    {'timezones': ['Europe/Vilnius'], 'code': 'LT', 'continent': 'Europe', 'name': 'Lithuania', 'capital': 'Vilnius'},
    {'timezones': ['Europe/Luxembourg'], 'code': 'LU', 'continent': 'Europe', 'name': 'Luxembourg',
     'capital': 'Luxembourg City'},
    {'timezones': ['Europe/Riga'], 'code': 'LV', 'continent': 'Europe', 'name': 'Latvia', 'capital': 'Riga'},
    {'timezones': ['Africa/Tripoli'], 'code': 'LY', 'continent': 'Africa', 'name': 'Libya', 'capital': 'Tripoli'},
    {'timezones': ['Indian/Antananarivo'], 'code': 'MG', 'continent': 'Africa', 'name': 'Madagascar',
     'capital': 'Antananarivo'},
    {'timezones': ['Pacific/Majuro', 'Pacific/Kwajalein'], 'code': 'MH', 'continent': 'Oceania',
     'name': 'Marshall Islands', 'capital': 'Majuro'},
    {'timezones': ['Europe/Skopje'], 'code': 'MK', 'continent': 'Europe', 'name': 'Macedonia', 'capital': 'Skopje'},
    {'timezones': ['Africa/Bamako'], 'code': 'ML', 'continent': 'Africa', 'name': 'Mali', 'capital': 'Bamako'},
    {'timezones': ['Asia/Rangoon'], 'code': 'MM', 'continent': 'Asia', 'name': 'Myanmar', 'capital': 'Naypyidaw'},
    {'timezones': ['Asia/Ulaanbaatar', 'Asia/Hovd', 'Asia/Choibalsan'], 'code': 'MN', 'continent': 'Asia',
     'name': 'Mongolia', 'capital': 'Ulaanbaatar'},
    {'timezones': ['Africa/Nouakchott'], 'code': 'MR', 'continent': 'Africa', 'name': 'Mauritania',
     'capital': 'Nouakchott'},
    {'timezones': ['Europe/Malta'], 'code': 'MT', 'continent': 'Europe', 'name': 'Malta', 'capital': 'Valletta'},
    {'timezones': ['Indian/Mauritius'], 'code': 'MU', 'continent': 'Africa', 'name': 'Mauritius',
     'capital': 'Port Louis'},

    {'timezones': ['Africa/Blantyre'], 'code': 'MW', 'continent': 'Africa', 'name': 'Malawi', 'capital': 'Lilongwe'},
    {'timezones': ['America/Mexico_City', 'America/Cancun', 'America/Merida', 'America/Monterrey', 'America/Mazatlan',
                   'America/Chihuahua', 'America/Hermosillo', 'America/Tijuana'], 'code': 'MX',
     'continent': 'North America', 'name': 'Mexico', 'capital': 'Mexico City'},
    {'timezones': ['Asia/Kuala_Lumpur', 'Asia/Kuching'], 'code': 'MY', 'continent': 'Asia', 'name': 'Malaysia',
     'capital': 'Kuala Lumpur'},
    {'timezones': ['Africa/Maputo'], 'code': 'MZ', 'continent': 'Africa', 'name': 'Mozambique', 'capital': 'Maputo'},
    {'timezones': ['Africa/Windhoek'], 'code': 'NA', 'continent': 'Africa', 'name': 'Namibia', 'capital': 'Windhoek'},
    {'timezones': ['Africa/Niamey'], 'code': 'NE', 'continent': 'Africa', 'name': 'Niger', 'capital': 'Niamey'},
    {'timezones': ['Africa/Lagos'], 'code': 'NG', 'continent': 'Africa', 'name': 'Nigeria', 'capital': 'Abuja'},
    {'timezones': ['America/Managua'], 'code': 'NI', 'continent': 'North America', 'name': 'Nicaragua',
     'capital': 'Managua'},
    {'timezones': ['Europe/Amsterdam'], 'code': 'NL', 'continent': 'Europe', 'name': 'Kingdom of the Netherlands',
     'capital': 'Amsterdam'},
    {'timezones': ['Europe/Oslo'], 'code': 'NO', 'continent': 'Europe', 'name': 'Norway', 'capital': 'Oslo'},
    {'timezones': ['Asia/Katmandu'], 'code': 'NP', 'continent': 'Asia', 'name': 'Nepal', 'capital': 'Kathmandu'},
    {'timezones': ['Pacific/Nauru'], 'code': 'NR', 'continent': 'Oceania', 'name': 'Nauru', 'capital': 'Yaren'},
    {'timezones': ['Pacific/Auckland', 'Pacific/Chatham'], 'code': 'NZ', 'continent': 'Oceania', 'name': 'New Zealand',
     'capital': 'Wellington'},
    {'timezones': ['Asia/Muscat'], 'code': 'OM', 'continent': 'Asia', 'name': 'Oman', 'capital': 'Muscat'},
    {'timezones': ['America/Panama'], 'code': 'PA', 'continent': 'North America', 'name': 'Panama',
     'capital': 'Panama City'},
    {'timezones': ['America/Lima'], 'code': 'PE', 'continent': 'South America', 'name': 'Peru', 'capital': 'Lima'},
    {'timezones': ['Pacific/Port_Moresby'], 'code': 'PG', 'continent': 'Oceania', 'name': 'Papua New Guinea',
     'capital': 'Port Moresby'},
    {'timezones': ['Asia/Manila'], 'code': 'PH', 'continent': 'Asia', 'name': 'Philippines', 'capital': 'Manila'},
    {'timezones': ['Asia/Karachi'], 'code': 'PK', 'continent': 'Asia', 'name': 'Pakistan', 'capital': 'Islamabad'},
    {'timezones': ['Europe/Warsaw'], 'code': 'PL', 'continent': 'Europe', 'name': 'Poland', 'capital': 'Warsaw'},
    {'timezones': ['Europe/Lisbon', 'Atlantic/Madeira', 'Atlantic/Azores'], 'code': 'PT', 'continent': 'Europe',
     'name': 'Portugal', 'capital': 'Lisbon'},
    {'timezones': ['Pacific/Palau'], 'code': 'PW', 'continent': 'Oceania', 'name': 'Palau', 'capital': 'Ngerulmud'},

    {'timezones': ['Asia/Qatar'], 'code': 'QA', 'continent': 'Asia', 'name': 'Qatar', 'capital': 'Doha'},
    {'timezones': ['Europe/Bucharest'], 'code': 'RO', 'continent': 'Europe', 'name': 'Romania', 'capital': 'Bucharest'},
    {'timezones': ['Europe/Kaliningrad', 'Europe/Moscow', 'Europe/Volgograd', 'Europe/Samara', 'Asia/Yekaterinburg',
                   'Asia/Omsk', 'Asia/Novosibirsk', 'Asia/Krasnoyarsk', 'Asia/Irkutsk', 'Asia/Yakutsk',
                   'Asia/Vladivostok', 'Asia/Sakhalin', 'Asia/Magadan', 'Asia/Kamchatka', 'Asia/Anadyr'], 'code': 'RU',
     'continent': 'Europe', 'name': 'Russia', 'capital': 'Moscow'},
    {'timezones': ['Africa/Kigali'], 'code': 'RW', 'continent': 'Africa', 'name': 'Rwanda', 'capital': 'Kigali'},
    {'timezones': ['Asia/Riyadh'], 'code': 'SA', 'continent': 'Asia', 'name': 'Saudi Arabia', 'capital': 'Riyadh'},
    {'timezones': ['Pacific/Guadalcanal'], 'code': 'SB', 'continent': 'Oceania', 'name': 'Solomon Islands',
     'capital': 'Honiara'},
    {'timezones': ['Indian/Mahe'], 'code': 'SC', 'continent': 'Africa', 'name': 'Seychelles', 'capital': 'Victoria'},
    {'timezones': ['Africa/Khartoum'], 'code': 'SD', 'continent': 'Africa', 'name': 'Sudan', 'capital': 'Khartoum'},
    {'timezones': ['Europe/Stockholm'], 'code': 'SE', 'continent': 'Europe', 'name': 'Sweden', 'capital': 'Stockholm'},
    {'timezones': ['Asia/Singapore'], 'code': 'SG', 'continent': 'Asia', 'name': 'Singapore', 'capital': 'Singapore'},
    {'timezones': ['Europe/Ljubljana'], 'code': 'SI', 'continent': 'Europe', 'name': 'Slovenia',
     'capital': 'Ljubljana'},
    {'timezones': ['Europe/Bratislava'], 'code': 'SK', 'continent': 'Europe', 'name': 'Slovakia',
     'capital': 'Bratislava'},
    {'timezones': ['Africa/Freetown'], 'code': 'SL', 'continent': 'Africa', 'name': 'Sierra Leone',
     'capital': 'Freetown'},
    {'timezones': ['Europe/San_Marino'], 'code': 'SM', 'continent': 'Europe', 'name': 'San Marino',
     'capital': 'San Marino'},
    {'timezones': ['Africa/Dakar'], 'code': 'SN', 'continent': 'Africa', 'name': 'Senegal', 'capital': 'Dakar'},
    {'timezones': ['Africa/Mogadishu'], 'code': 'SO', 'continent': 'Africa', 'name': 'Somalia', 'capital': 'Mogadishu'},
    {'timezones': ['America/Paramaribo'], 'code': 'SR', 'continent': 'South America', 'name': 'Suriname',
     'capital': 'Paramaribo'},

    {'timezones': ['Asia/Damascus'], 'code': 'SY', 'continent': 'Asia', 'name': 'Syria', 'capital': 'Damascus'},

    {'timezones': ['Asia/Bangkok'], 'code': 'TH', 'continent': 'Asia', 'name': 'Thailand', 'capital': 'Bangkok'},
    {'timezones': ['Asia/Dushanbe'], 'code': 'TJ', 'continent': 'Asia', 'name': 'Tajikistan', 'capital': 'Dushanbe'},
    {'timezones': ['Asia/Ashgabat'], 'code': 'TM', 'continent': 'Asia', 'name': 'Turkmenistan', 'capital': 'Ashgabat'},
    {'timezones': ['Africa/Tunis'], 'code': 'TN', 'continent': 'Africa', 'name': 'Tunisia', 'capital': 'Tunis'},

    {'timezones': ['Europe/Istanbul'], 'code': 'TR', 'continent': 'Asia', 'name': 'Turkey', 'capital': 'Ankara'},
    {'timezones': ['America/Port_of_Spain'], 'code': 'TT', 'continent': 'North America', 'name': 'Trinidad and Tobago',
     'capital': 'Port of Spain'},
    {'timezones': ['Pacific/Funafuti'], 'code': 'TV', 'continent': 'Oceania', 'name': 'Tuvalu', 'capital': 'Funafuti'},
    {'timezones': ['Africa/Dar_es_Salaam'], 'code': 'TZ', 'continent': 'Africa', 'name': 'Tanzania',
     'capital': 'Dodoma'},
    {'timezones': ['Europe/Kiev', 'Europe/Uzhgorod', 'Europe/Zaporozhye', 'Europe/Simferopol'], 'code': 'UA',
     'continent': 'Europe', 'name': 'Ukraine', 'capital': 'Kiev'},
    {'timezones': ['Africa/Kampala'], 'code': 'UG', 'continent': 'Africa', 'name': 'Uganda', 'capital': 'Kampala'},
    {'timezones': ['America/New_York', 'America/Detroit', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello',
                   'America/Indiana/Indianapolis', 'America/Indiana/Marengo', 'America/Indiana/Knox',
                   'America/Indiana/Vevay', 'America/Chicago', 'America/Indiana/Vincennes',
                   'America/Indiana/Petersburg', 'America/Menominee', 'America/North_Dakota/Center',
                   'America/North_Dakota/New_Salem', 'America/Denver', 'America/Boise', 'America/Shiprock',
                   'America/Phoenix', 'America/Los_Angeles', 'America/Anchorage', 'America/Juneau', 'America/Yakutat',
                   'America/Nome', 'America/Adak', 'Pacific/Honolulu'], 'code': 'US', 'continent': 'North America',
     'name': 'United States', 'capital': 'Washington, D.C.'},
    {'timezones': ['America/Montevideo'], 'code': 'UY', 'continent': 'South America', 'name': 'Uruguay',
     'capital': 'Montevideo'},
    {'timezones': ['Asia/Samarkand', 'Asia/Tashkent'], 'code': 'UZ', 'continent': 'Asia', 'name': 'Uzbekistan',
     'capital': 'Tashkent'},
    {'timezones': ['Europe/Vatican'], 'code': 'VA', 'continent': 'Europe', 'name': 'Vatican City',
     'capital': 'Vatican City'},
    {'timezones': ['America/Caracas'], 'code': 'VE', 'continent': 'South America', 'name': 'Venezuela',
     'capital': 'Caracas'},
    {'timezones': ['Asia/Saigon'], 'code': 'VN', 'continent': 'Asia', 'name': 'Vietnam', 'capital': 'Hanoi'},
    {'timezones': ['Pacific/Efate'], 'code': 'VU', 'continent': 'Oceania', 'name': 'Vanuatu', 'capital': 'Port Vila'},
    {'timezones': ['Asia/Aden'], 'code': 'YE', 'continent': 'Asia', 'name': 'Yemen', 'capital': "Sana'a"},
    {'timezones': ['Africa/Lusaka'], 'code': 'ZM', 'continent': 'Africa', 'name': 'Zambia', 'capital': 'Lusaka'},
    {'timezones': ['Africa/Harare'], 'code': 'ZW', 'continent': 'Africa', 'name': 'Zimbabwe', 'capital': 'Harare'},
    {'timezones': ['Africa/Algiers'], 'code': 'DZ', 'continent': 'Africa', 'name': 'Algeria', 'capital': 'Algiers'},
    {'timezones': ['Europe/Sarajevo'], 'code': 'BA', 'continent': 'Europe', 'name': 'Bosnia and Herzegovina',
     'capital': 'Sarajevo'},
    {'timezones': ['Asia/Phnom_Penh'], 'code': 'KH', 'continent': 'Asia', 'name': 'Cambodia', 'capital': 'Phnom Penh'},
    {'timezones': ['Africa/Bangui'], 'code': 'CF', 'continent': 'Africa', 'name': 'Central African Republic',
     'capital': 'Bangui'},
    {'timezones': ['Africa/Ndjamena'], 'code': 'TD', 'continent': 'Africa', 'name': 'Chad', 'capital': "N'Djamena"},
    {'timezones': ['Indian/Comoro'], 'code': 'KM', 'continent': 'Africa', 'name': 'Comoros', 'capital': 'Moroni'},
    {'timezones': ['Europe/Zagreb'], 'code': 'HR', 'continent': 'Europe', 'name': 'Croatia', 'capital': 'Zagreb'},
    {'timezones': ['Asia/Dili'], 'code': 'TL', 'continent': 'Asia', 'name': 'East Timor', 'capital': 'Dili'},
    {'timezones': ['America/El_Salvador'], 'code': 'SV', 'continent': 'North America', 'name': 'El Salvador',
     'capital': 'San Salvador'},
    {'timezones': ['Africa/Malabo'], 'code': 'GQ', 'continent': 'Africa', 'name': 'Equatorial Guinea',
     'capital': 'Malabo'},
    {'timezones': ['America/Grenada'], 'code': 'GD', 'continent': 'North America', 'name': 'Grenada',
     'capital': "St. George's"},
    {'timezones': ['Asia/Almaty', 'Asia/Qyzylorda', 'Asia/Aqtobe', 'Asia/Aqtau', 'Asia/Oral'], 'code': 'KZ',
     'continent': 'Asia', 'name': 'Kazakhstan', 'capital': 'Astana'},
    {'timezones': ['Asia/Vientiane'], 'code': 'LA', 'continent': 'Asia', 'name': 'Laos', 'capital': 'Vientiane'},
    {'timezones': ['Pacific/Truk', 'Pacific/Ponape', 'Pacific/Kosrae'], 'code': 'FM', 'continent': 'Oceania',
     'name': 'Federated States of Micronesia', 'capital': 'Palikir'},

    {'timezones': ['Europe/Monaco'], 'code': 'MC', 'continent': 'Europe', 'name': 'Monaco', 'capital': 'Monaco'},
    {'timezones': ['Europe/Podgorica'], 'code': 'ME', 'continent': 'Europe', 'name': 'Montenegro',
     'capital': 'Podgorica'},
    {'timezones': ['Africa/Casablanca'], 'code': 'MA', 'continent': 'Africa', 'name': 'Morocco', 'capital': 'Rabat'},
    {'timezones': ['America/St_Kitts'], 'code': 'KN', 'continent': 'North America', 'name': 'Saint Kitts and Nevis',
     'capital': 'Basseterre'},
    {'timezones': ['America/St_Lucia'], 'code': 'LC', 'continent': 'North America', 'name': 'Saint Lucia',
     'capital': 'Castries'},
    {'timezones': ['America/St_Vincent'], 'code': 'VC', 'continent': 'North America',
     'name': 'Saint Vincent and the Grenadines', 'capital': 'Kingstown'},
    {'timezones': ['Pacific/Apia'], 'code': 'WS', 'continent': 'Oceania', 'name': 'Samoa', 'capital': 'Apia'},
    {'timezones': ['Europe/Belgrade'], 'code': 'RS', 'continent': 'Europe', 'name': 'Serbia', 'capital': 'Belgrade'},
    {'timezones': ['Africa/Johannesburg'], 'code': 'ZA', 'continent': 'Africa', 'name': 'South Africa',
     'capital': 'Pretoria'},
    {'timezones': ['Europe/Madrid', 'Africa/Ceuta', 'Atlantic/Canary'], 'code': 'ES', 'continent': 'Europe',
     'name': 'Spain', 'capital': 'Madrid'},
    {'timezones': ['Asia/Colombo'], 'code': 'LK', 'continent': 'Asia', 'name': 'Sri Lanka',
     'capital': 'Sri Jayewardenepura Kotte'},
    {'timezones': ['Africa/Mbabane'], 'code': 'SZ', 'continent': 'Africa', 'name': 'Swaziland', 'capital': 'Mbabane'},
    {'timezones': ['Europe/Zurich'], 'code': 'CH', 'continent': 'Europe', 'name': 'Switzerland', 'capital': 'Bern'},
    {'timezones': ['Asia/Dubai'], 'code': 'AE', 'continent': 'Asia', 'name': 'United Arab Emirates',
     'capital': 'Abu Dhabi'},
    {'timezones': ['Europe/London'], 'code': 'GB', 'continent': 'Europe', 'name': 'United Kingdom',
     'capital': 'London'}, ]

items = [
    ["sword", 10, "weapon", "A sharp blade for close combat."],
    ["bow", 8, "weapon", "A ranged weapon for attacking from a distance."],
    ["potion", 0, "consumable", "A drink that restores health."],
    ["armor", 0, "armor", "Protective gear that reduces damage taken."],
    ["gold", 0, "currency", "A valuable metal used for trading."],
    ["dagger", 6, "weapon", "A small blade for quick attacks."],
    ["staff", 7, "weapon", "A long stick used for casting spells."],
    ["wand", 5, "weapon", "A short stick used for casting spells."],
    ["crossbow", 9, "weapon", "A ranged weapon that fires bolts."],
    ["axe", 11, "weapon", "A heavy blade for chopping."],
    ["mace", 12, "weapon", "A heavy club with a spiked head."],
    ["spear", 8, "weapon", "A long pole with a sharp tip."],
    ["halberd", 10, "weapon", "A pole weapon with an axe and spearhead."],
    ["shield", 0, "armor", "A protective barrier that blocks attacks."],
    ["helmet", 0, "armor", "A protective headgear that reduces damage taken."],
    ["boots", 0, "armor", "Protective footwear that reduces damage taken."],
    ["gloves", 0, "armor", "Protective hand-wear that reduces damage taken."],
    ["ring", 0, "accessory", "A piece of jewelry that grants magical powers."],
    ["amulet", 0, "accessory", "A necklace that grants magical powers."],
    ["bracers", 0, "armor", "Protective arm-wear that reduces damage taken."],
    ["greaves", 0, "armor", "Protective leg-wear that reduces damage taken."],
    ["cuirass", 0, "armor", "A breastplate that reduces damage taken."],
    ["pizza-variant italia", 0, "consumable", "a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough topped with tomatoes, cheese, and often various other ingredients (such as various types of sausage, anchovies, mushrooms, onions, olives, vegetables, meat, ham, etc.), which is then baked at a high temperature, traditionally in a wood-fired oven. "],
    ["water", 0, "consumable", "A liquid that restores health and energy."],
    ["torch", 0, "tool", "A portable light source."],
    ["rope", 0, "tool", "A long, strong cord used for climbing and binding."],
    ["grappling hook", 0, "tool", "A hook attached to a rope used for climbing."],
    ["lockpick", 0, "tool", "A tool used for picking locks."],
    ["key", 0, "tool", "A small metal object used for unlocking doors."],
    ["map", 0, "tool", "A diagram that shows the layout of an area."],
    ["compass", 0, "tool", "A device that shows the cardinal directions."],
    ["flint and steel", 0, "tool", "A tool used for starting fires."],
    ["fishing rod", 0, "tool", "A long, flexible rod used for catching fish."],
    ["tent", 0, "tool", "A portable shelter used for camping."],
    ["bedroll", 0, "tool", "A portable bed used for camping."],
    ["backpack", 0, "container", "A bag used for carrying items."],
    ["satchel", 0, "container", "A small bag used for carrying items."],
    ["pouch", 0, "container", "A small bag used for carrying small items."],
    ["quiver", 0, "container", "A container used for holding arrows or bolts."],
    ["scroll", 0, "tool", "A piece of parchment with a spell written on it."],
    ["book", 0, "tool", "A bound collection of pages with information written on them."],
    ["ink and quill", 0, "tool", "A tool used for writing."],
    ["herbs", 0, "consumable", "A plant used for its medicinal properties."],
    ["samosa", 0, "consumable", "A yummy food used for its Ambrosial properties."],
    ["gemstone", 0, "currency", "A valuable stone used for trading."],
    ["Pizza", 0, "consumable", "A savory dish of Italian origin, consisting of a usually round, flattened base of leavened wheat-based dough topped with tomatoes, cheese, and various other ingredients."],
    ["Sushi", 0, "consumable", "A Japanese dish of prepared vinegared rice, usually with some sugar and salt, accompanying a variety of ingredients, such as seafood, vegetables, and occasionally tropical fruits."],
    ["Tacos", 0,  "consumable", "A traditional Mexican dish consisting of a corn or wheat tortilla folded or rolled around a filling."],
    ["Burgers", 0,  "consumable", "A sandwich consisting of one or more cooked patties of ground meat, usually beef, placed inside a sliced bread roll or bun."],
    ["Pasta", 0,  "consumable", "A type of Italian noodle dish typically made from an unleavened dough of wheat flour mixed with water or eggs and formed into sheets or various shapes, then cooked by boiling or baking."],
    ["Ramen", 0,  "consumable", "A Japanese dish with Chinese origins, consisting of Chinese wheat noodles served in a meat or fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, and green onions."],
    ["Curry", 0,  "consumable", "A variety of dishes originating in the Indian subcontinent that use a complex combination of spices or herbs, usually including ground turmeric, cumin, coriander, ginger, and fresh or dried chilies."],
    ["Steak", 0,  "consumable", "A cut of meat, usually beef, sliced perpendicular to the muscle fibers, potentially including a bone."],
    ["Fried Rice", 0,  "consumable", "A dish of cooked rice that has been stir-fried in a wok or a frying pan and is usually mixed with other ingredients such as eggs, vegetables, seafood, or meat."],
    ["Chow Mein", 0,  "consumable", "A Chinese stir-fried noodle dish which is popular in many countries."],
    ["Biryani", 0,  "consumable", "A mixed rice dish with its origins in the Indian subcontinent. It is made with Indian spices, rice, and meat, and sometimes, in addition, eggs and/or vegetables such as potatoes."],
    ["Lasagna", 0,  "consumable", "A wide, flat pasta noodle, usually baked in layers in the oven with a filling of either meat, cheese, or vegetables."],
    ["Fajitas", 0,  "consumable", "A Tex-Mex dish consisting of grilled meat usually served as a taco on a flour or corn tortilla."],
    ["Goulash", 0, "consumable", "A stew of meat and vegetables, seasoned with paprika and other spices."],
    ["Stroganoff", 0,  "consumable", "A Russian dish of sautéed pieces of beef served in a sauce with smetana."],
    ["Paella", 0,  "consumable", "A Valencian rice dish that has ancient roots but its modern form originated in the mid-19th century in the area around the Albufera lagoon on the east coast of Spain adjacent to the city of Valencia."],
    ["Ratatouille", 0,  "consumable", "A French Provençal stewed vegetable dish, originating in Nice, and sometimes referred to as ratatouille niçoise."],
    ["Chili con Carne", 0,  "consumable", "A spicy stew containing chili peppers, meat, and often tomatoes and beans."],
    ["Jambalaya", 0,  "consumable", "A Louisiana-origin dish of Spanish and French influence, consisting mainly of meat and vegetables mixed with rice."],
    ["Gumbo", 0,  "consumable", '''A stew that originated in southern Louisiana during the 18th century. It consists primarily of a strongly-flavored stock, meat or shellfish, a thickener, and the Cajun/Creole "holy trinity" ― celery, bell peppers, and onions.'''],
    ["Pierogi", 0,  "consumable", "A type of filled dumpling, originating from Central and Eastern Europe(mainly poland)."],
    ["Borscht", 0,  "consumable", '''A sour soup common in Eastern Europe and Northern Asia. In English, the word "borscht" is most often associated with the soup's variant of Ukrainian origin, made with beetroots as one of the main ingredients.'''],
    ["Schnitzel", 0,  "consumable", "A thin slice of meat fried in fat. The meat is usually thinned by pounding with a meat tenderizer. Most commonly, the meats are breaded before frying."],
    ["Kebab", 0, "consumable", "A dish of pieces of meat, fish, or vegetables roasted or grilled on"]
    ]




class UtilsGaurav:  # creates class Utils_Gaurav
    def __init__(self, ai, scratch):  # tells the program what to do when the Utils_Gaurav class has been initialised
        if ai == True:
            self.Ai_Enabled = True
            self.r = sr.Recognizer()  # initialises the Recogniser Function (no arguments) in the sr(Speech Recognition) Class
            self.Gaurav = ChatBot(
                "Gaurav")  # initialises the ChatBot Class with 1 parameter/argument name which is set to the string Gaurav and  this is set to the variable assigned Gaurav
            self.trainer = ChatterBotCorpusTrainer(
                self.Gaurav)  # initialises the ChatterBotCorpustrainer Class with 1 parameter/argument -the Chatbot class- this is set to the variable assigned Trainer
            self.trainer.train(
                "chatterbot.corpus.english")  # trainer(a variable) which has an attribute of train which is a function in the ChatterBotCorpusTrainer Class with 1 argument type string
        else:
            self.Ai_Enabled = False
        if scratch == True:
            self.Scratch_Enabled = True
            import scratchconnect  # gives access to the Scratch Connect module
            self.user = scratchconnect.ScratchConnect("__BIT__",
                                                      "Lakshya123@")  # logs into a Scratch User to Give us access to all Scratch Features
            self.project = self.user.connect_project(project_id=778517371)  # Accesses the Project using project id
            self.Variables = self.project.connect_cloud_variables()  # Connect the project's cloud variables
            self.Event = self.Variables.create_cloud_event()  # Create a cloud  event
            self.communications_line = "Cloud"  # Sets the Communications line with the Project To the string Cloud we need an identical Cloud Variable in Scratch to interact and share data
        else:
            self.Scratch_Enabled = False
        print("---GAURAV'S UTILS FUNCTION---")  # prints a string

    def Roll(self, d):
        import random
        return random.randint(1, int(d))

    def SpeakText(self,
                  command):  # a function/Subroutine named SpeakText with 1 argument command the def keyword is used to define the function
        if self.Ai_Enabled == True:
            engine = pyttsx3.init()  # initialises the init()subroutine and sets it to the variable assigned as engine
            engine.say(
                command)  # engine(a variable) which has an attribute of say which is a function in the pyttsx3 module with 1 argument type string command
            engine.runAndWait()  # engine(a variable) which has an attribute of runAndWait which is a function in the pyttsx3 module with 1 argument self
        else:
            raise IOError("Function_Disabled")

    def find(self, word,
             var):  # a function/Subroutine named find  def keyword is used to define the function with 2 parameters word and var standing for keyword and data set
        WORD = ""  # initialises a variable assigned WORD indicates that it is going to be a string
        ret = 0  # initialises a variable assigned ret indicates that it is going to be an integer
        new_word = ""  # initialises a variable assigned new_word indicates that it is going to be a string
        speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
        for i in range(len(var)):  # a for loop that is going to repeat length of var
            item = var[i]  # sets variable assigned item to the  i character of var
            WORD = WORD + item  # sets variable assigned WORD to itself + variable item
            if item == "'":  # an if statement that activates the tabbed code under if the statement is true
                if speech_marks == 1:  # an if statement that activates the tabbed code under if the statement is true
                    if WORD == "'" + word + "'":  # an if statement that activates the tabbed code under if the statement is true
                        speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
                        WORD = ""  # initialises a variable assigned WORD indicates that it is going to be a string
                        ret = 1  # sets variable assigned ret to  1
                    elif ret == 1:  # else if statement
                        for i2 in range(len(WORD)):  # a for loop that is going to repeat length of WORD
                            letter = WORD[i2]  # sets variable assigned letter to the  i character of WORD
                            if letter != "'":  # an if statement that activates the tabbed code under if the statement is true
                                new_word = new_word + letter  # sets variable assigned new_word to itself + variable letter
                        return new_word  # returns the variable assigned new_word
                    else:  # else statement that only gets activated if the other statements are false
                        speech_marks = 0  # initialises a variable assigned speech_marks indicates that it is going to be an integer
                        WORD = ""  # initialises a variable assigned WORD indicates that it is going to be a string
                else:  # else statement that only gets activated if the other statements are false
                    speech_marks = 1  # sets the variable assigned speech_marks to integer value 1

    def receive(self):  # a function/Subroutine named SpeakText  def keyword is used to define the function
        if self.Ai_Enabled == True:
            try:  # Tries the following code check for errors that might be raised
                with sr.Microphone() as source2:  # calls the Microphone() function /attribute as keyword used to give a temporary name for example source2
                    self.r.adjust_for_ambient_noise(source2,
                                                    duration=0.2)  # calls the adjust_for_ambient_noise function with 2 arguments microphone source ,duration
                    audio2 = self.r.listen(
                        source2)  # calls the listen function with 1 argument microphone also known as source2 and is set to the variable assigned audio2
                    MyText = self.r.recognize_google(
                        audio2)  # calls the recognize_google function with one argument which is the sound input this function coverts the sound input into text using the Google Ai model and sets the variable assigned Mytext
                    MyText = MyText.lower()  # first the Mytext has an  attribute lower which makes it lower case, and then it is set to the variable assigned Mytext
                    return MyText  # returns the Mytext Variable

            except sr.RequestError:  # the except keyword tells the computer how to handle a RequestError only used with the try function
                return "NO INPUT"  # Returns a string called NO INPUT

            except sr.UnknownValueError:  # the except keyword tells the computer how to handle a UnknownValueError only used with the try function
                return "NO INPUT"  # Returns a string called NO INPUT
        else:
            raise IOError("Function_Disabled")

    def INPUT(self, prompt, types, data):  # Input function with  4 parameters prompt,type and data + self
        if types == "Basic":  # an if statement that activates the tabbed code under if the statement is true
            return input(str(prompt))  # returns the answer to the question
        elif types == "MO":  # Multiple Options (else if statement)
                print(str(prompt))  # prints the answer to the question
                for i in range(len(list(data))):  # a for loop that is going to repeat length of data
                    print(f"OPTION {i + 1}: {data[i]}")  # prints the Options of the question so user can answer
                out = input("PICK OPTION: ")  # returns the answer to the question
                if out != "":
                    if out > str(len(data)):
                        print("NOT an option")
                        return self.INPUT(prompt=prompt, types=types, data=data)
                    else:
                        return out
                else:
                    print("cannot except keys given ")
                    return self.INPUT(prompt=prompt, types=types, data=data)

    def Print(self, txt, delay):  # Print function with 3 parameters txt,delay and self
        for char in txt:  # a for loop that is going to repeat length of txt
            print(char, end='', flush=True)  # prints each character on same line
            time.sleep(delay)  # uses the time function to delay in seconds
        print("", end="\n", flush=False)

    def ChatBot(self, txt):  # Chatbot function with 2 parameters txt and self
        if self.Ai_Enabled == True:
            return self.Gaurav.get_response(
                txt)  # returns response to the txt input using the get response attribute of Gaurav
        else:
            raise IOError("Function_Disabled")

    def Stream_chatbot_out_to_Scratch(self):  # A function that allows for chatbots in scratch
        if self.Ai_Enabled == True and self.Scratch_Enabled == True:
            @self.Event.on("connect")  # triggers the code under if true
            def connect():  # function called connect
                print("Connection established starting data sharing")  # prints to terminal a string
                encoded_string = self.Variables.encode("Server Listening...")  # Encode a string
                self.Variables.set_cloud_variable(variable_name=self.communications_line,
                                                  value=encoded_string)  # Sends Encoded String

            @self.Event.on("set")  # triggers the code under if true
            def set(data):  # function called set with 1 argument data
                if str(data[
                           "user"]) != "__BIT__":  # an if statement that activates the tabbed code under if the statement is true
                    encoded = data["value"]  # sets variable assigned encoded to value in the data dictionary
                    message = self.Variables.decode(
                        encoded)  # sets variable assigned message to the decoded data sent from Scratch
                    function = self.find("function",
                                         message)  # sets variable assigned function to the return value form the find function with string "function" and message given as parameter
                    if function == "stream":  # an if statement that activates the tabbed code under if the statement is true
                        new_data = self.find("DATA",
                                             message)  # sets variable assigned new_data to the return value form the find string "DATA" and message given as parameter
                        encoded_string = self.Variables.encode(self.Gaurav.get_response(new_data))  # Encode a string
                        self.Variables.set_cloud_variable(variable_name=self.communications_line,
                                                          value=encoded_string)  # sets cloud Variable to encoded_String
                    else:  # else statement that only gets activated if the other statements are false
                        print("NOT STREAM")  # prints string Not Streaming
                        encoded_string = self.Variables.encode("NOT Correct format")  # Encode a string
                        self.Variables.set_cloud_variable(variable_name=self.communications_line,
                                                          value=encoded_string)  # sets cloud Variable to encoded_String

                self.Event.start(update_time=0.01)  # starts the cloud event
        else:
            raise IOError("Function_Disabled Hint:Maybe Forgot to Set Ai to True")

    def Gaurav(self):  # function named Gaurav with 1 parameter self
        if self.Ai_Enabled == True:
            while True:  # while statement set default to true meaning it will run infinite times
                txt = str(
                    self.receive())  # sets the variable assigned txt to the string from return value from the receive() function
                if txt != "bye":  # an if statement that activates the tabbed code under if the statement is true
                    self.SpeakText(
                        self.Gaurav.get_response(txt))  # speaks the response from Gaurav the Chatbot given some text
                elif txt == "what is your name":  # else if statement
                    self.SpeakText("Gaurav")  # speaks name Gaurav
                else:  # else statement that only gets activated if the other statements are false
                    self.SpeakText("Bye")  # speaks text bye
                    break  # breaks the infinite loop
        else:
            raise IOError("Function_Disabled")

    def Money_to_Coins(self, *money):
        total_amount = 0
        for i in money:
            total_amount = total_amount + int(i)
        T1 = total_amount // 20
        total_amount = total_amount - (20 * T1)
        T2 = total_amount // 10
        total_amount = total_amount - (10 * T2)
        T3 = total_amount // 5
        total_amount = total_amount - (5 * T3)
        T4 = total_amount // 2
        total_amount = total_amount - (2 * T4)
        return {"20": T1,
                "10": T2,
                "5": T3,
                "2": T4,
                "1": total_amount}

    def Country_Guessing_game(self):
        selected_countries = []
        selected_capitals = []
        for i in range(3):
            index = randint(0, len(countries) - 1)
            selected_countries.append(countries[index]["name"])
            selected_capitals.append(countries[index]["capital"])
        idx = randint(0, 2)
        while True:
            answer = self.INPUT(f"What is {selected_countries[idx]}'s capital ?: ", "MO", selected_capitals)
            try:
                int(answer)
            except ValueError:
                if answer == "Exit" or "exit":
                    break
            if selected_capitals[int(answer) - 1] == selected_capitals[idx]:
                self.Print("Well Done that is correct!", 0.2)
                break

            else:
                self.Print("Incorrect :( try again !!", 0.2)

        replay = self.INPUT("Do you want to play again?: ", "MO", ["Yes", "No"])
        if replay == "1":
            self.Country_Guessing_game()

    def Text_based_Games(self):
        pass


class Player(UtilsGaurav):

    def __init__(self):
        super().__init__(ai=False, scratch=False)
        self.Headshot_Multi = 1.75
        self.Torso_Multi = 1.2
        self.Legs_Multi = 0.7
        self.strength = self.Roll(20)
        self.Agility = self.Roll(20)
        self.intelligence = self.Roll(20)
        self.wisdom = self.Roll(20)
        self.charisma = self.Roll(20)
        self.HP = 100
        self.Inventory = []
        self.Item_Type = []
        self.Item_Damage = []
        self.Item_Description = []
        self.Item_quantity = []
        for item in items:
            for i, data in enumerate(item):
                if i == 0:
                    self.Inventory.append(data)
                    self.Item_quantity.append(2)
                elif i == 1:
                    self.Item_Damage.append(data)
                    self.Item_quantity.append(2)
                elif i == 2:
                    self.Item_Type.append(data)
                    self.Item_quantity.append(2)
                elif i == 3:
                    self.Item_Description.append(data)
                    self.Item_quantity.append(2)
                else:
                    raise IOError("Unknown data")

    def attack(self, attacker_name, attacker_HP):
        Weapons = []
        for item in self.Inventory:
            if self.Item_Type[self.Inventory.index(item)] == "weapon":
                Weapons.append(item)
        option2 = int(self.INPUT("What Weapon do you want to use?", "MO", Weapons))
        idx = self.Inventory.index(Weapons[option2 - 1])
        Weapon_damage = self.Item_Damage[idx]
        Multipliers = [self.Headshot_Multi, self.Torso_Multi, self.Legs_Multi]
        Multi = Multipliers[randint(0, 2)]
        if float(Weapon_damage) * float(Multi) > attacker_HP:
            if Multi == self.Legs_Multi:
                self.Print(f"You use the {Weapons[option2]} and manage to  hit his legs ", 0.2)
                self.Print(f"The {attacker_name} collapsed to the ground, clutching his legs. ", 0.03)
                self.Print(f"The pain was unbearable, like a thousand knives stabbing him at once. ", 0.03)
                self.Print(f"He felt blood gushing from his wounds, soaking his clothes and the dirt beneath him. ",
                           0.03)
                self.Print(f"He tried to scream, but no sound came out. ", 0.03)
                self.Print(f"His vision blurred and he felt dizzy. ", 0.03)
                self.Print(f"He knew he was dying, but he couldn’t accept it. ", 0.03)
                self.Print(f"He had so much to live for, so much to do. ", 0.03)
                self.Print(f"He wanted to see his family again, to tell them he loved them. ", 0.03)
                self.Print(f"He wanted to fight for his cause, to make a difference in the world. ", 0.03)
                self.Print(
                    f"He wanted to live. But all he could do was lie there, helpless and hopeless, waiting for the end.",
                    0.03)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "legs"}
            elif Multi == self.Torso_Multi:
                self.Print(f"You use the {Weapons[option2]} and manage to  hit his body ", 0.2)
                self.Print(
                    "He felt a sudden impact in his chest, followed by a sharp pain that spread throughout his body. ",
                    0.03)
                self.Print("He gasped for air, but it felt like he was breathing fire. ", 0.03)
                self.Print("He looked down and saw blood pouring from his shirt. He realized he had been Hit.", 0.03)
                self.Print(
                    "he staggered backwards, trying to reach for his secret weapon. But his arms were numb and heavy. ",
                    0.03)
                self.Print(
                    "He fell to his knees, feeling weak and cold. He heard voices around him, shouting and shooting. ",
                    0.03)
                self.Print("But they sounded distant and muffled. He closed his eyes, hoping it was all a nightmare. ",
                           0.03)
                self.Print("But he knew it was real. He knew he was dying. And he was afraid.", 0.03)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "torso"}
            elif Multi == self.Headshot_Multi:
                self.Print(f"You use the {Weapons[option2]} and manage to  hit his head ", 0.2)
                self.Print("He heard a loud bang, and then everything went black. ", 0.03)
                self.Print("He felt a brief flash of pain in his head, like a hammer smashing his skull. ", 0.03)
                self.Print("He didn’t have time to react or think. He was dead before he hit the ground.", 0.03)
                self.Print(" His brain was shattered by the bullet that pierced his temple. ", 0.03)
                self.Print("His life was over in an instant. He had no memories, no regrets, no dreams.", 0.03)
                self.Print(" He had nothing. He was nothing.", 0.03)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "head"}
            else:
                raise IOError("UNKNOWN body HIT")
        else:
            self.Print(f"The {attacker_name} has taken {float(Weapon_damage) * float(Multi)} damage", 0.2)
            return {"status": "engaged", "HP": attacker_HP - (float(Weapon_damage) * float(Multi)),
                    "Total_Damage": (float(Weapon_damage) * float(Multi)), "Weapon_Damage": Weapon_damage,
                    "Multi": Multi, "loc": "body"}

    def Declare_truce(self, attacker_Emotional_attachment, attacker_name, attacker_HP):
        Probability_of_acceptance = (1 * (attacker_Emotional_attachment / 20))
        if Probability_of_acceptance == 1:
            print(f"The {attacker_name} Looks Down at you and admires your attachment to his kind")
            print(f"I guess i will find food some where else ")
            print(f"The {attacker_name} walks away util you cannot see him ")
            print(f"Your Intelligence{self.intelligence} increase by one ")
            self.intelligence += 1
            return {"status": "Declared Truce", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}
        else:
            print("Ha Ha Ha did you really think your sadness will affect me !!")
            print("DIEEE DIEEE!!")
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}

    def Run(self, attacker_strengh, attacker_name, attacker_HP):
        if attacker_strengh > self.strength:
            Metres = self.strength * self.Agility
            self.Print(
                f"you Run for your life as the {attacker_name} chases you sadly after {Metres} metres your energy depletes and the {attacker_name} is behind you ",
                0.01)
            self.Print(f"Ha HA HA where will you go now ?? says the {attacker_name}", 0.01)
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}
        else:
            self.Print(f"You manage to escape the {attacker_name}", 0.01)
            return {"status": "escaped", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0,
                    "loc": "body"}

    def consume(self):
        consumable = []
        options = []
        for item in self.Inventory:
            if self.Item_Type[self.Inventory.index(item)] == "consumable":
                consumable.append(item)
        for item in consumable:
            if self.Item_quantity[consumable.index(item)] >= 1:
                options.append(item)
        option2 = int(self.INPUT("What food do you want to consume?", "MO", options))
        self.Print(f"Did u know that the {consumable[option2-1]} is {self.Item_Description[self.Inventory.index(consumable[option2-1])]} ?", 0.02)
        self.Item_quantity[self.Inventory.index(consumable[option2-1])] -= 1
        self.HP += 10
        if self.Item_quantity[self.Inventory.index(consumable[option2-1])] <= 1:
            self.Print(f"you have {self.Item_quantity[self.Inventory.index(consumable[option2-1])]} {consumable[option2 - 1]} left .", 0.02)
        else:
            self.Print(f"you have {self.Item_quantity[self.Inventory.index(consumable[option2-1])]} {consumable[option2-1]}s left .", 0.02)

    def Wear(self):
        wearable = []
        options = []
        for item in self.Inventory:
            if self.Item_Type[self.Inventory.index(item)] == "armor":
                wearable.append(item)
        for item in wearable:
            if self.Item_quantity[wearable.index(item)] >= 1:
                options.append(item)
        option2 = int(self.INPUT("What items do you want to equip?", "MO", options))
        self.Print(f"Did u know that the {wearable[option2 - 1]} is {self.Item_Description[self.Inventory.index(wearable[option2 - 1])]} ?", 0.02)

    def options(self, attacker_name, attacker_HP, attacker_strengh, attacker_Emotional_attachment):
        option = self.INPUT("What do you want to do?", "MO", ["RUN", "FIGHT", "Declare Truce", "Consume", "wear"])
        if option == "1":
            return self.Run(attacker_strengh, attacker_name, attacker_HP)
        elif option == "2":
            return self.attack(attacker_name=attacker_name, attacker_HP=attacker_HP)
        elif option == "3":
            return self.Declare_truce(attacker_HP=attacker_HP, attacker_name=attacker_name, attacker_Emotional_attachment=attacker_Emotional_attachment)
        elif option == "4":
            self.consume()
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0, "loc": "NONE"}
        elif option == "5":
            self.Wear()
            return {"status": "engaged", "HP": attacker_HP, "Total_Damage": 0, "Weapon_Damage": 0, "Multi": 0, "loc": "NONE"}

        else:
            raise IOError("Not an Option")


class Enemy(UtilsGaurav):

    def __init__(self, _name, HP, EM, Strength):
        super().__init__(ai=False, scratch=False)
        self.HP = HP
        self.Headshot_Multi = 1.7
        self.Torso_Multi = 1.2
        self.Legs_Multi = 0.7
        self.name = _name
        self.Emotional_Attachment = EM
        self.Strength = Strength
        self.Inventory = ["dagger", "sword", "wand"]
        self.Item_Damage = ["10", "35", "60", "0"]

    def process(self, player_HP):
        option2 = randint(1, len(self.Inventory) - 1)
        idx = self.Inventory.index(self.Inventory[option2])
        Weapon_damage = self.Item_Damage[idx]
        Multipliers = [self.Headshot_Multi, self.Torso_Multi, self.Legs_Multi]
        Multi = Multipliers[randint(0, 2)]
        if float(Weapon_damage) * float(Multi) > player_HP:
            if Multi == self.Legs_Multi:
                self.Print(f"The {self.name} uses the {self.Inventory[option2]} and manage to  hit your legs ", 0.2)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "legs"}

            elif Multi == self.Torso_Multi:
                self.Print(f"The {self.name} uses the {self.Inventory[option2]} and manage to  hit your body ", 0.2)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "torso"}

            elif Multi == self.Headshot_Multi:
                self.Print(f"The {self.name} uses the {self.Inventory[option2]} and manage to  hit your head ", 0.2)
                return {"status": "dead", "HP": 0, "Total_Damage": (float(Weapon_damage) * float(Multi)),
                        "Weapon_Damage": Weapon_damage, "Multi": Multi, "loc": "head"}

            else:
                raise IOError("UNKNOWN body HIT")
        else:
            self.Print(f"YOU have taken {float(Weapon_damage) * float(Multi)} damage", 0.2)
            return {"status": "engaged", "HP": player_HP - (float(Weapon_damage) * float(Multi)),
                    "Total_Damage": (float(Weapon_damage) * float(Multi)), "Weapon_Damage": Weapon_damage,
                    "Multi": Multi, "loc": "body"}
