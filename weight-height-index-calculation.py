#Kişinin ad, kilo ve boy bilgilerini alarak kilo indekslerini hesaplama 

name = input('Adınız: ')
kg = float(input('Kilonuz: '))
boy = float(input('Boyunuz: '))

index = (kg/(boy**2))

zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.5) and (index <= 24.9)
kilolu = (index >= 25.0) and (index <= 29.9)
obez = (index >= 30.0) and (index <= 34.9)


print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}')



