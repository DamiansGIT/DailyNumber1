
def szukanie_sumy(tablica, zadana_suma):

    bool_p = False
    nowa_tablica = []
    for i in range(len(tablica) - 1):
        temporary = str( int(zadana_suma) - int(tablica[i]) )
        nowa_tablica.append(temporary)
        for j in range(len(nowa_tablica)):

           # print('tablica[i+1]: ' + str(tablica[i+1]) + ',  nowa_tablica[j] ' + str(nowa_tablica[j]))

            if str(tablica[i+1]) == nowa_tablica[j]:
                bool_p = True
        if bool_p is True:
            break

        #print(bool_p)
    #print(bool_p)

    return bool_p
