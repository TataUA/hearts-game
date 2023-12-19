#️Домашнє завдання:
# написати функцію якам приймає рядок і повертає словник у якому
# ключами є всі символи, які зустрічаються в цьому рядку, а значення - відповідні вірогідності зустріти цей символ в цьому рядку.
# код повинен бути структурований за допомогою конструкції if name == "main":,
# всі аргументи і значення що функція повертає повинні бути типізовані, функція має рядок документації


from typing import Dict
from collections import Counter

def probability_simbols (text: str) -> Dict:
    """
    Функція 'probability_simbols' розраховує вірогідність зустрічі кожного символу в рядку.
    Параметри:
        text (str): вхідний рядок для якого потрібно підрахувати вірогідність зустрічі символів.
    Повертає:
        dict: словник, ключами якого є символи, а значеннями-вірогідність зустріти ці символи.
    """

    #Підрахуємо частоту зустрічі однакових символів у рядку за доп. класу 'Counter' модуля 'collections'
    simbols_counter = Counter(text)

    #Знайдемо довжину рядку
    text_length: int = len(text)

    #Визначаємо вірогідність зустрічі символу та записуємо до словника
    simbols_dict: Dict[str, float] = {simbol_key: round(text.count(simbol_key) / text_length * 100, 2) for simbol_key in set(text)}
#або
    simbols_dict2: Dict[str, float] = {simbol_key: round(count / text_length * 100, 2) for simbol_key, count in simbols_counter.items()}
    return (simbols_dict, simbols_dict2)

if __name__ == "__main__":
    string = "Hello World!"
    print(probability_simbols(string))


# за допомогою тернарного оператора релізувати логіку:
# є параметри x та у,
# якщо x < y - друкуємо x + y,
# якщо x == y - друкуємо 0,
# якщо x > y - друкуємо x - y,
# якщо x == 0 та y == 0 друкуємо "game over

x = 0
y = 0

result = "game over" if x == 0 and y == 0 else (0 if x == y else (x + y if x < y else x - y))

print(result)
