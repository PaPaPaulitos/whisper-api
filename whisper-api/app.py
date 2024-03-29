import requests

url = 'http://XXX:5000/whisper'

file_path = 'esse_audio.mp3'

with open(file_path, 'rb') as audio_file:
    files = {'audio_file': (file_path, audio_file)}
    response = requests.post(url, files=files)

if response.status_code == 200:
    print("Resposta da API:", response.json())
else:
    print("Erro ao enviar o arquivo:", response.status_code)
