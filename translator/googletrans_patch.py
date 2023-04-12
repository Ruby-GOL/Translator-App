from googletrans import Translator
import httpx

# Increase the timeout to 10 seconds
extended_timeout = httpx.Timeout(connect_timeout=10.0)

class PatchedTranslator(Translator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client.timeout = extended_timeout

translator = PatchedTranslator()

