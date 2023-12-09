import filters
from PIL import Image
filters = {
    1: filters.InversionFilter,
    2: filters.MirrorFilter,
    3: filters.BlurFilter
}

print("Введите путь к файлу:")
path = input()
img = Image.open(path) # img - наша картинка
img.show()
while True:
    print('''Меню фильтров:
    1 - Inversion Filter
    2 - Mirror Filter
    3 - BLur Filter
    0 - Выход
    Выберите фильтр (или 0 для выхода):''')
    filtNum = input()
    if filtNum == "0":
        print("А пока.. Пока!")
        exit(0)
    elif filtNum == "1" or filtNum == "2" or filtNum == "3":
        filtNum = int(filtNum)
        filt = filters[filtNum]()
        print(filt.description)
        while True:
            print("Применить фильтр к текущему изображению? Да / Нет")
            word = input().lower()
            if word == "нет":
                print("Ваше изображение")
                break
            elif word == "да":
                img = filt.transform(img)
                print("Куда сохранить изображение?")
                save = input()
                img.save(save)
                break
            else:
                print("ОТВЕТЬ ДА ИЛИ НЕТ")
    else:
        print("введите корректный номер фильотра")