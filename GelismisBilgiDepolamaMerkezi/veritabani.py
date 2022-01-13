import pymysql.cursors

class Veritabani:

    def baglan(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='Medcezir44.',
                             db='depolama',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        baglanti = db.cursor()
        return baglanti, db

    def yaz(self, yazar, kitap):
        conn, db = self.baglan()
        sonuc = conn.execute('INSERT INTO Depo VALUES(%s, %s)', (yazar, kitap))
        db.commit()

        print(str(sonuc) + 'yazar ve kitap eklendi')

    def oku(self):
        conn, db = self.baglan()
        conn.execute('SELECT * FROM Depo')
        veri = conn.fetchall()
        for i in veri:
            print(i)