from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from config import YAFA_CHANNEL, YAFA_NAME, CHANNEL_SUDO
from YukkiMusic import app


@app.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not YAFA_CHANNEL:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(CHANNEL_SUDO, msg.from_user.id)
        except UserNotParticipant:
            if YAFA_CHANNEL.isalpha():
                link = u"{YAFA_CHANNEL}"
            else:
                chat_info = await bot.get_chat(CHANNEL_SUDO)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"ЁЯЪзя╕Щ╪╣╪░╪▒╪з┘Л╪М ╪╣┘Д┘К┘Г ╪з┘Д╪г╪┤╪к╪▒╪з┘Г ┘Б┘К ┘В┘Ж╪з╪й ╪з┘Д╪и┘И╪к ╪г┘И┘Д╪з┘Л\nтЪая╕Пя╕Щ╪з╪┤╪к╪▒┘Г ╪л┘Е ╪г╪▒╪│┘Д : /start",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"{YAFA_NAME}", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"╪╣┘Д┘К┘Г ╪▒┘Б╪╣ ╪з┘Д╪и┘И╪к ╪в╪п┘Е┘Ж ┘Б┘К ╪з┘Д┘В┘Ж╪з╪й ╪г┘И┘Д╪з┘Л ╪Я╪Я : {YAFA_CHANNEL} !")
