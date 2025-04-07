import random

cookies = {
    '__lhash_': '7aea1b856996795f7bee932f71664d60',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_CHAT_VERSION': '6.6.0',
    'SENTRY_TRANSACTIONS_RATE': '0.1',
    'SENTRY_REPLAYS_SESSIONS_RATE': '0.01',
    'SENTRY_REPLAYS_ERRORS_RATE': '0.01',
    'SENTRY_ERRORS_RATE': '0.1',
    'MVID_FILTER_CODES': 'true',
    'MVID_SUGGEST_DIGINETICA': 'true',
    'MVID_MEDIA_STORIES': 'true',
    'MVID_SERVICES': '111',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_GTM_ENABLED': '011',
    'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
    'MVID_WEB_SBP': 'true',
    'MVID_CREDIT_SERVICES': 'true',
    'MVID_TYP_CHAT': 'true',
    'MVID_SP': 'true',
    'MVID_CREDIT_DIGITAL': 'true',
    'MVID_CASCADE_CMN': 'true',
    'MVID_EMPLOYEE_DISCOUNT': 'true',
    'MVID_AB_UPSALE': 'true',
    'MVID_AB_PERSONAL_RECOMMENDS': 'true',
    'MVID_SERVICE_AVLB': 'true',
    'MVID_NEW_CHAT_PDP': 'true',
    'MVID_TYP_ACCESSORIES_ORDER_SET': 'true',
    'MVID_GROUP_BY_QUALITY': 'true',
    'MVID_DISPLAY_PERS_DISCOUNT': 'true',
    'MVID_AB_PERSONAL_RECOMMENDS_SRP': 'true',
    'MVID_DIGINETICA_ENABLED': 'true',
    'MVID_ACCESSORIES_ORDER_SET_VERSION': '2',
    'MVID_BYPASS_FC': 'true',
    'MVID_IMG_RESIZE': 'true',
    'MVID_NEW_GET_SHOPPING_CART_SHORT': 'true',
    'MVID_WEB_QR': 'true',
    'MVID_SRP_DIGINETICA_ENABLED': 'true',
    'MVID_ALLPROMOTIONS_NEW': 'true',
    'MVID_SORM_INTEGRATION': 'true',
    'MVID_QUASAR_CUSTOMER': 'true',
    'MVID_QUASAR_CAPTCHA': 'true',
    'MVID_QUASAR_UPDATE_CUSTOMER': 'true',
    'MVID_ACTIVATE_BONUSES_MCOMBO': 'true',
    'MVID_DISABLEDITEM_PRICE': 'true',
    'MVID_RECOMENDATION_SET_ALGORITHM': '0',
    'MVID_DEVICE_UUID': 'adc0ab31-784f-4307-ae09-596b554b3b8f',
    '_userGUID': '0:m975bxsx:3tLmdopiAtB53JZY7IHJYFP8nNbBxGew',
    'mindboxDeviceUUID': 'f91cb93b-118a-4aa1-83b7-8915a11a63ae',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22f91cb93b-118a-4aa1-83b7-8915a11a63ae%22%7D',
    '_userGUID': '0:m975bxsx:3tLmdopiAtB53JZY7IHJYFP8nNbBxGew',
    '_ym_uid': '1744034871374953538',
    '_ym_d': '1744034871',
    '_ym_isad': '1',
    '_ga': 'GA1.1.1761856223.1744034871',
    'tmr_lvid': 'd2d72708cd4b4d187f1cab0a3bff87ee',
    'tmr_lvidTS': '1744034873619',
    'advcake_track_id': '8f30152a-32f6-ce7f-dee1-b80d0829fe37',
    'advcake_session_id': '8c86c09b-c288-fc1e-e110-1c42a8d86fa5',
    'uxs_uid': 'b2ddc040-13b9-11f0-842c-af18c0b64758',
    'afUserId': '4df81e0e-aa48-48bf-872d-eeca7055e0d1-p',
    'AF_SYNC': '1744034874117',
    'domain_sid': 'rNR8sHOsWfS1veI5mVlKh%3A1744034874970',
    'flocktory-uuid': '55e8bdf1-4272-47e4-8e02-5ab424cd1547-2',
    '_sp_ses.d61c': '*',
    '_dvs': '0:m97bpq95:9YrB1hrBSvpKC_tudkxf1lNAEsWdS_4c',
    'MVID_GEOLOCATION_NEEDED': 'false',
    '_ym_visorc': 'w',
    'MVID_GUEST_ID': '24538421527',
    'MVID_VIEWED_PRODUCTS': '',
    'wurfl_device_id': 'generic_web_browser',
    'MVID_YANDEX_WIDGET': 'true',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'searchType2': '3',
    'COMPARISON_INDICATOR': 'false',
    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
    'deviceType': 'desktop',
    'MVID_ENVCLOUD': 'prod2',
    'JSESSIONID': 'JTgmn0LL0rlTGvxvdYGCQP612rQrl2pQdpBBTS2yvGwCd2gTMyj1!-365775078',
    'flacktory': 'no',
    'BIGipServeratg-ps-prod_tcp80': '2936331274.20480.0000',
    'bIPs': '672961728',
    'MVID_GTM_BROWSER_THEME': '1',
    'BIGipServeratg-ps-prod_tcp80_clone': '2936331274.20480.0000',
    'adid': '174404711407417',
    'digi_uc': '|v:174404:20087845:400071374:400336589|c:174404:20082732:400350412:400391824',
    '__hash_': '5cba8bfc1a4d15b6a78b51b8dd73c455',
    'dSesn': '0cbdbde1-c6ce-d97f-582f-59c6208800b0',
    'CACHE_INDICATOR': 'true',
    'MVID_CITY_ID': 'CityCZ_975',
    'MVID_REGION_ID': '1',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_REGION_SHOP': 'S002',
    'MVID_CITY_CHANGED': 'true',
    'MVID_KLADR_ID': '7700000000000',
    '_sp_id.d61c': '293f9364-7362-40df-8e3d-f68e38983067.1744034871.2.1744048195.1744035170.5c434bd2-7254-4fa1-a2c7-9c0'
                   'a4e0cd23a.c525280d-32fa-42fd-8292-653e0ea66803.a2e152db-e618-4781-a4c7-5fbde35e4026.1744045590407.4'
                   '06',
    'advcake_track_url': '%3D20250113icNedADNLeY79H45kGeclpdd9vCeMSpTJt4O3Q8Nq%2FLl3FXD1oIVylFVVnkrzCA%2BR%2BWDkbss5msR'
                         'eaX4tW5ylDoEwZIzuWfNzFnuOn1Ddc90C%2FwLwzoHf6Yg0CGSwd1nFX5upM0foeo1PxgctpSAd7EXgPWdhYDuNTIMjVf'
                         'UxcGoPMtDTsgUcM%2F883AGh%2BDuG9jFb1ySP0toJf%2BrPSad59NMVWZ3tk5U3UVKhzhRi1B%2BwvrN1Ogo4WIUs7jN'
                         '%2FqrxK22oKSSwgWdvRNrgzc%2BV4AxQghloFYbl%2FIwa7roLoU9f2ZLz3Ryaf3rjpZSSIfODJWr2UILFlXXvnZI6C%2'
                         'BQL5qy1huzBYRlhEq7cSr2RBX7jLotUNcR4Zx8HhiBtsEjAy7dQMIvSs6lplsY%2B3%2BB8SjZevzln4Rhah6VK6gpllg'
                         'YzZosTqES%2BXfdiCBIVvIu%2BPBtBaWznDTPeOud%2BuG7qzGFejtCxCk%2BGzlkexYL3lek2JUmTWMYfxgjqDoztQio'
                         'ZZjkFsZ9G%2FBaZ5lZLVe0kPPC2cXmbLjpThiPU5Aon2IAEaKFnGMwOcCxJXcbPB%2BANSvc33WZ6dt8qOei7TxA06ymT'
                         'ewiMjZr023r2hkDvjXMynaW6YVgdrhpeMrWw7aZh17Mj7fhVWKPcC4tw7M5qRI38kMVoUGzzoF3nslP4IwuKTQcOXP6X4'
                         'UM%3D',
    'tmr_detect': '0%7C1744048197701',
    'gsscgib-w-mvideo': 'S4OKHm+vxIjMm2RD5e1DTyuEsgzaFl22B4tTBG1gdlG+6ZwotLFtYlpLyZEOIWFmTTjiS9SjbY3RYa0r9nAp0pLogEKkia'
                        'Kbh4xpi2tg+gSXoUjVgC1mKT6yn/lbqNrtj4+dguzhZcwNnarVWhzSP4upJT213zKTEWwWTa0JXe/J4limajO+sHV3CeDM'
                        'vyjRoMnDnTTAYXtPA4CbgFD6B7TqYOr9ZoUuZ3MLaYjFtb+e2A3ruNQLEbJh0H2np4iCfmQbWGaP',
    'gsscgib-w-mvideo': 'S4OKHm+vxIjMm2RD5e1DTyuEsgzaFl22B4tTBG1gdlG+6ZwotLFtYlpLyZEOIWFmTTjiS9SjbY3RYa0r9nAp0pLogEKkia'
                        'Kbh4xpi2tg+gSXoUjVgC1mKT6yn/lbqNrtj4+dguzhZcwNnarVWhzSP4upJT213zKTEWwWTa0JXe/J4limajO+sHV3CeDM'
                        'vyjRoMnDnTTAYXtPA4CbgFD6B7TqYOr9ZoUuZ3MLaYjFtb+e2A3ruNQLEbJh0H2np4iCfmQbWGaP',
    'fgsscgib-w-mvideo': 'rPqrf61c37f61ee3c4616ff65dda90f0f4bbb7fb',
    'fgsscgib-w-mvideo': 'rPqrf61c37f61ee3c4616ff65dda90f0f4bbb7fb',
    'gsscgib-w-mvideo': 'CvNfXA8QIgmhd0k6/4mIFaf9CYL5tAlepiGqh0zqYWx2RXtA8//lGtlEW90I7whO53zOo3O0lZvsqS40+v8xRque1oNLfZ'
                        'KbwVVl778Xb53k9djcIcEkh2g9VFVAOQq9IVyienlU3CRjC6uBJm5u+ZSv8o1vp5uKJGvvvCSi0x7rIBVkyHm8vd72XM+n'
                        'ousvZXgMS0sDpYroHS1cqkSvBYFjpZp4stqhrffRw5qTvPexFs6wJufbb0TWUh3dYVSQgxubAwxv',
    'cfidsgib-w-mvideo': 'unocVg2LaXYnUWs8FyJjwTNDp1NaGMGgZ03Hg2GKEcyQ51kribtlZ9In1QQsEiwIIEwLeZIGjFQaJUJ83CK/o8eMgOrv8'
                         'R2ER6RZcVMDLeos+h0a+8LEQ827mv/xvxLMn7fdaj6buburZbZIngs+JRv0yaN5xx0k1x3ETH0=',
    '_ga_BNX5WPP3YK': 'GS1.1.1744045590.3.1.1744048447.60.0.0',
    '_ga_CFMZTSS5FM': 'GS1.1.1744045590.3.1.1744048447.0.0.0',
}

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/92.0.4515.159 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/92.0.4515.159 Safari/537.36 OPR/77.0.4054.90'
]

