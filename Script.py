class script(object):  
    START_TXT = """<b>✨ Hᴇʟʟᴏ {user}.
Mʏ Nᴀᴍᴇ Is {bot}.
I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇ Fᴏʀ Yᴏᴜ Jᴜsᴛ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Oʀ Sᴇᴀʀᴄʜ Hᴇʀᴇ </b>"""
    
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""

    FILTER_TXT = "Sᴇʟᴇᴄᴛ Wʜɪᴄʜ Oɴᴇ Yᴏᴜ Wᴀɴᴛ...✨"

    PWGEN_TXT = """❖ /genpw - ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀ ʀᴀɴᴅᴏᴍ ᴘᴀꜱꜱᴡᴏʀᴅ"""

    ABOUT_TXT = """<b>╔═══❰ <b>ᴀʙᴏᴜᴛ</b> ❱══════❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼✯ Mʏ Nᴀᴍᴇ: {}
║┃
║┣⪼✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/TGTesla'>𝚃𝙴𝚂𝙻𝙰</a>
║┃
║┣⪼✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</
║┃
║┣⪼✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
║┃
║┣⪼✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
║┃
║┣⪼✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://app.koyeb.com/'>Kᴏʏᴇʙ</a>
║┃
║┣⪼✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v4.7.1 [ Sᴛᴀʙʟᴇ ]
║╰━━━━━━━━━━━━━━━➣
╚═════════════════❍⊱❁۪۪</b>"""

    WALLPAPER_TXT = """<b>ᗯᗩᒪᒪᑭᗩᑭᗴᖇ ᗰOᗪᑌᒪᗴ</b> 
<b>Gɪᴠᴇs Yᴏᴜ ᴀ Wᴀʟʟᴘᴀᴘᴇʀ ᴏʀ Mᴇᴍᴇ</b>

▪︎ /cars - 𝓖𝓲𝓿𝓮𝓼 𝔂𝓸𝓾 𝓪 𝑪𝒂𝒓 𝓦𝓪𝓵𝓵𝓹𝓪𝓹𝓮𝓻
▪︎ /nice - 𝓖𝓲𝓿𝓮𝓼 𝔂𝓸𝓾 𝓪 𝓝𝓲𝓬𝓮 𝓦𝓪𝓵𝓵𝓹𝓪𝓹𝓮𝓻
▪︎ /meme - 𝓖𝓲𝓿𝓮𝓼 𝔂𝓸𝓾 𝓪 𝓜𝓮𝓶𝓮

Wᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs ᴀs ᴡᴇʟʟ

Made With ❤️ BY @StarkBotUpdates""" 

    TRAILER_TXT = """<b>DISCLAIMER</b>
<b>⪼✯<a>Monetary</b>
    Tʜɪs ʙᴏᴛ ɪs ᴀ ғʀᴇᴇ ᴀɴᴅ sᴇʟғ-ᴄᴏᴅᴇᴅ sɪᴅᴇ ᴘʀᴏᴊᴇᴄᴛ ᴀɴᴅ ɪs ɪɴᴅᴇᴘᴇɴᴅᴇɴᴛ ғʀᴏᴍ ᴀɴʏ ᴏᴛʜᴇʀ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ᴅᴇᴠᴇʟᴏᴘᴇʀ.
Iғ ᴀɴʏᴏɴᴇ ᴏғғᴇʀs sᴇʀᴠɪᴄᴇs ʟɪᴋᴇ ᴛʜᴇsᴇ ғᴏʀ ᴍᴏɴᴇʏ ᴘʟᴇᴀsᴇ ᴅᴏ ɴᴏᴛ ᴀᴄᴄᴇᴘᴛ ɪᴛ .
 
<b>⪼✯Legal</b>
     Iғ ʏᴏᴜ ғᴇᴇʟ ᴛʜᴀᴛ ᴛʜɪs ʙᴏᴛ ᴠɪᴏʟᴀᴛᴇs ᴀɴʏ ᴄᴏᴘʏʀɪɢʜᴛs ᴏʀ ᴏᴛʜᴇʀ ʀᴜʟᴇs ᴘʟᴇᴀsᴇ ʀᴇᴘᴏʀᴛ ɪᴛ ᴀᴛ ᴛʜᴇ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ ᴀɴᴅ ᴡᴇ ᴡɪʟʟ ʙᴇ ᴍᴏʀᴇ ᴛʜᴀɴ ʜᴀᴘᴘʏ ᴛᴏ sᴏʟᴠᴇ ᴛʜᴇ ᴘʀᴏʙʟᴇᴍ.
Tʜᴇ ʙᴏᴛ ɪs ᴀʟᴍᴏsᴛ ᴄᴏᴍᴘʟᴇᴛᴇʟʏ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴅʀɪᴠᴇɴ sᴏ ᴛʜᴇ ғɪʟᴇs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ ᴜsᴇʀs ᴏғ ᴛʜᴇ ʙᴏᴛ ᴏʀ ʀᴀɴᴅᴏᴍʟʏ sᴄʀᴀᴘᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟs.
 
<b>⪼✯Note</b>
     Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ɪɴᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ ʀᴇɢᴀʀᴅɪɴɢ ᴛʜᴇ ᴀᴄᴛɪᴠɪᴛɪᴇs ᴏғ ᴛʜᴇ ʙᴏᴛ ᴘʟᴇᴀsᴇ ʟᴇᴛ ᴜs ᴋɴᴏᴡ .</a>

Made With ❤️ BY @StarkBotUpdates"""
    TELEGRAPH_TXT = """<b>🔰 Telegraph Module</b>
<b>Commands and Usage:</b>
❖ /telegraph - upload supported media (within 5MB) to telegraph.

Made With ❤️ BY @StarkBotUpdates"""
    PIN_TXT = """📌 <b>Pin :-</b>

All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!

📚 Admin Commands:

⫸ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

⫸ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message

Made With ❤️ BY @StarkBotUpdates"""
    WHOIS_TXT = """<b>WHO-IS</b> MODULE
Note:- Give a user details

⫸/whois :-give a user full details
⫸/stickerid :- Id of sticker

Made With ❤️ BY @StarkBotUpdates"""
    PASTE_TXT = """<b>PASTY MODULE</b> 
▪︎ Pastes the Given test to PASTY.
▪︎ /paste (your text to be pasted written here)

Made With ❤️ BY @StarkBotUpdates"""      

    PICEDIT_TXT = """ꜱᴇɴᴅ ᴍᴇ ᴀɴ ɪᴍᴀɢᴇ ᴛᴏ ꜱᴇᴇ ᴛʜᴇ ᴍᴀɢɪᴄ"""
    CARBON_TXT = """ ❖ /carbon - Rᴇᴘʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Cᴀʀʙᴏɴᴀᴛᴇᴅ Iᴍᴀɢᴇ"""
    WRITTEN_TXT = """ ❖ /written - Rᴇᴩʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Fɪʟᴇ (ᴜꜱᴇꜰᴜʟʟ ꜰᴏʀ ᴄᴏᴅᴇʀꜱ)"""
    SHARETXT_TXT = """ ❖ /share - Rᴇᴘʟʏ Wɪᴛʜ Tᴇxᴛ Tᴏ Gᴇᴛ Tᴇxᴛ Sʜᴀʀᴀʙʟᴇ Lɪɴᴋ"""
    VIDEODL_TXT = """ ❖ /video [ʟɪɴᴋ] - Tᴏ Dᴏᴡɴʟᴏᴀᴅ Tʜᴇ YᴏᴜTᴜʙᴇ Vɪᴅᴇᴏ"""
    
   
    SOURCE_TXT = """<b>NOTE:</b>
- Source - /repo 

<b>DEVS:</b>
- <a href=https://t.me/TGTesla>𝚃𝙴𝚂𝙻𝙰</a>"""

    FILE_TXT = """<b>➤ Hᴇʟᴘ Fᴏʀ Fɪʟᴇ Sᴛᴏʀᴇ</b>

<i>Bʏ Usɪɴɢ Tʜɪs Mᴏᴅᴜʟᴇ Yᴏᴜ Cᴀɴ Sᴛᴏʀᴇ Fɪʟᴇs Iɴ Mʏ Dᴀᴛᴀʙᴀsᴇ Aɴᴅ I Wɪʟʟ Gɪᴠᴇ Yᴏᴜ A Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ  Tᴏ Aᴄᴄᴇss Tʜᴇ Sᴀᴠᴇᴅ Fɪʟᴇs. Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Fɪʟᴇs Fʀᴏᴍ A Pᴜʙʟɪᴄ Cʜᴀɴɴᴇʟ Sᴇɴᴅ Tʜᴇ Fɪʟᴇ Lɪɴᴋ Oɴʟʏ  Oʀ Yᴏᴜ Wᴀɴᴛ Tᴏ Aᴅᴅ Fɪʟᴇs Fʀᴏᴍ A  Pʀɪᴠᴀᴛᴇ Cʜᴀɴɴᴇʟ Yᴏᴜʀ Mᴜsᴛ Mᴀᴋᴇ Mᴇ Aᴅᴍɪɴ Oɴ Tʜᴇ Cʜᴀɴɴᴇʟ Tᴏ Aᴄᴄᴇss Fɪʟᴇs</i>

<b>⪼ Cᴏᴍᴍᴀɴᴅ & Usᴀɢᴇ</b>
➪ /link › Rᴇᴘʟʏ Tᴏ Aɴʏ Mᴇᴅɪᴀ Tᴏ Gᴇᴛ Tʜᴇ Lɪɴᴋ 
➪ /batch › Tᴏ Cʀᴇᴀᴛᴇ Lɪɴᴋ Fᴏʀ Mᴜʟᴛɪᴘʟᴇ Mᴇᴅɪᴀ
  
    FILTER_TXT = "Sᴇʟᴇᴄᴛ Wʜɪᴄʜ Oɴᴇ Yᴏᴜ Wᴀɴᴛ...✨"""
    
    GLOBALFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

