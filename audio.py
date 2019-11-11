#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pydub import AudioSegment
from pydub.playback import play

class audio:
    def load_audio(name):
        if name[-3:]=="wav":
            sound = AudioSegment.from_file(name, format="wav")
        if name[-3:]=="mp3":
            sound = AudioSegment.from_file(name, format="mp3")

        play(sound)


# In[ ]:





# In[ ]:




