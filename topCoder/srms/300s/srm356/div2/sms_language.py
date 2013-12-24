import re

class SMSLanguage:
    def translate(self, text):
        text = re.sub(r'[\.,\?!]', '', text).lower()
        text = re.sub(r'and', '&', text)
        text = re.sub(r'ate', '8', text)
        text = re.sub(r'at', '@', text)
        return re.sub(r'you', 'U', text)