<b>Nᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
❖ /gfilter - Tᴏ Aᴅᴅ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
❖ /gfilters - Tᴏ Vɪᴇᴡ Lɪsᴛ Oғ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
❖ /delg - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ
❖ /delallg - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀꜱ

❖ /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    MANUELFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Fɪʟᴛᴇʀs</b>

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tʜɪs Bᴏᴛ Sʜᴏᴜʟᴅ Hᴀᴠᴇ Aᴅᴍɪɴ Pʀɪᴠɪʟʟᴀɢᴇ.
𝟸. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ.
𝟹. Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs Hᴀᴠᴇ A Lɪᴍɪᴛ Oғ 𝟼𝟺 Cʜᴀʀᴀᴄᴛᴇʀs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
❖ /filter - Aᴅᴅ A Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
❖ /filters - Lɪsᴛ Aʟʟ Tʜᴇ Fɪʟᴛᴇʀs Oғ A Cʜᴀᴛ
❖ /del - Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
❖ /delall - Dᴇʟᴇᴛᴇ Tʜᴇ Wʜᴏʟᴇ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ (Cʜᴀᴛ Oᴡɴᴇʀ Oɴʟʏ)

❖ /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    BUTTON_TXT = """<b>Hᴇʟᴘ Fᴏʀ Bᴜᴛᴛᴏɴs</b>

<i>Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴏᴛʜ Uʀʟ Aɴᴅ Aʟᴇʀᴛ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs.</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tᴇʟᴇɢʀᴀᴍ Wɪʟʟ Nᴏᴛ Aʟʟᴏᴡs Yᴏᴜ Tᴏ Sᴇɴᴅ Bᴜᴛᴛᴏɴs Wɪᴛʜᴏᴜᴛ Aɴʏ Cᴏɴᴛᴇɴᴛ, Sᴏ Cᴏɴᴛᴇɴᴛ Is Mᴀɴᴅᴀᴛᴏʀʏ.
𝟸. Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴜᴛᴛᴏɴs Wɪᴛʜ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Mᴇᴅɪᴀ Tʏᴘᴇ.
𝟹. Bᴜᴛᴛᴏɴs Sʜᴏᴜʟᴅ Bᴇ Pʀᴏᴘᴇʀʟʏ Pᴀʀsᴇᴅ As Mᴀʀᴋᴅᴏᴡɴ Fᴏʀᴍᴀᴛ

<b>Uʀʟ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonurl:xxxxxxxxxxxx)

<b>Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonalert:Tʜɪs Is Aɴ Aʟᴇʀᴛ Mᴇssᴀɢᴇ)"""

    AUTOFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ AᴜᴛᴏFɪʟᴛᴇʀ</b>

