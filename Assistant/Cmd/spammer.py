from Assistant import app
from Assistant.Cmd.commands import *

@app.on_message(command("ban spammer"))
async def plug(_, message):
    RishBroProMax = await message.reply_text(text="අහරයා උන් spam කරන්නේ අපි massege බලන්නේ නැති උනාම තොට ඕක තේරෙන්නේ නැද්ද ?? #Admin Please Send /unban {removed_user_id} "
    )
    RishBroproMax = """
I m Assistant Bot Of Rishmika Sandanu
@ImRishmika_Bot   
    """
    await RishBroproMax.edit_text(Rishmika)


