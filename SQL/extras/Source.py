import re
import time
from datetime import datetime
from matrix import StartTime, matrix
from matrix.Config import Config
from matrix.plugins import mention
help1 = ("**ꪎ︙ كيفيه التنصيب :**")
help2 = ("**ꪎ︙ قـائمـه الاوامـر :**\n**ꪎ︙ قنـاه السـورس :** @Matrix_Thon\n** \n - اوامر الاونلاين تشتغل فقط في المجموعات ")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎ꪎ┊𝖬y 𖠄 {mention} ٫ **\n‌‎**‌‎ꪎ┊𝖡𝗈𝖳 𖠄 {TG_BOT} ٫**\n**‌‎‌‎ꪎ┊𝖳𝗂𝗆𝖾 𖠄 {TM} ٫**\n**‌‎‌‎ꪎ┊‌‎𝖵𝖾𝖱𝗌𝗅𝗈𝖭 𖠄 (8.1) ,** \n**‌‎ꪎ┊‌‎𝖬𝖺𝗍𝗋𝗂ꪎ 𝖠𝗋𝖺𝖻𝗂𝖼 𖠄** @Matrix_Thon"
