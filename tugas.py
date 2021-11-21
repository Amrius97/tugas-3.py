JumlahAyam = float(input("Masukan Nilai"))

if ( JumlahAyam >= 1900 and JumlahAyam <= 2000 ) : 
    print ("Untung besar")
elif ( JumlahAyam >= 1500 and JumlahAyam < 1899 ) :
    print ("Untung sedikit")
elif ( JumlahAyam >= 1000 and JumlahAyam < 1499 ) :
    print ("Rugi sedikit")
elif ( JumlahAyam >= 500 and JumlahAyam < 999 ) :
    print ("Rugi banyak")
elif ( JumlahAyam > 1 and JumlahAyam < 499 ) :
    print ("Siap-siap suntik dana")
elif ( JumlahAyam <= 0 ) :
    print ("Bangkrut")
else : 
    print ("Nilai tidak diketahui")
