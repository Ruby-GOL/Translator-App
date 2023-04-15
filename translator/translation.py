import torch
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

from langdetect import detect

def load_m2m100_model():
    model_name = "facebook/m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model
    
tokenizer, model = load_m2m100_model()

def translate(text, src_lang, tgt_lang):
    tokenizer.src_lang = src_lang
    encoded_input = tokenizer(text, return_tensors="pt")
    translated_output = model.generate(**encoded_input, forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang])
    translation = tokenizer.decode(translated_output[0], skip_special_tokens=True)
    return translation


def detect_language(text):
    try:
        lang = detect(text)
    except:
        lang = "en"  # default to English if detection fails
    return lang
