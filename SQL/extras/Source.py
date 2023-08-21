import re
import time
from datetime import datetime
from matrix import StartTime, matrix
from matrix.Config import Config
from matrix.plugins import mention
help1 = ("**✾︙ كيفيه التنصيب :**")
help2 = ("**✾︙ قـائمـه الاوامـر :**\n**✾︙ قنـاه السـورس :** @MatrixThon\n** \n - اوامر الاونلاين تشتغل فقط في المجموعات")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎✾┊𝖬y 𖠄 {mention} ٫ **\n‌‎**‌‎✾┊𝖡𝗈𝖳 𖠄 {TG_BOT} ٫**\n**‌‎‌‎✾┊𝖳𝗂𝗆𝖾 𖠄 {TM} ٫**\n**‌‎ꪎ┊‌‎𝖬𝖺𝗍𝗋𝗂ꪎ 𝖠𝗋𝖺𝖻𝗂𝖼 𖠄** @MaTrixThon"