<Ai>Aᴜᴛᴏ Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Tᴏ Fɪʟᴛᴇʀ & Sᴀᴠᴇ Tʜᴇ Fɪʟᴇs Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Fʀᴏᴍ Cᴜᴀɴɴᴇʟ Tᴏ Gʀᴏᴜᴘ. Yᴏᴜ Cᴀɴ Usᴇ Tʜᴇ Fᴏʟʟᴏᴡɪɴɢ Cᴏᴍᴍᴀɴᴅ Tᴏ ᴏɴ/ᴏғғ Tʜᴇ AᴜᴛᴏFɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ</i>

❖ /autofilter on - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴇɴᴀʙʟᴇ ɪɴ ʏᴏʀ ᴄʜᴀᴛ
❖ /autofilter off - ᴀᴜᴛᴏғɪʟᴛᴇʀ ᴅɪsᴀʙʟᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ

<Ob>Oᴛʜᴇʀ Cᴏᴍᴍᴀɴᴅs:</b>
❖ /set_template - Sᴇᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ 
❖ /get_template - Gᴇᴛ Cᴜʀʀᴇɴᴛ Iᴍᴅʙ Tᴇᴍᴘʟᴀᴛᴇ Fᴏʀ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    CORONA_TXT ="""<b>Thank you...
to everyone who supported COVID19 API over the past few years.

This API handled over 1 billion requests, serving numerous dashboards, mobile apps and travel-related solutions worldwide. Due to the changing nature of Covid-19 and subsequent lack of data we decided to discontinue the service on May 15th, 2023.</b>

Made With ❤️ BY @StarkBotUpdates"""
    STICKER_TXT ="""<b>COMMAND /stickerid\n𝖨𝖿 𝖸𝗈𝗎 𝖭𝖾𝖾𝖽 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 𝖢𝗅𝗂𝖼𝗄 /stickerid 𝖳𝗈 𝖦𝖾𝗍 𝖲𝗍𝗂𝖼𝗄𝖾𝗋 𝖨𝖽 (𝖱𝖾𝗉𝗅𝗒 𝖶𝗂𝗍𝗁 𝖲𝗍𝗂𝖼𝗄𝖾𝗋)</b>
    
    Made With ❤️ BY @StarkBotUpdates"""
    ALIVE_TXT ="""╔════❰ <b>ALIVE MODULE</b> ❱═════❍⊱❁۪۪
║
║╭━━━━━━━━━━━━━━━➣
║┣⪼ /alive - check me alive or dead🤧
║┣⪼ /helpme - help 
║┣⪼ /repo - repo of bot
║┣⪼ /runs - random
║╰━━━━━━━━━━━━━━━➣
║
║Made With ❤️ BY @StarkBotUpdates
║
╚══════════════════════❍⊱❁۪۪"""
    FUN_TXT ="""╔═══════❰ <b>FUN MODULE</b> ❱══════❍⊱❁۪۪
║
║╭━━━━━━━━━━━━━━━➣
║┣⪼🎲 NOTHING MUCH JUST SOME FUN THINGS
║
║┣⪼𝟣. /dice - Roll The Dice 
║┣⪼𝟤. /Throw 𝗈𝗋 /Dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Dart
║┣⪼𝟣. /Goal or /Shoot - To Make A Goal Or Shoot
║┣⪼𝟤. /luck - To Spin 
║┣⪼𝟣. /pinball or /tenpin - Bowling
║┣⪼𝟤. /break
║
║╰━━━━━━━━━━━━━━━➣
║
║Made With ❤️ BY @StarkBotUpdates
║
╚═══════════════════════❍⊱❁۪۪"""

    FONT_TXT = """ /font [ᴛᴇxᴛ] - Tᴏ Cʜᴀɴɢᴇ Yᴏᴜʀ Tᴇxᴛ Fᴏɴᴛs Tᴏ Fᴀɴᴄʏ Fᴏɴᴛ"""
    

    CONNECTION_TXT = """╔═══❰ <b>Hᴇʟᴘ Fᴏʀ Cᴏɴɴᴇᴄᴛɪᴏɴs</b> ❱═══❍⊱❁
║
║╭━━━━━━━━━━━━━━━━━━━➣
║┣⪼ <i> Usᴇᴅ Tᴏ Cᴏɴɴᴇᴄᴛ Bᴏᴛ Tᴏ Pᴍ Fᴏʀ Mᴀɴᴀɢɪɴɢ Fɪʟᴛᴇʀs</i>
║┣⪼ <i> Iᴛ Hᴇʟᴘs Tᴏ Aᴠᴏɪᴅ Sᴘᴀᴍᴍɪɴɢ Iɴ Gʀᴏᴜᴘs</i>
║┣⪼ <b>Nᴏᴛᴇ:</b>
║┣⪼ ❖ Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ A Cᴏɴɴᴇᴄᴛɪᴏɴ.
║┣⪼ ❖ Sᴇɴᴅ /connect Fᴏʀ Cᴏɴɴᴇᴄᴛɪɴɢ Mᴇ Tᴏ Uʀ Pᴍ
║
║┣⪼ <b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
║┣⪼ /connect - Cᴏɴɴᴇᴄᴛ A Pᴀʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ Tᴏ Yᴏᴜʀ Pᴍ
║┣⪼ /disconnect - Dɪsᴄᴏɴɴᴇᴄᴛ Fʀᴏᴍ A Cʜᴀᴛ
║┣⪼ /connections - Lɪsᴛ Aʟʟ Yᴏᴜʀ Cᴏɴɴᴇᴄᴛɪᴏɴs
║
║╰━━━━━━━━━━━━━━━━━━━➣
║
║Made With ❤️ BY @StarkBotUpdates
║
╚═══════════════════════❍⊱❁
"""

    ADMIN_TXT = """<b>Hᴇʟᴩ Fᴏʀ Aᴅᴍɪɴꜱ</b>
    
<i>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</i>

<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ</b>
• /logs - Tᴏ Gᴇᴛ Tʜᴇ Rᴇᴄᴇɴᴛ Eʀʀᴏʀꜱ
• /delete - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪꜰɪᴄ Fɪʟᴇ Fʀᴏᴍ DB
• /deleteall - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Fɪʟᴇs Fʀᴏᴍ DB
• /users - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Uꜱᴇʀꜱ Aɴᴅ Iᴅꜱ
• /chats - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Cʜᴀᴛꜱ Aɴᴅ Iᴅꜱ
• /channel - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟꜱ
• /broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀꜱᴛ A Mᴇꜱꜱᴀɢᴇ Tᴏ Aʟʟ Uꜱᴇʀꜱ
• /group_broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ A Mᴇssᴀɢᴇ Tᴏ Aʟʟ Cᴏɴɴᴇᴄᴛᴇᴅ Gʀᴏᴜᴘs
• /leave  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ A Cʜᴀᴛ
• /disable  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Dɪꜱᴀʙʟᴇ A Cʜᴀᴛ
• /invite - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Gᴇᴛ Tʜᴇ Iɴᴠɪᴛᴇ Lɪɴᴋ Oғ Aɴʏ Cʜᴀᴛ Wʜᴇʀᴇ Tʜᴇ Bᴏᴛ Is Aᴅᴍɪɴ
• /ban_user  - Wɪᴛʜ Iᴅ Tᴏ Bᴀɴ A Uꜱᴇʀ
• /unban_user  - Wɪᴛʜ Iᴅ Tᴏ Uɴʙᴀɴ A Uꜱᴇʀ
• /restart - Tᴏ Rᴇsᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
• /clear_junk - Cʟᴇᴀʀ Aʟʟ Dᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ & Bʟᴏᴄᴋᴇᴅ Aᴄᴄᴏᴜɴᴛ Iɴ Dᴀᴛᴀʙᴀsᴇ
• /clear_junk_group - Cʟᴇᴀʀ Aᴅᴅ Rᴇᴍᴏᴠᴇᴅ Gʀᴏᴜᴘ Oʀ Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Gʀᴏᴜᴘs Oɴ Dʙ"""


    STATUS_TXT = """╔════❰ <b>ʙᴏᴛ sᴛᴀᴛᴜs</b> ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📄 ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
║┃
║┣⪼👥 ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
║┃
║┣⪼💬 ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
║┃
║┣⪼💾 ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ: <code>{}</code>
║┃
║┣⪼📊 ꜰʀᴇᴇ ᴅʙ ꜱɪᴢᴇ: <code>{}</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

⫸ ɢʀᴏᴜᴩ: {a}
⫸ ɢ-ɪᴅ: <code>{b}</code>
⫸ ʟɪɴᴋ: @{c}
⫸ ᴍᴇᴍʙᴇʀꜱ: <code>{d}</code>
⫸ ᴀᴅᴅᴇᴅ ʙʏ: {e}

⫸ ʙʏ: @{f}</b>"""
  
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
⫸ ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
⫸ ᴀᴄᴄ-ɴᴀᴍᴇ: {}
⫸ ᴜꜱᴇʀɴᴀᴍᴇ: @{}

