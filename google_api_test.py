#sample wav file location: F:\pro\pbl-sample
from base64 import encode

from google.cloud import speech
import numpy as np
import io
def transcribe_with_word_time_offsets(speech_file):
    """Transcribe the given audio file asynchronously and output the word time
    offsets."""
    from google.cloud import speech
    import numpy as np
    import io
    import json
    from collections import OrderedDict

    # Instantiates a client
    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR",
        enable_word_time_offsets=True,
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    result = operation.result(timeout=180)

    for result in result.results:
        alternative = result.alternatives[0]
        print("Transcript: {}".format(alternative.transcript))
        print("Confidence: {}".format(alternative.confidence))

        data_total_form_list = {
            "sentence" : []
        }

        for word_info in alternative.words:
            data_form = OrderedDict()
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time

            print(
                f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
            )

            #word들을 json형태로 바꿔주기
            #이유:csv변환 코드가 json만 받아서.
            data_total_form_list["sentence"].append({
                'word' : word,
                'start_time' : start_time.total_seconds(),
                'end_time' : end_time.total_seconds()
            })

    #json 파일 생성
    json_data = json.dumps(data_total_form_list)
    json_decode_data = json_data.encode().decode('unicode-escape')
    with open('test.json', 'w', encoding='UTF-8') as f:
        f.write(json_decode_data)

transcribe_with_word_time_offsets('F:\pro\pbl-sample\sample2.wav')