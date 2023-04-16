import subprocess
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os
#import django settings
from django.conf import settings

article = "UN Chief says there is no military solution in Syria"
def translator(text_input):

    token = "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"
    tokenizer = AutoTokenizer.from_pretrained(
        "facebook/nllb-200-distilled-600M", use_auth_token=token
    )
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M", use_auth_token=token)

    

    inputs = tokenizer(text_input, return_tensors="pt")

    translated_tokens = model.generate(
        **inputs, forced_bos_token_id=tokenizer.lang_code_to_id["kik_Latn"], max_length=30
    )
    text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
   
    # AUDIO_FORMAT = 'mp3'
    # URL = 'https://www.africanvoices.tech/language/kik'
    

    # # Construct the command for the first curl command
    # cmd1 = f'curl -X POST -F "synth_id=kik_opb263" -F "text={text}" -F "audio_format={AUDIO_FORMAT}" {URL} | grep synth-audio | sed -e \'s/.*src="\\(.\\){AUDIO_FORMAT}.*/\\1/\''

    # # Execute the first curl command and capture the output
    # output1 = subprocess.check_output(cmd1, shell=True, text=True)
    # output_file = f'sound.{AUDIO_FORMAT}'
    # output_dir = os.path.join(settings.STATIC_URL, 'audio')

    # # Construct the command for the second curl command
    # output_path = os.path.join(output_dir, output_file).replace('/', '\\')
    # cmd2 = f"curl https://www.africanvoices.tech{output1}{AUDIO_FORMAT} --output '{output_path}'"

    # # Execute the second curl command
    # subprocess.run(cmd2, shell=True)
    # AUDIO_FORMAT = 'wav'
    # URL = 'https://www.africanvoices.tech/language/kik'
    # TEXT =  text # Replace with the desired text

    # # Construct the command for the first curl command
    # cmd1 = f'curl -X POST -F "synth_id=kik_opb263" -F "text={TEXT}" -F "audio_format={AUDIO_FORMAT}" {URL} | grep synth-audio | sed -e \'s/.*src="\\(.*\\){AUDIO_FORMAT}.*/\\1/\''

    # # Execute the first curl command and capture the output
    # output1 = subprocess.check_output(cmd1, shell=True, text=True).strip()

    # output_file = f'sound.{AUDIO_FORMAT}'
    # output_dir = os.path.join(settings.STATIC_URL, 'audio')
   
    # # Construct the command for the second curl command
    # cmd2 = f"curl https://www.africanvoices.tech{output1}{AUDIO_FORMAT} --output '{output_dir}\{output_file}'"

    # # Execute the second curl command
    # voice = subprocess.run(cmd2, shell=True)
    

    


    AUDIO_FORMAT = 'wav'
    URL = 'https://www.africanvoices.tech/language/kik'
    TEXT =  text # Replace with the desired text

    # Construct the command for the first curl command
    cmd1 = f'curl -X POST -F "synth_id=kik_opb263" -F "text={TEXT}" -F "audio_format={AUDIO_FORMAT}" {URL} | grep synth-audio | sed -e \'s/.*src="\\(.*\\){AUDIO_FORMAT}.*/\\1/\''

    # Execute the first curl command and capture the output
    output1 = subprocess.check_output(cmd1, shell=True, text=True).strip()

    output_file = f'sound.{AUDIO_FORMAT}'
    output_dir = os.path.join(settings.STATIC_ROOT, 'audio')

    # Construct the command for the second curl command
    cmd2 = f"curl https://www.africanvoices.tech{output1}{AUDIO_FORMAT} --output '{output_dir}/{output_file}'"

    # Execute the second curl command
    voice = subprocess.run(cmd2, shell=True)


    return "This is sound"
