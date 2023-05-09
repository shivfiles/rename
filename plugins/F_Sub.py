from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import FORCE_SUB

async def not_subscribed(_, client, message):
    if not client.force_channel:
        return False
    try:             
        user = await client.get_chat_member(client.force_channel, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[ InlineKeyboardButton(text="GET ACCESS", url=f"https://t.me/Shreeshiva323") ]]
    text = "Hey..😍. You Need to Buy Premium On this Bot use Me...!"
    try:
        user = await client.get_chat_member(client.force_channel, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="Hey..😍. You Need to get access from @Shreeshiva323 use Me...!")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



