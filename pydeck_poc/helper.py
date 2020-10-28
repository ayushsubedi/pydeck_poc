from googletrans import Translator
import requests

translator = Translator()
EXTERNAL_API = 'https://www.affirmations.dev/'
DEFAULT_TEXT = 'hello world, we are having issues'

def tweet_text():
    r = requests.get(EXTERNAL_API)
    data = r.json()
    eng_text = data.get('affirmation', DEFAULT_TEXT)
    nep_text = translator.translate(eng_text, dest='ne')
    return nep_text.text
