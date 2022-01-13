from veritabani import Veritabani
from GoruntuIsleme import GoruntuIsleme


if __name__ == '__main__':
    vb = Veritabani()
    gi = GoruntuIsleme()

    print('Yazar adını gösterin')
    author = gi.goruntuOku()
    input()
    print('Kitap adını gösterin')
    kitap = gi.goruntuOku()
    print('Yazar : ', author)
    print('Kitap : ', kitap)
    vb.yaz(author, kitap)
    vb.oku()
