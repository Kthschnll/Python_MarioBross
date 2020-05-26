# Vorlage Kommentar

"""
	date:
	    - 25.05.2020
	desc:
	    - dieses skript ist beinahlten Sachen aus dem Unterrricht die für spätere Funktionen eventuell hilfreich sein können
	param:
        - nothing
    return:
        - nothing
	to_do:
	    - helpful_code  vor Abgabe löschen
"""

# Datenbanken Stunde 02
# Datenverarbeitung mit Data Frames Stunde 03

var_1 = [] #array
var_2 = () #tuple: wenn ich mehrere parameter übergeben mochte arbeite ich mit nicht veränderliche liste
var_3 = {} #dictionary
dc_variable = {"mein_key":42, "mein_key2":[1,2,3,4, "test"]}

# import statistica as s -> dann überall statistics. durch s. ersetzen
# from statistics import mean -> wir wollen nur die Funktion mean importieren

# für highscore: write, append, read files

meinText = 'hallo'
saveFile = open('test.txt', 'w') # w für write, alles andere was in der datei ist wird gelöscht
saveFile.write(meinText)
saveFile.close()

meinText = '\nnomon'
saveFile = open('test.txt', 'a') # a für append es wird der meintext an letzten buchstaben angehängt
saveFile.write(meinText)
saveFile.close()

readme = open("test.txt", "r").read()
print(readme)


    # text splitten
splitme = readme.split('o') #splittet an der stelle wo ein o oder z.B. \n steht, splitme ist ein array
print(splitme)
print(splitme[2])

    #lists operations
x = [2,3,4,5,2,6,71,2,3]
print (x)
x.append(4) # hintenanhängen
print(x)
x.insert(5,66) # an Pos [5] 66 einfügen
print(x)
x.remove(3) # pos[3] löschen
print(x)
print(x.index(4)) # [] wo 4 das erste mal
print(x.count(2)) # wie viele zweier
x.sort() #aufwärts sortieren
print(x)


    #dictionarys
# haben einen eindeutigen schlüssel
grade_test = {'Daniel': 89, 'Theo': [7,90], 'Jack':90}
print(grade_test)
print(grade_test['Daniel'])
print(grade_test['Theo'][1])
grade_test['Theo'][0] = 100 #wert ändern wenn theo (7,80) also ein tupel wäre es nicht möglich
grade_test['Daniel'] = 100 #wert ändern
grade_test['Jessica'] = 0 #neuen key anlegen
grade_test['Jessi'] = [0,90] #neuen key anlegen, ohne klammern wäre es ein tupel und somit nicht veränderbar
del grade_test['Jack'] #key mit wert löschen
print(grade_test)