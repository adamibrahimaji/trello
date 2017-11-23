import random

def main():
    print('Permainan Tebak Angka 1 - 50')
    #angka = 45
    angka = random.randint(1,50)
    skor = 100 
    
    ketemu = False
    while not ketemu:
        x = raw_input('Masukan Angka : ')
        x = int(x)
        
        if x == angka:
            print('Tebakan Mu Benar')
            ketemu = True
        elif x > angka:
            print('Angka terlalu besar')
            skor -= 5
        elif x < angka:
            print('Angka terlalu kecil')
            skor -= 10

    print("Skor Anda : ",skor)

main()
    
    
