import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ChatMemberStatus

# ប្រើប្រាស់ Token ផ្ទាល់ (ឬប្រើ Environment Variable បើអ្នកបានកំណត់)
API_TOKEN = '8595295507:AAEVTSWfekhWbExH9odVbNHVF3KTeGYviSw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def filter_messages(message: types.Message):
    # បើជាសារក្នុង Group
    if message.chat.type in ["group", "supergroup"]:
        try:
            # ពិនិត្យសិទ្ធិអ្នកផ្ញើ
            member = await bot.get_chat_member(message.chat.id, message.from_user.id)
            
            # បើមិនមែន Admin ឬ Owner ទេ ទើបឆែកលុប
            if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
                has_link = message.entities and any(e.type in ["url", "text_link"] for e in message.entities)
                is_forwarded = message.forward_origin is not None
                
                if has_link or is_forwarded:
                    await message.delete()
                    logging.info(f"Deleted message from {message.from_user.id}")
        except Exception as e:
            logging.error(f"Error checking member: {e}")

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.info("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
