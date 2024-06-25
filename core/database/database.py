import aiosqlite
import os

async def create_db():
    db_file = './data.db'
    if not os.path.exists(db_file):
        async with aiosqlite.connect(db_file) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    api_id INTEGER,
                    api_hash TEXT,
                    device_model TEXT,
                    system_version TEXT,
                    app_version TEXT,
                    system_lang_code TEXT,
                    lang_code TEXT,
                    proxy TEXT,
                    phone_number TEXT                                                          
                );
            ''')
            await db.commit()

async def setup_client(api_id, api_hash, device_model, system_version, app_version, system_lang_code, lang_code, proxy, phone_number):
    db_file = './data.db'
    async with aiosqlite.connect(db_file) as db:
        await db.execute(
            'INSERT INTO sessions (api_id, api_hash, device_model, system_version, app_version, system_lang_code, lang_code, proxy, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            (
                api_id,
                api_hash,
                device_model,
                system_version,
                app_version,
                system_lang_code, 
                lang_code,
                proxy,
                phone_number
            ),
        )
        await db.commit()

async def check_user_id(api_id):
    db_file = './data.db'
    async with aiosqlite.connect(db_file) as db:
        async with db.execute('SELECT api_id FROM sessions WHERE api_id = ?', (api_id,)) as cursor:
            result = await cursor.fetchone()
            if result is not None:
                return True
            else:
                return False
            
async def get_session(api_id):
    db_file = './data.db'
    async with aiosqlite.connect(db_file) as db:
        async with db.execute('SELECT * FROM sessions WHERE api_id = ?', (api_id,)) as cursor:
            row = await cursor.fetchone()
            return row
  

        
        
