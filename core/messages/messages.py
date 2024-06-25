import random

async def get_random_message():
    with open('./core/messages/messages.txt', 'r', encoding='utf-8') as file:
        messages = file.readlines()
    return random.choice(messages).strip()
