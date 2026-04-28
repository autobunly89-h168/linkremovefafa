import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ChatMemberStatus

# ដាក់ Token របស់អ្នកនៅទីនេះ
API_TOKEN = '8595295507:AAEVTSWfekhWbExH9odVbNHVF3KTeGYviSw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def filter_messages(message: types.Message):
    # បញ្ជាក់ពីសិទ្ធិរបស់អ្នកផ្ញើសារ
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    
    # បើមិនមែនជា Admin ឬ Owner
    if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
        
        # ឆែកមើល Link ឬ ការ Forward
        has_link = message.entities and any(e.type in ["url", "text_link"] for e in message.entities)
        is_forwarded = message.forward_origin is not None
        
        if has_link or is_forwarded:
            try:
                await message.delete()
            except Exception as e:
                logging.error(f"Error: {e}")

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    if has_link or is_forwarded:
            try:
                print(f"រកឃើញ Link ពីអ្នកប្រើប្រាស់ ID: {message.from_user.id}") # បន្ថែមជួរនេះដើម្បីមើលក្នុង Terminal
                await message.delete()
                print("លុបសារជោគជ័យ!")
            except Exception as e:
                print(f"លុបមិនកើតដោយសារ៖ {e}")