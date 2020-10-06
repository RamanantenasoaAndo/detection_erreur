#mot = input("entre un mot:")
# arr = bytearray (mot,'utf-8')
# c = bin (arr).strip('utf-8')
# for i in c:
#	if(c.count("1")%2 == 0):
#		c = "0"+c
#		print(c)
#	else:
#		c = "1"+c
#		print(c)

def pair(a):
    for i in a:
        c = bin(i).strip("0b")
        if (c.count("1") % 2 == 0):

            bit = "0"+ c
            byte_arr = bytearray(bit, "utf-8")
        else:
            bit = "1" + c
            byte_arr = bytearray(bit, "utf-8")
    print(byte_arr)

def impair(a):
    for i in a:
        c = bin(i).strip("0b")
        if (c.count("1") % 2 == 0):
            bit = "1" + c
            byte_arr = bytearray(bit, "utf-8")
        else:
            bit = "0" + c
            byte_arr = bytearray(bit, "utf-8")
    print(byte_arr)

#main
arr = input("Entrer un message: ")
a = bytearray(arr, "utf-8")
print("resultat en bytearray:")
pair(a)
print("bitarray pair:")
impair(a)
print("bitarray impair: ")

