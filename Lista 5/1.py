def slowaNaLiczby(liczba):
    j={"jeden":1, "dwa":2,"trzy":3,"cztery":4,"pięć":5,"sześć":6,"siedem":7,"osiem":8,"dziewięć":9,"dziesięć":10,"jedenaście":11,"dwanaście":12,"trzynaście":13,"czternaście":14,"pietnaście":15,"szesnaście":16,"siedemnaście":17,"osiemnaście":18,"dziewietnaście":19,"dwadzieścia":20,"trzydzieści":30,"czterdzieści":40,"pięćdziesiąt":50}
    f=int(0)
    liczba1=liczba.split(" ")
    inti=int(0)
    for x in liczba1:
        inti+=int(j[x])
        
    return inti
print("zapodaj liczbę")
liczba=input()
print(slowaNaLiczby(liczba))
