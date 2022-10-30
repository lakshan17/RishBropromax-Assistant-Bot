import requests
from bot import bot
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import (InlineQuery, InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent,
                            InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery)
from info import START_IMG, START_TEXT, START_BUTTON, HELP_TEXT, HELP_BUTTON, BOTSTATUS_TEXT, BOTSTATUS_BUTTON
from bot.plugins import *

from config import Config
from bot import LOGGER
from bot.helpers.humanbytes import humanbytes
from bot.helpers.database.access_db import db
from bot.helpers.broadcast import broadcast_handler
from bot.helpers.stats import bot_sys_stats
from bot.helpers.database.add_user import AddUserToDatabase
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup

startbtn = InlineKeyboardMarkup(
               [
                [
                    InlineKeyboardButton(text='❤️\u200d🔥About❤️\u200d🔥', url='https://t.me/AboutRishmika')
                ],
                [
                   InlineKeyboardButton(text='◈━━━━━━━━━━━━━━◈', callback_data='stats_callback'),
                ],
                [
                    InlineKeyboardButton(text='🆘Help and commands🆘', callback_data='helpmenu'),
                ],
               ]
)
@bot.on_message(filters.private & filters.command("start"))
async def startmsg(_, message):
    await AddUserToDatabase(_, message
    await bot.send_sticker(message.from_user.id, file_id)
    await message.reply_text(
    text=f"**✨Hello {message.from_user.mention}🙋\n🌺I am The Assistant Bot Of [Rishmika Sandanu](https://t.me/ImRishmika)**.\n\n__💬You Can Contract Him Using This Bot.\n📨Send Your Messages Normally And I Will Forward Them To Him.__", 
    reply_markup=startbtn,
    disable_web_page_preview=True,
    quote=True) 

@bot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def startgmsg(_, message):
    await message.reply_photo(photo="https://telegra.ph/file/d340fbf28f412487c5750.jpg", 
    caption=f"Hey {message.from_user.mention}☄️. \n\nI am the Assistant bot of Sithija.",
    reply_markup = InlineKeyboardMarkup(
                 [
                  [ InlineKeyboardButton(text='Visit PM', url='https://t.me/ImRishmika_Bot') ],
                  [ InlineKeyboardButton(text='◈━━━━━━◈', callback_data='stats_callback') ]
                 ]
))
async def bot_msg_stats():
    stats = f"""
💖Thank you for use my bot
Stay with me forever💖
@ImRishmika_Bot
"""
    return stats

@bot.on_callback_query(filters.regex("stats_callback"))
async def stats_callbacc(_, CallbackQuery):
    text = await bot_msg_stats()
    await bot.answer_callback_query(CallbackQuery.id, text, show_alert=True)
    

@bot.on_message(filters.private & filters.command("help"))
async def helpmsg(_, message):
    await message.reply_photo(photo="https://telegra.ph/file/d340fbf28f412487c5750.jpg", 
    caption=f"""" Hey {message.from_user.mention}☄️
I have some fun and useful tools
So you can get a help about them🚀 """,
   reply_markup=HELPBUTTON,
   disable_web_page_preview=True
   )

@bot.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await bot.answer_callback_query(query.id, text="🆘Help Menu...", show_alert=False)
    await query.edit_message_text(HELP_TEXT,
        reply_markup=HELP_BUTTON,
     disable_web_page_preview=True
    )

@bot.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(
        text=f"**✨Hello {query.from_user.mention}🙋\n🌺I am The Assistant Bot Of [Rishmika Sandanu](https://t.me/ImRishmika)**.\n\n__💬You Can Contract Him Using This Bot.\n📨Send Your Messages Normally And I Will Forward Them To Him.__",
        reply_markup=START_BUTTON,
     disable_web_page_preview=True
    )
    
 # ============stats===================
@bot.on_message(filters.private & filters.incoming & filters.command("status") & filters.user(Config.OWNER))
async def status(bot, update):
    await update.reply_text(
        text=BOTSTATUS_TEXT,
        reply_markup=BOTSTATUS_BUTTON,
        disable_web_page_preview=True
    )

@bot.on_message(filters.private & filters.command("stats") & filters.user(Config.OWNER))
async def show_status_count(_, Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await bot.reply_text(
        text=f"**💽 Tᴏᴛᴇʟ Dɪꜱᴋ Sᴘᴀᴄᴇ:** {total} \n**💿 Uꜱᴇᴅ Sᴘᴀᴄᴇ:** `{used}({disk_usage}%)` \n**📊 Fʀᴇᴇ Sᴘᴀᴄᴇ:** `{free}` \n**Cᴘᴜ Uꜱᴀɢᴇ:** `{cpu_usage}%` \n**Rᴀᴍ Uꜱᴀɢᴇ:** `{ram_usage}%` \n\n**Tᴏᴛᴀʟ Uꜱᴇʀꜱ 👀:** `{total_users}`\n\n**@ImRishmika_Bot🛡**",
        parse_mode="Markdown",
        quote=True
    )      
    
@bot.on_callback_query(filters.regex("stats"))
async def stats_callbacc(_, CallbackQuery):
    text = await bot_sys_stats()
    await bot.answer_callback_query(CallbackQuery.id, text, show_alert=True)  
 # ============stats===================

@bot.on_message(filters.command("bcast") & filters.user(Config.OWNER) & filters.reply)
async def _broadcast(_, bot: Message):
    await broadcast_handler(bot)  
  

#----------------------variables end-----------------------------
@bot.on_callback_query(filters.regex("postcall"))
async def postcallbacc(_, CallbackQuery):
    await bot.answer_callback_query(CallbackQuery.id, text="🔆Shared Via @ImRishmika_Bot ...", show_alert=False)

#========================inline post=============================



bot.start()
LOGGER.info("Sithija's assistant is online")
idle()
