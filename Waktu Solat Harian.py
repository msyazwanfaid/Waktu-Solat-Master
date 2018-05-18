import math
import ephem
import datetime

#Penentuan Lintasan Arah Kiblat Harian
latitudkaabah = 21+25/60+21/3600
longitudkaabah = 39+49/60+34.32/3600

print("Masukkan Nama Tempat")
namatempat = str(input())
print("Masukkan Koordinate Tempat yang ingin Dikira Kiblatnya")

lokasi = ephem.Observer()
print("Masukkan Latitud (Utara = Positif, Selatan=Negatif)")
lokasi.lat = input()

print("Masukkan Longitud(Timur = Positif, Barat=Negatif)")
lokasi.long = input()

print("Masukkan Hari")
day = int(input())

print("Masukkan Bulan")
month = int(input())

print("Masukkan Tahun")
year = int(input ())
time = 0
print("Masukkan Time Zone")
tz = int(input())
tz1 = time - tz


#Pengiraan Time Zone#

if tz1 < 0:
    dtz = day - 1
    ttz = (24 + time) - tz

elif tz1 <= 24:
    ttz = time-tz
    dtz=day
else :
    dtz = day+1
    ttz = ((time-tz)-24)
#print('')
#print('Waktu UTC mengikut timezone %i adalah %i dan hari %i'% (tz,ttz,dtz))

#Pengiraan Tahun Lompat
x = year%4
if x == 0:
    k = 1
    dt = 366
else:
    k = 2
    dt = 365

#Pengiraan Hari dalam Setahun dan Nisbah Hari dalam setahun#
n =  round(((275*month)/9)-0.5) - k * round(((month+9)/12)-0.5) + dtz -30 - 1 + ttz/24
y1 = str(year+ (n/dt))
d = ephem.Date(y1)
lokasi.date=d
mata = ephem.Sun()

#Pengiraan Waktu Istiwa
n= lokasi.next_transit(mata)
o = float(n)
waktuistiwa =(o-int(o)-0.5)*24+tz
waktuistiwadegrees = int(waktuistiwa)
temp = 60 * (waktuistiwa - waktuistiwadegrees)
waktuistiwaminute = int(temp)
waktuistiwasaat = 60 * (temp - waktuistiwaminute)
waktuistiwa=waktuistiwa+0.0194

kualalumpur = ephem.Observer ()
kualalumpur.lon = lokasi.long
kualalumpur.lat = lokasi.lat
kualalumpur.date = lokasi.date
matahari = ephem.Sun()
matahari.compute (kualalumpur)
mataharidecpadaharikiraan= float(math.degrees(matahari.dec))

lokasi.date = lokasi.date+ephem.hour*24
ualalumpur = ephem.Observer ()
kualalumpur.lon = lokasi.long
kualalumpur.lat = lokasi.lat
kualalumpur.date = lokasi.date
matahari = ephem.Sun()
matahari.compute (kualalumpur)
mataharidecpadakeesokkanharikiraan = float(math.degrees(matahari.dec))

lokasi.date = lokasi.date-ephem.hour*24
kualalumpurlat = float(math.degrees(kualalumpur.lat))
kualalumpurlon = float(math.degrees(kualalumpur.lon))
i = (16.5/24)*((mataharidecpadakeesokkanharikiraan)-(mataharidecpadaharikiraan))
decmatahariwaktuasar = (mataharidecpadaharikiraan)+ i

#Jarak zenit Za#
q = (kualalumpurlat)-(decmatahariwaktuasar)
r = abs (q)
s = math.tan(math.radians(r))
t = 1+s
u = math.degrees(math.atan(t))


#Sudut Waktu Matahari Awal Waktu Asar Ta#
v = math.cos(math.radians(u))
w = math.sin(math.radians(decmatahariwaktuasar))
x = math.sin(math.radians(kualalumpurlat))
y = math.cos(math.radians(decmatahariwaktuasar))
z = math.cos(math.radians(kualalumpurlat))
j = (v-w*x)/y*z
k = math.degrees(math.acos(j))
sudutwaktumatahari = k/15
waktuasar = waktuistiwa+sudutwaktumatahari


ghaisDj = int(abs(waktuistiwa))
ghaisDm = int((abs(waktuistiwa)%1)*60)
ghaisDs = (((abs(waktuistiwa)%1)*60)%1)*60
#print (waktuasar,ghaisDj,ghaisDm,ghaisDs)
ghaisDs = int(ghaisDs)
ghaisDs = int(ghaisDs)

t = datetime.time(ghaisDj,ghaisDm,ghaisDs)
print (kualalumpur.date)
print ("waktu zuhur adalah %s"%t)
ghaisDj = int(abs(waktuasar))
ghaisDm = int((abs(waktuasar)%1)*60)
ghaisDs = (((abs(waktuasar)%1)*60)%1)*60
#print (waktuasar,ghaisDj,ghaisDm,ghaisDs)
ghaisDs = int(ghaisDs)
ghaisDs = int(ghaisDs)
print(waktuasar)
t = datetime.time(ghaisDj,ghaisDm,ghaisDs)
print ("waktu asar adalah %s"%t)