⫸ ʙʏ: @{}</b>"""
  
    GROUPMANAGER_TXT = """<b>Hᴇʟᴩ Fᴏʀ GʀᴏᴜᴩMᴀɴᴀɢᴇʀ</b>

<i>Tʜɪꜱ Iꜱ Hᴇʟᴩ Oꜰ Yᴏᴜʀ Gʀᴏᴜᴩ Mᴀɴᴀɢɪɴɢ. Tʜɪꜱ Wɪʟʟ Wᴏʀᴋ Oɴʟʏ Fᴏʀ Gʀᴏᴜᴩ aᴅᴍɪɴꜱ</i>

<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ:</b>
❖ /inkick - Cᴏᴍᴍᴀɴᴅ Wɪᴛʜ Rᴇǫᴜɪʀᴇᴅ Aʀɢᴜᴍᴇɴᴛs Aɴᴅ I Wɪʟʟ Kɪᴄᴋ Mᴇᴍʙᴇʀs Fʀᴏᴍ Gʀᴏᴜᴘ.
❖ /instatus - Tᴏ Cʜᴇᴄᴋ Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs Oғ Cʜᴀᴛ Mᴇᴍʙᴇʀ Fʀᴏᴍ Gʀᴏᴜᴘ.
❖ /dkick - Tᴏ Kɪᴄᴋ Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛs
❖ /ban - To Bᴀɴ A Uꜱᴇʀ Fᴏʀᴍ Tʜᴇ Gʀᴏᴜᴩ
❖ /unban - Uɴʙᴀɴ Tʜᴇ Bᴀɴɴᴇᴅ Uꜱᴇʀ
❖ /tban - Tᴇᴍᴩᴏʀᴀʀʏ Bᴀɴ A Uꜱᴇʀ
❖ /mute - To Mᴜᴛᴇ A Uꜱᴇʀ
❖ /unmute - To Uɴᴍᴜᴛᴇ Tʜᴇ Mᴜᴛᴇᴅ Uꜱᴇʀ
❖ /tmute - Wɪᴛʜ Vᴀʟᴜᴇ To Mᴜᴛᴇ Uᴩ To Pᴀʀᴛɪᴄᴜʟᴀʀ Tɪᴍᴇ Eɢ: <code>/tmute 2h</code> To Mᴜᴛᴇ 2Hᴏᴜʀ Vᴀʟᴜᴇꜱ Iꜱ (m/h/d)
❖ /pin - Tᴏ Pɪɴ A Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ
❖ /unpin - Tᴏ Uɴᴩɪɴ Tʜᴇ Mᴇꜱꜱᴀɢᴇ Oɴ Yᴏᴜʀ Cʜᴀᴛ
❖ /purge - Dᴇʟᴇᴛᴇ Aʟʟ Mᴇssᴀɢᴇs Fʀᴏᴍ Tʜᴇ Rᴇᴘʟɪᴇᴅ Tᴏ Mᴇssᴀɢᴇ, Tᴏ Tʜᴇ Cᴜʀʀᴇɴᴛ Mᴇssᴀɢᴇ"""

    TTS_TXT = """ /tts [ᴛᴇxᴛ] - Cᴏɴᴠᴇʀᴛ Tᴇxᴛ Tᴏ Sᴘᴇᴇᴄʜ"""

    LYRIC_TXT = """<b>SONG LYRICS</b>

