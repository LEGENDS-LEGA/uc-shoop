# ██╗     ███████╗ ██████╗ ███████╗███╗  ██╗██████╗  ██████╗
# ██║     ██╔════╝██╔════╝ ██╔════╝████╗ ██║██╔══██╗██╔════╝
# ██║     █████╗  ██║  ██╗ █████╗  ██╔██╗██║██║  ██║╚█████╗
# ██║     ██╔══╝  ██║  ╚██╗██╔══╝  ██║╚████║██║  ██║ ╚═══██╗
# ███████╗███████╗╚██████╔╝███████╗██║ ╚███║██████╔╝██████╔╝
# ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚══╝╚═════╝ ╚═════╝  


from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from pyrogram.errors import RPCError


api_id = '24235841'
api_hash = '5dcca0184e08a824d00aa0cc24c0a18c'
bot_token = '7357455642:AAHbHrrL5X3h1VG_lXX2LNam8-Z0AiPur6E'
MOD = 7316630403


app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


with app:
    ids = open ( "ids.txt" , "r")
    ids_array = ids.read().split("\n")
    ids_array.remove("")
    for i in ids_array:
        try:
            app.send_message( i , "Աշխարհի ամենալավ UC-ները, 𝐋𝐞𝐠𝐞𝐧𝐝-ի կողմից սպասում են ձեզ, ➡️ Սեղմեք այս հրամանին՝ /uc_legends")
        except Exception:
            pass

@app.on_message(filters.command("start"))
async def start_message(_,msg):
    greeting = "Բարև ձեզ, ես LEGENDA-ն եմ!:Այս հրամանաը կոգնի ձես գնել uc-ները /uc_legends"
    await msg.reply(greeting)




replyd = []
@app.on_message(filters.photo)
async def photo(_,msg):
    global MOD
    await app.send_message ( msg.chat.id, "**Շնորհակալություն, խնդրում ենք ուղարկել ձեր խաղի ID-ն առանց որևէ այլ նշանների:**")
    await app.forward_messages( MOD , msg.chat.id , msg.id)
    await app.send_message( MOD , f"**User link:**{msg.from_user.mention}\nIf link upper doesnt work try username: {msg.from_user.username}\nThis is Users id, if links isnt working: {msg.from_user.id}")
    global replyd 
    await asyncio.sleep(5*60)
    if msg.from_user.id not in replyd:
        await app.send_message(msg.chat.id, "Սպասեք 5-ր " )
        await app.send_message( MOD , f"Patasxani exoos: {msg.from_user.id}")
        await app.send_message( MOD , f"**User link:**{msg.from_user.mention}\nIf link upper doesnt work try username: {msg.from_user.username}\nThis is Users id, if links isnt working: {msg.from_user.id}")


@app.on_message(filters.command( "reply", prefixes= ["." , "!", "-", "/"]))
async def reply_mod(_,msg):
    global MOD
    if msg.from_user.id == MOD:
        text_to_forw = msg.text.split(maxsplit = 1)[1]
        try:
            msg_with_id = msg.reply_to_message.text
            repled = True
        except Exception:
            await app.send_message ( msg.chat.id , "You forgot to reply to the message with **ID**! Try again")
            repled = False
        if repled == True:
            array = msg_with_id.split()
            try:
                user_to_forw_id = array[-1]
                user_to_forw_id = int(user_to_forw_id)
                taken_id = True
            except Exception:
                await app.send_message ( msg.chat.id , "That was a wrong message, plz reply to the message with **user ID**")
                taken_id = False
            if taken_id == True:
                await app.send_message ( user_to_forw_id , f"**Moderator**: __{text_to_forw}__")
                global replyd 
                replyd.append (msg.from_user.id)

@app.on_message(filters.command("uc_legends" , prefixes="/"))
async def uc_message(_,msg):
    prices = """
✅30💰 - 200֏ 🔥
    
✅60💰 - 400֏ 🔥

✅120💰 - 800֏ 🔥

✅180💰 - 1100֏ 🔥

✅240💰 - 1400֏ 🔥

✅325💰 - 1800֏ 🔥

✅660💰 - 3500֏ 🔥
    
✅720💰 - 3700֏ 🔥
 
✅1800💰 - 8500֏ 🔥

✅1950💰 - 9000֏ 🔥

✅3850💰 - 17000֏  🔥

✅4000💰 - 17500֏  🔥

✅5650💰 - 26500֏  🔥

✅8100💰 - 33000֏  🔥

✅8400💰 - 34000֏ 🔥
  
🛒 Մեր բանկային հաշիվները իմանալու համար սեղմեք այս հրամանին /legends\n
ՈՒշադրություն /ID ուղարկեք նկարի հետ\n"""

    footer = """Մեր բանկային քարտի համար՝ Telceli\n
Խնդիրների դեպքում գրեք մեզ:"""

    legends_part = """          
    **💎 LEGENDS 💎**\n\n  
Մեր փորձառու թիմը պատրաստ է օգնել ձեզ  յուրաքանչյուր հարցում: Ադմին  @legendsold։ \n\n
Սեխմեք այս հրամանին /legends որ իմանանք մեր բնակային հաշիվները։\n"""
    
    full_message = prices + "\n\n" + legends_part
    
    await app.send_message( msg.chat.id , full_message)

@app.on_message(filters.command("legends"))
async def legends_message(_,msg):
    legends_text = "**💎 LEGENDS 💎**\n\n💵 TELCEL WALLET         **→**       +37498222474\n 💳 Բանկային քարտ      **→**     4355053926154248 \n\nԲարի գալուստ մեր UC-SHOP! \n Մեր փորձառու թիմը պատրաստ է օգնել ձեզ  յուրաքանչյուր հարցում: \n Եթե բոտը չի աշխատում գրեք մեր ադմինին @legendsold "
    await app.send_message( msg.chat.id , legends_text)








text_random_char = """ Սեղմեք կոճակը /start"""

@app.on_message()
async def check_id(_,msg):
    global MOD
    try:
        id = msg.text
        id = int(id)
        await app.send_message( MOD , f"**ID of {msg.from_user.first_name} is** `{id}`" )
        await app.send_message( msg.chat.id , "Շնորհակալություն, խնդրում եմ սպասեք:")
    except Exception:
        global text_random_char
        await app.send_message ( msg.chat.id , text_random_char)


@app.on_message(group=1)
async def save_ids(_,msg):
    ids = open( "ids.txt" , "r")
    ids_array = ids.read().split("\n")
    if str(msg.from_user.id) not in ids_array:
        ids = open( "ids.txt", "a")
        ids.write(f"{msg.from_user.id}\n")



app.run()
# .reply botna uxarkum