headers = {
    'User-Agent': random.choice(user_agents),
    'accept': 'application/json',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    'baggage': 'sentry-environment=production,sentry-release=release_25_3_3(11110),sentry-public_key=ae7d267743424249bf'
               'eeaa2e347f4260,sentry-trace_id=9e9ddcb80177459d8dc7fe63260ef957,sentry-transaction=%2F**%2F,sentry-samp'
               'led=false,sentry-sample_rand=0.34097381537683025,sentry-sample_rate=0.1',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "YaBrowser";v="25.2", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '9e9ddcb80177459d8dc7fe63260ef957-8f66e70e305dbb89-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0'
                  'YaBrowser/25.2.0.0 Safari/537.36',
    'x-set-application-id': 'bd146e27-d33c-4a9e-bd80-f320af04f2d4',
}

categories = ('10','64','54')

# categories_id = ('10','64','54','8','58','25','28','42','37','4107','4329','4147','47','5427','23','2468','24','19','9',
#                  '1','5487','3787','20','41','25344','50','5','7','55','34','2687','4','3','53','51','31517','29',
#                  '2427','2428','11','2','92','292','8027','7672','9375','34821','4887','5927','35','23226','14',
#                  '26714','8410','4507','36','23497','4327','4330','4927','7950','9491','28153','31713','28151','33737',
#                  '31','31018','30420','32328','56','31034','35284','2287','12','26087','59','25841','27763','17',
#                  '32156','6247','32','6327','1461','36077')

# problem_categories:
# '58' - аксессуары для смартфонов > 10000 единиц