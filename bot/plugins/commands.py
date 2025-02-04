#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@Mv_LinkzZ"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="𝐘𝐨𝐮 𝐦𝐮𝐬𝐭 𝐣𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐨𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 𝐓𝐡𝐢𝐬 𝐛𝐨𝐚𝐭 𝐢𝐬 𝐮𝐧𝐮𝐬𝐚𝐛𝐥𝐞\n<b>ꜱʜᴀʀᴇ ᴀɴᴅ ꜱᴜᴘᴘᴏʀᴛ\n\n<a href='https://t.me/Mv_LinkZZ'>©Mallu Villa</a></b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" Join Channel ", url=f"https://t.me/Mv_LinkzZ")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + """</code>\n━━━━━━━━━━━━━━━━━━━━
<b>💡 ɢʀᴏᴜᴘ
@Mallu_villa

🎯  ᴄʜᴀɴɴᴇʟs
@Mv_LinkzZ</b>""")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'SHARE', url="https://t.me/share/url?url=https://t.me/Mallu_villa"
                                ),
                                InlineKeyboardButton
                                (   
                                    'GROUP', url="https://t.me/Mallu_villa"
                                )      
                                 
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'SHARE', url="https://t.me/share/url?url=https://t.me/film_zone_group"
                                ),
                                InlineKeyboardButton
                                (   
                                    'GROUP', url="https://t.me/Mallu_villa"
                                )      
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Dev', url="https://t.me/MaxxCoderz"
                                ),
                            InlineKeyboardButton
                                (   
                                    'Support', url="https://t.me/CoderzHEX"
                                )      
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('⚠️JOIN', url='https://t.me/Mv_LinkzZ'),
        InlineKeyboardButton('🕵‍♂CREATOR', url='https://t.me/MaxxCoderz')
    ],[
        InlineKeyboardButton('💡HELP', callback_data="help"),
        InlineKeyboardButton('🔐ClOSE', callback_data="close")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('⬇️BACK', callback_data='start'),
        InlineKeyboardButton('📕About', callback_data='about')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('⬇️BACK', callback_data='start'),
        InlineKeyboardButton('🔐CLOSE', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
