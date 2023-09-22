from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "/Users/adsl/PycharmProjects/pythonProject/yandexdriver"
yandex_binary_path = "/Applications/Yandex.app/Contents/MacOS/Yandex"

service = Service(executable_path=chrome_driver_path)
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = yandex_binary_path
driver = webdriver.Chrome(service=service, options=chromeOptions)

# Неявное ожидание 10 секунд
driver.implicitly_wait(10)

try:
    # Открываем страницу Petfriends
    driver.get("https://petfriends.skillfactory.ru/login")

    # Находим поле для ввода email и вводим почту
    email_field = driver.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys("DSIK@DSIK.ru") #ВСТАВЛЯЕМ СВОЮ ПОЧТУ 

    # Находим поле для ввода пароля и вводим пароль
    password_field = driver.find_element(By.ID, "pass")
    password_field.clear()
    password_field.send_keys("DSIK") #ВСТАВЛЯЕМ СВОЙ ПАРОЛЬ

    # Нажимаем кнопку "Войти"
    login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-success[type='submit']")
    login_button.click()

    # Открываем страницу "Мои питомцы"
    driver.get('https://petfriends.skillfactory.ru/my_pets')

    # Ищем список питомцев
    table = driver.find_element(By.ID, "all_my_pets")

    # Получаем все строки таблицы
    rows = table.find_elements(By.TAG_NAME, "tr")

    has_photo_count = 0  # Счетчик питомцев с фото
    total_pets = len(rows) - 1  # Общее количество питомцев, за вычетом заголовка

    valid_pets_count = 0  # Счетчик питомцев с полной информацией

    pet_info_set = {}  # Словарь для хранения комбинаций имени, породы и возраста и их количества

    pet_names = []  # Массив для хранения имен питомцев

    for row in rows[1:]:  # Пропускаем первую строку, так как там заголовки столбцов
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) >= 4:
            pet_name = columns[0].text
            pet_names.append(pet_name)  # Добавляем имя питомца в массив

            pet_type = columns[1].text
            pet_age = columns[2].text

            # Проверяем атрибут src элемента img с использованием ожидания
            img_element = WebDriverWait(row, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
            img_src = img_element.get_attribute("src")

            # Проверяем, есть ли у питомца фото
            has_photo = bool(img_src.strip())  # Проверка на пустую строку

            # Проверяем, что у питомца есть имя, порода и возраст
            if pet_name and pet_type and pet_age:
                valid_pets_count += 1

            # Проверяем, что комбинация имени, породы и возраста уникальна
            pet_info = (pet_name, pet_type, pet_age)
            if pet_info in pet_info_set:
                pet_info_set[pet_info] += 1
            else:
                pet_info_set[pet_info] = 1

            # Увеличиваем счетчик, если у питомца есть фото
            if has_photo:
                has_photo_count += 1

    # Сравниваем количество питомцев в статистике с количеством в списке (total_pets)
    if total_pets == len(pet_names):
        print("Присутствуют все питомцы.")
    else:
        print("Присутствуют не все питомцы.")

    # Проверяем, что у более чем половины питомцев есть фото
    if has_photo_count > total_pets / 2:
        print("У более чем половины питомцев есть фото.")
    else:
        print("У менее чем половины питомцев есть фото.")

    # Проверяем, что у всех питомцев есть имя, порода и возраст
    if valid_pets_count == total_pets:
        print("У всех питомцев есть имя, порода и возраст.")
    else:
        print("Не у всех питомцев есть имя, порода и возраст.")

    # Проверяем, что все имена питомцев разные
    if len(set(pet_names)) == total_pets:
        print("У всех питомцев разные имена.")
    else:
        print("У некоторых питомцев совпадают имена.")

    # Проверяем, что в списке есть повторяющиеся питомцы
    if any(count > 1 for count in pet_info_set.values()):
        print("В списке есть повторяющиеся питомцы:", end=" ")

        # Создаем список для хранения повторяющихся имен
        duplicate_names = []

        for pet_info, count in pet_info_set.items():
            if count > 1:
                duplicate_names.append(pet_info[0])

        # Выводим повторяющиеся имена через запятую
        print(", ".join(duplicate_names))
    else:
        print("В списке нет повторяющихся питомцев.")


except Exception as e:
    # Обрабатываем исключение и выводим сообщение об ошибке
    print("Произошла ошибка:", str(e))

finally:
    driver.quit()
