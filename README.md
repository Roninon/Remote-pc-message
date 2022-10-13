# Установка

1. Скачать репозиторий, перейти в папку репозитория
2. Создать виртуальное окружение:
   
   
   `py -m venv venv`
   
   `cd venv/Scripts`

   `activate`

   Убедитесь что в консоли появилось `(venv)` в начале строки
   
   `cd ../..`

3. Установить зависимости из файла
   
   `pip install -r requirements.txt`

4. Перейти в [BotFather](https://t.me/botfather) и создать бота с сложным для подбора никнеймом, например `unic_9137_oecm_bot`
5. Затем скопировать API token бота
6. Поменять значение переменной API_TOKEN вставив свой токен
7. Запустить установку exe файла

  `pyinstaller -F --noconsole -n "Name of your app" -i default_image.ico msg_bot.py`

8. Добавить программу в автозапуск windows 

`Win + R` => `shell:startup`

положить сюда ярлык вашей программы

# Готово!
