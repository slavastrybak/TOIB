import requests
import hashlib


with open(r'ВВЕСТИ СЮДА ПУТЬ ФАЙЛА АЛЯ C:\Users\Admin\Desktop\file1', 'r') as file: # Считать файл с именами пользователей и паролем
    for line in file:
        usrname, password = line.strip().split(',') # Разделить строку на имя_пользователя,пароль
        password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # Схэшировать пароль по SHA-1

        response = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}") # Запросить у API HIBP проверку использования пароля

        if response.status_code == 200: # Проверить статус ответа, если 200 - пароль был слит
            hashes = [line.split(':') for line in response.text.splitlines()] # Получить список хэшей паролей которые начинаются на 5 символов также как и пароль из файла
            for h, count in hashes: # Проверить есть ли хэш пароля из файла в одном из слитых
                if password_hash[5:] == h:
                    print(f"Пароль для пользователя {usrname} был использован {count} раз.")
                    break
        else:
            print(f"Не удалось проверить пароль для пользователя {usrname}.")