
from gtts import gTTS
import os
fp = open("text.txt", "r")
mytext = fp.read().replace("\n", "")
language = 'ar'
output = gTTS(text=mytext,lang=language,slow=False)
output.save("test.mp3")
os.system("start test.mp3")
fp.close()