To Find the Lyrics of A Song 

❖ /song [ɴᴀᴍᴇ] - Tᴏ Sᴇᴀʀᴄʜ Tʜᴇ Sᴏɴɢ Iɴ YᴏᴜTᴜʙᴇ 🎈
❖ /lyric - ʀᴇᴘʟʏ ᴛᴏ ᴀ ꜱᴏɴɢ ɴᴀᴍᴇ

Made With ❤️ BY @StarkBotUpdate"""

    JSON_TXT = """⚙ <b>Json</b>

Bot Send Json For All Replied Messages Using A Simple Command

📚 Avaible Command:

⫸ /json :- Reply To Any Message To Get Json

⫸ You Can Use This Command In Pm And Groups

Made With ❤️ BY @StarkBotUpdates"""

    EXTRAMOD_TXT = """<b>Hᴇʟᴩ Fᴏʀ Exᴛʀᴀ Mᴏᴅᴜʟᴇ</b>

<i>Jᴜꜱᴛ Sᴇɴᴅ Aɴʏ Iᴍᴀɢᴇ Tᴏ Eᴅɪᴛ Iᴍᴀɢᴇ ✨</i>

<b>Cᴏᴍᴍᴀɴᴅꜱ & Uꜱᴀɢᴇ:</b>
❖ /id - Gᴇᴛ Iᴅ Oғ A Sᴘᴇᴄɪғᴇᴅ Usᴇʀ
❖ /info  - Gᴇᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ Aʙᴏᴜᴛ A Usᴇʀ
❖ /imdb  - Gᴇᴛ Tʜᴇ Fɪʟᴍ Iɴғᴏʀᴍᴀᴛɪᴏɴ Fʀᴏᴍ Iᴍᴅʙ Sᴏᴜʀᴄᴇ"""    
    
    CREATOR_REQUIRED = "❗<b>Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"
      
    INPUT_REQUIRED = "❗ **Aʀɢᴜᴍᴇɴᴛ Rqᴜɪʀᴇᴅ**"
      
    KICKED = "✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ"
      
    START_KICK = "Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ"
      
    ADMIN_REQUIRED = "❗<b>Iᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"
      
    DKICK = "✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"
      
    FETCHING_INFO = "<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"
   
    SERVER_STATS = """Sᴇʀᴠᴇʀ Sᴛᴀᴛꜱ:
 
