from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

search = input("Что ищем? ")

browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(search, Keys.ENTER)

while True:
    print("\n1. Листать параграфы текущей статьи")
    print("2. Перейти на одну из связанных страниц")
    print("3. Выйти из программы")
    choice = input("Выберите действие: ")

    if choice == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        # Для перебора пишем цикл
        for paragraph in paragraphs:
            print(paragraph.text)
            input()

    elif choice == "2":
        links = browser.find_elements(By.CSS_SELECTOR, "a")
        for i, link in enumerate(links):
            print(f"{i + 1}. {link.text}")
        link_index = int(input("Введите номер ссылки: ")) - 1
        link = links[link_index]
        browser.get(link.get_attribute("href"))

        while True:
            print("\n1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из внутренних статей")
            print("3. Вернуться на предыдущую страницу")
            choice = input("Выберите действие: ")

            if choice == "1":
                paragraphs = browser.find_elements(By.CSS_SELECTOR, "p")
                for paragraph in paragraphs:
                    print(paragraph.text)

            elif choice == "2":
                links = browser.find_elements(By.CSS_SELECTOR, "a")
                for i, link in enumerate(links):
                    print(f"{i + 1}. {link.text}")
                link_index = int(input("Введите номер ссылки: ")) - 1
                link = links[link_index]
                browser.get(link.get_attribute("href"))

            elif choice == "3":
                browser.back()
                break

    elif choice == "3":
        break

browser.quit()