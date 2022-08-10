# RishBroPromax Assistant Example Plugin Format Here : 
You can create your own custom plugin useing this format or use any [pyrogram](http://pyrogram.org) method !

```
from Assistant import app
from Assistant.Cmd.commands import *

@app.on_message(command("test"))
async def plug(_, message):
    RishBroProMax = await message.reply_text(text="Hello I am Assistant Bot Of Rishmika Sandanu"
    )
    RishBroproMax = """
I m Assistant Bot Of Rishmika Sandanu
@ImRishmika_Bot   
    """
    await RishBroproMax.edit_text(Rishmika)

__MODULE__ = "test"
__HELP__ = """  
/Assistant - test cmd here
"""
```
