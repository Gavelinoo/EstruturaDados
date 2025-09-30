# # iterando sobre range
#
# for i in range(5):
#     print(i)
#
# # iterando sobre string
#
#
#
# for i in "Python":
#     print(i)

# #iterando com enumrate
# frutas = ["maçã","banana","laranja"]
# for indice, fruta in enumerate(frutas):
#     print(f"{indice}: {fruta}")


# Loop com continue
# for num in range(10):
#     if num % 2 != 0:
#         continue
#     print(num)


# Usando for com if

print("Números pares (for com if) :")
for numero in range(1,21):
    if numero % 2 == 0:
        print(numero, end=" ")
