from telethon.sync import TelegramClient

async def send_message_to_chat(client: TelegramClient, chat_username: str, message: str):
    try:
        await client.send_message(chat_username, message)
        print(f"Сообщение успешно отправлено в чат с username: {chat_username}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения в чат: {e}")