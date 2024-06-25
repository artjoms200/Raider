from telethon.sync import TelegramClient
from core.block_bypass import *
from .database.database import *
import socks

async def create_client(session_name, api_id, api_hash, phone_number):

    if await check_user_id(api_id):
        session = await get_session(api_id)
        api_id, api_hash, device_model, system_version, app_version, system_lang_code, lang_code, proxy, phone_number = session[:9]

    else:    
        device_model = await get_device_model()
        system_version = await get_system_version()
        app_version = await get_app_version()
        system_lang_code = await get_system_lang_code()
        lang_code = await get_lang_code()

        proxy = input(f'Enter SOCKS5 PROXY for {phone_number} (ip:port:login:password) - ')

        await setup_client(api_id, api_hash, device_model, system_version, app_version, system_lang_code, lang_code, proxy, phone_number)

    proxy_parts = proxy.split(':')
    proxy_ip = proxy_parts[0]
    proxy_port = int(proxy_parts[1])
    proxy_login = proxy_parts[2]
    proxy_password = proxy_parts[3]

    client = TelegramClient(
        session_name, 
        api_id, 
        api_hash, 
        flood_sleep_threshold=60,
        device_model=device_model,
        system_version=system_version, 
        app_version=app_version, 
        system_lang_code=system_lang_code, 
        lang_code=lang_code,
        proxy=(socks.SOCKS5, proxy_ip, proxy_port, True, proxy_login, proxy_password),
    )

    print(f'Starting client {session_name} with phone number {phone_number}')
    await client.start(phone=phone_number)
    return client