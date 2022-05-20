file = open('sample_dna.txt', 'r')
dna = file.read()

print( "Cadena de ADN: ", dna)

print( "Cantidad de C (citosina): ", dna.count("C"))
print( "Cantidad de G (guanina): ", dna.count("G"))

# mi codigo
c = 0
g = 0
for nucleobase in dna:
    if nucleobase == "C": c+=1
    if nucleobase == "G": g+=1


print( "Cantidad de C (citosina): ", c)
print( "Cantidad de G (guanina): ", g)
