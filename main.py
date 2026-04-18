#1
def konvert(miqdor, kurs=1.0):
    return miqdor * kurs

#2
def daraja(ism, ball=0):
    if ball < 50:
        level = "Boshlovchi"
    elif ball < 80:
        level = "O‘rta"
    else:
        level = "Professional"
    
    return f"{ism}: {level}"

#3
def takrorla(matn, soni, ajratuvchi=", "):
    return ajratuvchi.join([matn] * soni)

#4
def sana(kun, oy, yil=2025):
    return f"{kun:02d}.{oy:02d}.{yil}"

#5
import string

def parol_kuch(parol):
    uzunlik = len(parol) >= 8
    harf = any(c.isalpha() for c in parol)
    raqam = any(c.isdigit() for c in parol)
    belgi = any(c in string.punctuation for c in parol)

    score = sum([uzunlik, harf, raqam, belgi])

    if score <= 2:
        return "Zaif"
    elif score == 3:
        return "O‘rta"
    else:
        return "Kuchli"
