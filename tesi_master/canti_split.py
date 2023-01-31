import re

def main():
    # ## 1. Inferno
    # # Open file
    # with open ("/Users/tessacattaneo/Desktop/tesi_master/If.txt", "r") as If:
    #     Inferno = If.read()

    # # Split main file into each canto
    # canti = re.split('canto\s[ivx]+\n', Inferno)

    # # Creating a file for each individual canto
    # for item in canti:
    #     index = str((canti.index(item)))
    #     if index == '1' or index == '2' or index == '3' or index == '4' or index == '5' or index == '6' or index == '7' or index == '8' or index == '9':
    #         filepath = '/Users/tessacattaneo/Desktop/tesi_master/Inferno/0'+index+'_If.txt'
    #     else:
    #         filepath = '/Users/tessacattaneo/Desktop/tesi_master/Inferno/'+index+'_If.txt'
    #     if len(item) != 0:
    #         with open (filepath, 'w') as a:
    #             a.write(item)

    # ## 2. Purgatorio
    # # Open file
    # with open ("/Users/tessacattaneo/Desktop/tesi_master/Pd.txt", "r") as Pg:
    #     Purgatorio = Pg.read()

    # # Split main file into each canto
    # canti = re.split('canto\s[ivx]+\n', Purgatorio)

    # # Creating a file for each individual canto
    # for item in canti:
    #     index = str((canti.index(item)))
    #     if index == '1' or index == '2' or index == '3' or index == '4' or index == '5' or index == '6' or index == '7' or index == '8' or index == '9':
    #         filepath = '/Users/tessacattaneo/Desktop/tesi_master/Purgatorio/0'+index+'_Pg.txt'
    #     else:
    #         filepath = '/Users/tessacattaneo/Desktop/tesi_master/Purgatorio/'+index+'_Pg.txt'
    #     if len(item) != 0:
    #         with open (filepath, 'w') as a:
    #             a.write(item)
    
    # ## 3. Paradiso
    # # Open file
    # with open ("/Users/tessacattaneo/Desktop/tesi_master/Pd.txt", "r") as Pd:
    #     Paradiso = Pd.read()

    # # Split main file into each canto
    # canti = re.split('canto\s[ivx]+\n', Paradiso)

    # # Creating a file for each individual canto
    # for item in canti:
    #     index = str((canti.index(item)))
    #     if index == '1' or index == '2' or index == '3' or index == '4' or index == '5' or index == '6' or index == '7' or index == '8' or index == '9':
    #         filepath = '/Users/tessacattaneo/Desktop/tesi_master/Paradiso/0'+index+'_Pd.txt'
    #     else:
    #         filepath = '/Users/tessacattaneo/Desktop/tesi_master/Paradiso/'+index+'_Pd.txt'
    #     if len(item) != 0:
    #         with open (filepath, 'w') as a:
    #             a.write(item)

    ## 4. Orlando Furioso
    with open ("/Users/tessacattaneo/Desktop/tesi_master/orlando_furioso.txt", "r") as OF:
        Orlando_furioso = OF.read()

    # Split main file into each canto
    canti = re.split('[A-Z]{2,}\s[A-Z]{2,}\n', Orlando_furioso)

    # Creating a file for each individual canto
    ## For some reason the before last canto is badly cut --> I cut out the last line manually
    for item in canti:
        index = str((canti.index(item)))
        if index == '1' or index == '2' or index == '3' or index == '4' or index == '5' or index == '6' or index == '7' or index == '8' or index == '9':
            filepath = '/Users/tessacattaneo/Desktop/tesi_master/OF/0'+index+'_Of.txt'
        else:
            filepath = '/Users/tessacattaneo/Desktop/tesi_master/OF/'+index+'_Of.txt'
        if len(item) != 0:
            with open (filepath, 'w') as a:
                a.write(item)

if __name__ == "__main__":
    main()