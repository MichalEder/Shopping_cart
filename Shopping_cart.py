
# Zadané hodnoty
kosik = dict()
oddelovac = '=' * 40
potraviny = {
    'mleko': [30, 5],  # index '0'-> cena, index '1' -> pocet
    'maso': [100, 1],
    'banan': [30, 10],
    'jogurt': [10, 5],
    'chleb': [20, 5],
    'jablko': [10, 10],
    'pomeranc': [15, 10]
}
nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomenrac  |    15,-  |
+-----------+----------+
"""

print('Vítejte u našeho nákupního košíku!',
    oddelovac, 
    nabidka,
    'Pro ukonceni ńakupu zadejte "KONEC"',
    sep='\n')

while (vybrane_zbozi := input('Vyberte zbozi z nabidky: ')) != 'KONEC':
    if vybrane_zbozi not in potraviny:
        print('Toto zbozi neni v nabidce!')
    elif potraviny[vybrane_zbozi][1] == 0:
        print(f'Zbozi {vybrane_zbozi} jiz neni skladem')
    elif vybrane_zbozi not in kosik and potraviny[vybrane_zbozi][1] > 0:
        potraviny[vybrane_zbozi][1] -= 1
        kosik[vybrane_zbozi] = [potraviny[vybrane_zbozi], 1]
        print(f'Zbozi {vybrane_zbozi} bylo pridano do kosiku!')
    elif vybrane_zbozi in kosik and potraviny[vybrane_zbozi][1] > 0:
        potraviny[vybrane_zbozi][1] -= 1
        kosik[vybrane_zbozi][1] += 1
        print(f'Zbozi {vybrane_zbozi} bylo pridano do kosiku!')

print(kosik)
