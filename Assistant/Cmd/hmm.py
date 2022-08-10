from Assistant import app
from Assistant.Cmd.commands import *

@app.on_message(command("hmm"))
async def plug(_, message):
    RishBroProMax = await message.reply_text(text="Join [Things Zone](t.me/ThingsZone) | [TeamSemmy](t.me/TeamSemmy)"
    )
    RishBroproMax = """
I m Assistant Bot Of Rishmika Sandanu
@ImRishmika_Bot   
    """
    await RishBroproMax.edit_text(Rishmika)

__MODULE__ = "hmm"
__HELP__ = """  
/hmm - Support group link
"""
