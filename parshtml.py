#coding=utf8
from bs4 import BeautifulSoup
import re

# строка комента
# http://www.santrade.by/catalog/laminat/

# with open("laminad.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#
# link = soup.find_all('div', {"class": 'image'}, 'a')
# for im in link:
#     print(im.img)
#
#
# link2 = soup.find_all('div', {"class": 'title'}, 'a')
# print('-'*80)
# for d in link2:
#     text = d.get_text()
#     lin = d.a
#     allText = text+lin.get('href')
#     print("T: %s "%allText )


# http://www.santrade.by/catalog/laminat/


def page_h(name):
    print(name)

    try:
        file = open(name, "r")
    except IOError:
        print("Error! not open file!")
    else:

        with file as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            link2 = soup.find_all('div', {"class": 'title'}, 'a')
            print("Дериктория {} успешно создана".format(name))
    # print(link2)
            print('-' * 80)
            for d in link2:
                text = d.get_text()
                lin = d.a
                all_text = text + " - " + lin.get('href')
                print("page_h: %s " % all_text)

def page_mod(name_file, clasname):
    print(name_file)
    clas = clasname

    try:
        file = open(name_file, "r")
    except IOError:
        print("Error! not open file!")
    else:
        hfile = open("out.txt", 'w')

        with file as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            # link2 = soup.find('div', {"class": clas}, 'a')
            link2 = soup.find('div', {"class": clas}, 'a')
            # link2 = soup.find('div', {"class": clas}).find('a').get('href')
            #
            # print("Дериктория {} успешно создана".format(name_file))
            # a_tag = soup.next_sibling
            # cont = a_tag
            # print("Cont: %s" % cont )
            # print("link2: %s" % link2 )
            # print("link2 count: %d" % len(link2))



            # lin_text = soup.find('div', {"class": clas}).find('a').text
            # print("Lin text: %s" % lin_text)
            #
            # link3 = soup.find_all('a')
            # for ll in link3:
            #     print(ll.get('href'))
            #     print(ll.get_text())


            # print(link3.get_text())
            # print(link3.get('href'))
            # print(link2.get('href'))

            # for d in link2:
                # text = d.re.get_text
            for i in range(19):
                i = i + 2
                hfile.writelines(" %s" %link2.contents[i])
                # print('-' * 80)
                # print(d.get('href'))

                # print(d)
        hfile.close()

def pars_link(fname):
    hf = open(fname, 'r')
    hfout = open("link.txt", 'w')
    con = []
    i = 0

    with hf as str:
    # for str in hf:
    #     print(str)
        sp = BeautifulSoup(str, 'html.parser')
        conten = sp.find_all(re.compile('a'))
        for j in conten:
            # print(j.get_text() + " " + j.get('href'))
            t2 = j.get_text().strip()
            # aa = re.split(' +', t2)
            t2 = t2 + " \n"
            t = j.get('href')
            all = t+ " " + t2

            # hfout.writelines(t + " ")
            print("")
            hfout.write(all.encode('utf-8'))
            # hfout.writelines(all+"\n")
            # con.append(all+"\n")
            # print("")

            # print(j.get('href'))
            # print(j.get_text())
        # for jb in con:
            # tt = jb.get_text()
            # jb.strip()
            #  print(jb)
        print(con)

            # hfout.write(jb)
        # hfout.writelines(con)
            #
            # a = re.split(' +', tt) # стр.417
            # tar = a[:1]
            # print("%s"%tar)
        hf.close()
        # for so in con:
        #     i = i+1
        #     text = so
        #     print(" %s"%text)
        #     print(so)

            # hfout.write(text)
        hfout.close()

# a.html
def page2(name):

    fname = name
    print(fname)

    try:
        hfile = open(fname, "r")

    except IOError:
        print("Error! not open file!")
    else:
        with hfile as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            link2 = soup.find_all('a', {"class": 'fancybox'})
            # link2 = soup.find_all('div', {"class": 'right-coll'}, 'a', {"class": 'fancybox'})
            print("Файл {} успешно открыт".format(name))
            print(link2)
            print('-' * 80)
            for d in link2:
                text = d.get_text()
                print(text)
                lin = d.a
                # allText = text + " - " + lin.get('href')
                print("page1: %s " %d.get('href'))
# for link in soup.find_all('div', {"class": 'catalog-item'}):
#     print(link)



#   print(" {} {}".format(link.get_text(), link.get('href')))
#print(soup.prettify())
def main():
    # pname = "a.html"
    pname = "laminad.html"
    page2(pname)

if __name__ == '__main__':
    main()