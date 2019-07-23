#coding=utf8


import parshtml

name = "a.html"
name2 = "laminad.html"


def main():

    print("main pars")
    # parshtml.page2(name)
    # parshtml.page_h(name2)
    # parshtml.page_mod
    # parshtml.page_mod(name2, "catalog")

    # берет див и записывает его содержимое в файл
    parshtml.page_mod(name2, "top_menu")
#     читае файл и парсет ссылки и текст и записывает в вайл link.txt
    parshtml.pars_link("out.txt")

# строка комента

# парсив адреса страниц
#     имя
#     адрес
# тарсим каждую страницу
#     ссылку на картинку
if __name__ == '__main__':
    main()

