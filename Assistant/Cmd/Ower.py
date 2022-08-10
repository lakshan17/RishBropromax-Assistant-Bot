from Assistant import app
from Assistant.Cmd.commands import *

@app.on_message(command("Assistant"))
async def plug(_, message):
    RishBroProMax = await message.reply_text(text="Hello I am Assistant Bot Of Rishmika Sandanu. My Master Is Good Boy. You Wan't Massege my master Follow the Rules \n\n >> Not Spam \n >> Don't Use Bad Words"
    )
    RishBroproMax = """
I m Assistant Bot Of Rishmika Sandanu
@ImRishmika_Bot   
    """
    await RishBroproMax.edit_text(supun)

__MODULE__ = "ower"
__HELP__ = """  
/Assistant - Assisatnt Massege
"""
