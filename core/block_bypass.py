import random

async def get_device_model():
    list = [
        'iPhone 12', 
        'iPhone 12 Pro', 
        'iPhone 12 Pro Max', 
        'iPhone 13', 
        'iPhone 13 Pro', 
        'iPhone 13 Pro Max', 
        'iPhone 14', 
        'iPhone 15', 
        'iPhone 11', 
        'iPhone 11 Pro', 
        'iPhone 11 Pro Max', 
        'iPhone XS', 
        'iPhone XS Max', 
        'iPhone XR', 
        'iPhone X', 
        'iPhone 8', 
        'iPhone 8 Plus', 
        'iPhone 7', 
        'iPhone 7 Plus', 
        'iPhone 6s', 
        'iPhone 6s Plus'
    ]
    return random.choice(list)

async def get_system_version():
    list = [
        'IOS 15.5.1', 
        'IOS 15.5', 
        'IOS 15.4.1', 
        'IOS 15.4', 
        'IOS 15.3.1', 
        'IOS 15.3', 
        'IOS 15.2.1', 
        'IOS 15.2', 
        'IOS 15.1.1', 
        'IOS 15.1'
    ]
    return random.choice(list)

async def get_app_version():
    list = [
        '10.12.0',
        '10.11.0',
        '10.10.0',
        '10.9.0',
        '10.8.0',
        '10.7.0',
        '10.6.0',
        '10.5.0',
        '10.4.0',
        '10.3.0',
        '10.2.0',
        '10.1.0'
    ]
    return random.choice(list)

async def get_system_lang_code():
    list = [
        'en-US',
        'ru-RU',
        'uk-UA',
        'de-DE',
        'fr-FR',
        'es-ES',
        'it-IT',
        'pt-PT',
        'tr-TR',
        'pl-PL',
        'ua-UA',
        'sk-SK',
        'cs-CZ',
        'da-DK',
        'he-IL',
        'ja-JP',
        'ko-KR',
        'zh-CN',
    ]
    #return random.choice(list)
    return 'lv-LV' #for me it profiter

async def get_lang_code():
    list = [
        'en',
        'ru',
        'uk',
        'de',
        'fr',
        'es',
        'it',
        'pt',
        'tr',
        'pl',
        'ua',
        'sk',
        'cs',
        'da',
        'he',
        'ja',
        'ko',
        'zh',
    ]
    #return random.choice(list)
    return 'lv' #for me it profiter
    
