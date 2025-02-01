# Создаем словарь соответствия кириллицы к латинице
trans_table = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "jo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "j",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "shh",
    "ъ": "*",
    "ы": "y",
    "ь": "'",
    "э": "je",
    "ю": "ju",
    "я": "ya",
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "Jo",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "J",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "H",
    "Ц": "C",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shh",
    "Ъ": "*",
    "Ы": "Y",
    "Ь": "'",
    "Э": "Je",
    "Ю": "Ju",
    "Я": "Ya",
}


# Функция для создания таблицы перевода (для str.translate)
def create_trans_table():
    return str.maketrans(trans_table)


# Чтение исходного файла
with open("cyrillic.txt", mode="r", encoding="utf-8") as file_in:
    text = file_in.read()

# Транслитерация текста
translated_text = text.translate(create_trans_table())

# Запись результата в новый файл
with open("transliteration.txt", mode="w", encoding="utf-8") as file_out:
    file_out.write(translated_text)
