from gtts import gTTS

file_path = 'текстовый_файл.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

obj = gTTS(text, lang='ru')

obj.save('speech.wav')