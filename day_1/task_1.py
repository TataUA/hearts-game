from typing import Dict
from collections import Counter


def probability_simbols(text: str) -> Dict:
    """
    Функція 'probability_simbols' розраховує вірогідність зустрічі кожного символу в рядку.
    Параметри:
        text (str): вхідний рядок для якого потрібно підрахувати вірогідність зустрічі символів.
    Повертає:
        dict: словник, ключами якого є символи, а значеннями-вірогідність зустріти ці символи.
    """

    # Підрахуємо частоту зустрічі однакових символів у рядку за доп. класу 'Counter' модуля 'collections'
    simbols_counter = Counter(text)

    # Знайдемо довжину рядку
    text_length: int = len(text)

    # Визначаємо вірогідність зустрічі символу та записуємо до словника
    simbols_dict: Dict[str, float] = {
        simbol_key: round(count / text_length * 100, 2)
        for simbol_key, count in simbols_counter.items()
    }
    return simbols_dict


if __name__ == "__main__":
    string = "Hello World!"
    print(probability_simbols(string))
