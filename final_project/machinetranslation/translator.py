import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
class Watson():
    '''
    Watson class, initializes ibm_watson service for it's easy use
    '''
    def __init__(self):
        load_dotenv()
        self.apikey = os.environ['apikey']
        self.url = os.environ['url']
        self.authenticator = IAMAuthenticator(f'{self.apikey}')
        self.language_translator = LanguageTranslatorV3(
            version='2018-05-01',
            authenticator=self.authenticator
        )
        self.language_translator.set_service_url(f'{self.url}')

    def english_to_french(self, english_text):
        '''
        Translates given english text to french
        '''
        try:
            french_text = self.language_translator.translate(
                text=english_text,
                model_id='en-fr'
            ).get_result()
            return french_text['translations'][0]['translation']
        except:
            return ''

    def french_to_english(self, french_text):
        '''
        Translates given text to english
        '''
        try:
            english_text = self.language_translator.translate(
                text=french_text,
                model_id='fr-en'
            ).get_result()
            return english_text['translations'][0]['translation']
        except:
            return ''






    

