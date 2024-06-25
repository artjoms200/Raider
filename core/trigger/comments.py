from telethon.sync import TelegramClient

async def split_string(input_string):
    channel_username, message_id = input_string.split(':')
    message_id = int(message_id)
    return channel_username, message_id

async def send_comment(client: TelegramClient, entity: str, comment_text: str):
    try:
        channel_username, message_id = await split_string(entity)
        channel_entity = await client.get_entity(channel_username)
        message = await client.get_messages(channel_entity, ids=message_id)

        await client.send_message(
            channel_entity,
            message=comment_text, 
            reply_to=message.id
        )
        print(f"Комментарий отправлен к сообщению с ID: {message_id} в канале {channel_username}")
    except ValueError as e:
        print(f"Сообщение с ID {message_id} не найдено в канале {channel_username}. Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка при отправке комментария: {e}")