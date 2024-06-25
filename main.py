import asyncio
import json
import logging
from core.client import create_client
from core.trigger.chat import send_message_to_chat
from core.trigger.comments import send_comment
from core.messages.messages import get_random_message
from core.database.database import create_db

async def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        await create_db()

        chats = config["main"]["chats"]
        channels = config["main"]["channels"]

        clients = []
        for account in config:
            if account.startswith("account"):
                api_id = config[account]["api_id"]
                api_hash = config[account]["api_hash"]
                phone_number = config[account]["phone"]
                delay = config[account]["delay"]

                client = await create_client(f"./clients/{account}", api_id, api_hash, phone_number)
                clients.append((client, delay))

        while True:
            for client, delay in clients:
                message = await get_random_message()
                if chats:
                    for chat in chats:
                        await send_message_to_chat(client, chat, message)
                else:
                    logging.info("No chats found in the config. Skipping sending messages to chats.")
                if channels:
                    for channel in channels:
                        await send_comment(client, channel, message)
                else:
                    logging.info("No channels found in the config. Skipping sending comments to channels.")
                await asyncio.sleep(delay)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())