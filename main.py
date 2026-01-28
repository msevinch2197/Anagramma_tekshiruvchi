def anagramma_tekshir(soz1, soz2):
     
    soz1 = soz1.lower()
    soz2 = soz2.lower()
    
     
    if sorted(soz1) == sorted(soz2):
        return True
    else:
        return False

soz1 = input("Birinchi so'zni kiriting: ")
soz2 = input("Ikkinchi so'zni kiriting: ")

if anagramma_tekshir(soz1, soz2):
    print("Bu so'zlar ANAGRAMMA.")
else:
    print("Bu so'zlar anagramma EMAS.")
