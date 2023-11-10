import datetime

tarih = input('Aracınız hangi tarihte trafiğe çıktı: ')
tarih = tarih.split('/')
trafiğeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafiğeCikis
days = fark.days


if days <= 365:
    print('1. Servis Aralığı')
elif days > 365 and days < 365*2:
    print('2. Servis Aralığı')
elif days> 365*2 and days < 365*3:
    print('3. Servis Aralığı')
else:
    print('Hatalı süre')
