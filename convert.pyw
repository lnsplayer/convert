from tkinter import *
from pytube import YouTube
import moviepy.editor as mp
import os

# Создание окна
root = Tk()
root.title("lns's convert")

# Создание поля для ввода ссылки на видео
link_label = Label(root, text="Введите ссылку на видео из YouTube:")
link_label.pack()
link_entry = Entry(root, width=50)
link_entry.pack()

# Создание поля для ввода пути сохранения файла
path_label = Label(root, text="Введите путь для сохранения файла:")
path_label.pack()
path_entry = Entry(root, width=50)
path_entry.pack()

# Глобальная переменная для хранения пути установки
install_path = ""

# Функция для скачивания и конвертации видео в mp3
def download():
    # Получение ссылки на видео из поля ввода
    video_url = link_entry.get()

    # Создание объекта YouTube
    yt = YouTube(video_url)

    # Получение объекта с аудио потоком
    audio_stream = yt.streams.filter(only_audio=True).first()

    # Получение пути сохранения файла из поля ввода
    save_path = path_entry.get()

    # Запоминание пути установки
    global install_path
    install_path = save_path

    # Скачивание аудио файла
    audio_stream.download(output_path=save_path)

    # Конвертация в mp3
    video_title = yt.title
    file_name = video_title + ".mp4"
    clip = mp.AudioFileClip(save_path + "/" + file_name)
    clip.write_audiofile(save_path + "/" + video_title + ".mp3")

    # Удаление исходного файла
    os.remove(save_path + "/" + file_name)

    # Вывод сообщения об успешном сохранении файла
    success_label = Label(root, text="Файл успешно сохранен в " + save_path + "/" + video_title + ".mp3")
    success_label.pack()

# Создание кнопки для запуска скачивания
download_button = Button(root, text="Скачать", command=download)
download_button.pack()

# Запуск главного цикла окна
root.mainloop()

# Вывод пути установки
print("Путь установки: " + install_path)