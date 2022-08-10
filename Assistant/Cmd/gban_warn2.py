from Assistant import app
from Assistant.Cmd.commands import *

@app.on_message(command("gban"))
async def plug(_, message):
    RishBroProMax = await message.reply_text(text="උක්කන්න එපා gban ගහප්න්කෝ... මරනවා දැන ගනින් !! \n වෙන group වල Gban  ගහගනින් මේ Group එකෙක් බැ මම bot කියල බලන්නේ නැ හොදේ....."
    )
    RishBroproMax = """
I m Assistant Bot Of Rishmika Sandanu
@ImRishmika_Bot   
    """
    await RishBroproMax.edit_text(Rishmika)

