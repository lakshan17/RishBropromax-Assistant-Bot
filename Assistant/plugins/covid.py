import requests, json
from Assistant import Assistant
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


#Api responses
response_API = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
data = json.loads(response_API.text)
local_new_cases     = str(data['data']['local_new_cases'])
update_date_time    = str(data['data']['update_date_time'])
local_new_cases     = str(data['data']['local_new_cases'])
local_active_cases  = str(data['data']['local_active_cases'])
local_total_cases   = str(data['data']['local_total_cases'])
local_deaths        = str(data['data']['local_deaths'])
local_recovered     = str(data['data']['local_recovered'])
local_total_number_of_individuals_in_hospitals = str(data['data']['local_total_number_of_individuals_in_hospitals'])
global_new_cases    = str(data['data']['global_new_cases'])
global_total_cases  = str(data['data']['global_total_cases'])
local_new_deaths    = str(data['data']['local_new_deaths'])
global_deaths       = str(data['data']['global_deaths'])
global_new_deaths   = str(data['data']['global_deaths'])
global_recovered    = str(data['data']['global_recovered'])

COVIDLOCAL = f"""
**Covid Condition of SriLanka**
┌ **New Patients** - `{local_new_cases}`
├ **New Deaths** - `{local_new_deaths}`
├ **Total Patients** - `{local_total_cases}`
├ **Currently Cured** - `{local_recovered}`
├ **Still Being treated** - `{local_active_cases}`
└ **Total deaths** - `{local_deaths}`
🔄Updated on {update_date_time}
"""

COVIDGLOBAL = f"""
**Global Covid Condition **
┌ **New Patients ** - `{global_new_cases}`
├ **New Deaths ** - `{global_new_deaths}`
├ **Total Patients ** - `{global_total_cases}`
├ **Currently Cured ** - `{global_recovered}`
└ **Total deaths ** - `{global_deaths}`
🔄Updated on {update_date_time}
"""

REPLY_MARKUPL = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Global", callback_data="globalcovide"),
                    InlineKeyboardButton(f"Local" , callback_data="localcovide") 
                ],
                [
                    InlineKeyboardButton(" Bot ", url="https://t.me/Imrishmika_Bot")
                ],

            ]
        )

REPLY_MARKUPG = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f"Global", callback_data="globalcovide"),
                    InlineKeyboardButton(f"Local" , callback_data="localcovide") 
                ],
                [
                    InlineKeyboardButton(" Bot ", url="https://t.me/ImRishmika_Bot")
                ],

            ]
        )

@bot.on_callback_query(filters.regex("localcovide"))
async def covidl(_, query: CallbackQuery):
    await query.edit_message_text(COVIDLOCAL,
        reply_markup=REPLY_MARKUPL,
     disable_web_page_preview=True
    )

@bot.on_callback_query(filters.regex("globalcovide"))
async def covidg(_, query: CallbackQuery):
    await query.edit_message_text(COVIDGLOBAL,
        reply_markup=REPLY_MARKUPG,
     disable_web_page_preview=True
    )

  # ---------command---------
@bot.on_message(filters.regex("covid"))
async def covid(_, message):
    await message.reply_photo(photo="https://telegra.ph/file/53f7b5666c2eb6a302e8f.jpg", 
                              caption=COVIDLOCAL,
                              reply_markup=REPLY_MARKUPL,
    )


#https://telegra.ph/file/53f7b5666c2eb6a302e8f.jpg
