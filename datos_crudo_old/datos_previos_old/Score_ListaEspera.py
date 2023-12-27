def puntosListaEspera(lista_espera):
    score = 0
    if lista_espera == True:
        score += 175

    return score


print(puntosListaEspera(True))


# #     elif not viajes_2022 and not viajes_2023:
#         score += 50
#     elif not viajes_2022 and viajes_2023:
#         score += 40
#     elif viajes_2022 and not viajes_2023:
#         score += 20
#     elif viajes_2022 and viajes_2023:
#         if viajes_2022 + viajes_2023 > 2:
#             score += 0
#         else:
#             score += 10