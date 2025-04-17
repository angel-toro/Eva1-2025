
protocolo = input("Ingrese el nombre del protocolo (OSPF,EIGRP,BGP): ")
if protocolo == "OSPF":
    print("La distancia administrativa de OSPF es 110")
elif protocolo == "EIGRP":
    print("La distancia administrativa de EIGRP es 90")
elif protocolo == "BGP":
    print("La distancia administrativa de BGP es 20")
else:
    print("Protocolo no reconocido")