Uᴩᴛɪᴍᴇ: {}
CPU Uꜱᴀɢᴇ: {}%
RAM Uꜱᴀɢᴇ: {}%
Tᴏᴛᴀʟ Dɪꜱᴋ: {}
Uꜱᴇᴅ Dɪꜱᴋ: {} ({}%)
Fʀᴇᴇ Dɪꜱᴋ: {}"""
    
    BUTTON_LOCK_TEXT = "Hᴇʏ {query}\n𝚃𝙷𝙸𝚂 𝙸𝚂 𝙽𝙾𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄 , 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 ! 😊"
   
    FORCE_SUB_TEXT = "Sᴏʀʀʏ Bʀᴏ Yᴏᴜʀ Nᴏᴛ Jᴏɪɴᴇᴅ Mʏ Cʜᴀɴɴᴇʟ Sᴏ Pʟᴇᴀsᴇ Cʟɪᴄᴋ Jᴏɪɴ Bᴜᴛᴛᴏɴ Tᴏ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Aɴᴅ Tʀʏ Aɢᴀɪɴ"
   
    WELCOM_TEXT = """Hᴇʏ {user} 💞

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}.

ꜱʜᴀʀᴇ & ꜱᴜᴩᴩᴏʀᴛ, ʀᴇqᴜᴇꜱᴛ ʏᴏᴜ ᴡᴀɴᴛᴇᴅ ᴍᴏᴠɪᴇꜱ"""
  
    IMDB_TEMPLATE = """<b>Qᴜᴇʀʏ: {query}</b>

🏷 Tɪᴛʟᴇ: <a href={url}>{title}</a>
🎭 Gᴇɴʀᴇꜱ: {genres}
📆 Yᴇᴀʀ: <a href={url}/releaseinfo>{year}</a>
🌟 Rᴀᴛɪɴɢ: <a href={url}/ratings>{rating}</a>/10"""
    

    CUSTOM_FILE_CAPTION = """<b>Hey {mention} ⚡️</b>
{file_name} 
size - {file_size} 
╭─────── • ◆ • ───────➤ 
┣ ▫️ @FDFileStoreBot
┣ ▫️ @StarkBotUpdates
╰─────── • ◆ • ───────➤"""
  
 


   
  
 


