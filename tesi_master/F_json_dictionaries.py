import json
import itertools
import math
import re

def main():

    #In this script a dictionary containing all the riprese of a group of three from Dante by Ariosto is created. The dictionary contains the ordered group of three as the name of a sub_dictionary like this: A_B_C and the position of the three word combination in OF and in the three Cantica

    # Importing the json files and opening it as a python list
    # Inferno
    inferno = open('tesi_master/json_files/rimanti_json/inferno_rimanti.json')
    inferno_rimanti_list = json.load(inferno)

    # Purgtorio
    purgatorio = open('tesi_master/json_files/rimanti_json/purgatorio_rimanti.json')
    purgatorio_rimanti_list = json.load(purgatorio)

    # Paradiso
    paradiso = open('tesi_master/json_files/rimanti_json/paradiso_rimanti.json')
    paradiso_rimanti_list = json.load(paradiso)

    # Orlando Furioso
    OrlandoFurioso = open('tesi_master/json_files/rimanti_json/orlando_rimanti.json')
    of_rimanti_list = json.load(OrlandoFurioso)

    # Creating a comprehensive list of all the rimantis in Dante's Divina Commedia
    dante_canti = []
    dante_rimanti = []
    for canto in inferno_rimanti_list:
        dante_canti.append(canto)
        for sub_list in canto: 
            dante_rimanti.append(sub_list)
    for canto in purgatorio_rimanti_list:
        dante_canti.append(canto)
        for sub_list in canto: 
            dante_rimanti.append(sub_list)
    for canto in paradiso_rimanti_list:
        dante_canti.append(canto)
        for sub_list in canto: 
            dante_rimanti.append(sub_list)

    # with open ('tesi_master/json_files/rimanti_json/dante_rimanti.json', 'w') as dante:
    #     json.dump(dante_rimanti, dante)

    # Separating the groups of two rimanti's from the rest, first for the Divina Commedia than for the Orlando Furioso
    dante_two_rimanti = []
    for rimanti in dante_rimanti:
        if len(rimanti) == 2:
            dante_two_rimanti.append(sorted(rimanti))
    print(len(dante_two_rimanti))

    a_two_rimanti = []
    for canto in of_rimanti_list:
        for sub_list in canto:
            if len(sub_list) == 2:
                a_two_rimanti.append(sorted(sub_list))
    print(len(a_two_rimanti))

    # Canclulating the total number of groups of three rimanti in Orlando Furioso
    number_of_three_rimanti_of = 0
    for canto in of_rimanti_list:
        for sub_list in canto: 
            if len(sub_list) == 3:
                number_of_three_rimanti_of += 1
    print(number_of_three_rimanti_of)
    # The number is 9684

    # Calculating the number of riprese of Dante by Ariosto for complete groups of three
    three_rimanti_sorted = []
    for a_canto in of_rimanti_list:
        for of_sublist in a_canto: 
            if len(of_sublist) == 3:
                for d_sublist in dante_rimanti:
                    if sorted(of_sublist) == sorted(d_sublist):
                        three_rimanti_sorted.append(sorted(of_sublist))
                        break
    print(len(three_rimanti_sorted))
    # The length is 840
    # Updated: 850

    # Making a set to check that there are no repetitions
    opere_set = set(tuple(i) for i in three_rimanti_sorted)
    print(len(opere_set))

    # Creating a dictionary
    rimanti_dic = {}
    for sub_set in opere_set:
        key = '_'.join(sub_set)
        rimanti_dic[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    # List of all groups of three that are in Ariosto and Dante, with index of the group in Ariosto
    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in three_rimanti_sorted:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil(canto.index(of_sublist)/3)
                value = [pos_canto, pos_verso]
                rimanti_dic[key]['OF'].append(value)
    
    # Adding the information regarding the position of the rimanti in Dante's poem
    for canto in dante_canti:
        for dante_sublist in canto:
            if sorted(dante_sublist) in three_rimanti_sorted:
                key = '_'.join(sorted(dante_sublist))
                if dante_canti.index(canto) <= 33:
                    posotion_canto = (dante_canti.index(canto)) + 1
                    value = [posotion_canto, (canto.index(dante_sublist))*3]
                    rimanti_dic[key]['IF'].append(value)
                if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                    posotion_canto = (dante_canti.index(canto)) - 33
                    value = [posotion_canto, (canto.index(dante_sublist))*3]
                    rimanti_dic[key]['PG'].append(value)
                if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                    posotion_canto = (dante_canti.index(canto)) - 66
                    value = [posotion_canto, (canto.index(dante_sublist))*3]
                    rimanti_dic[key]['PD'].append(value)

    #print(rimanti_dic)

    with open ('tesi_master/json_files/dictionaries_json/groups_of_three.json', 'w') as dic:
        json.dump(rimanti_dic, dic)

    #Creating a dictionary for the groups of two cited by Ariosto (complete citation)


    # The same principles are applied for the rimanti in groups of two
    two_rimanti_sorted = []
    for a_rimanti in a_two_rimanti:
        for d_sublist in dante_two_rimanti:
            if a_rimanti == d_sublist:
                two_rimanti_sorted.append(a_rimanti)
                break
    print(len(two_rimanti_sorted))

    # Making a set to check that there are no repetitions
    two_set = set(tuple(i) for i in two_rimanti_sorted)
    print(len(two_set))

    # Making a dictionary
    two_rimanti_dic = {}
    for sub_set in two_set:
        key = '_'.join(sub_set)
        two_rimanti_dic[key] = {'OF': [], 'IF':[], 'PG': [], 'PD':[]}

    for canto in of_rimanti_list:
        for of_sublist in canto:
            if sorted(of_sublist) in two_rimanti_sorted:
                key = '_'.join(sorted(of_sublist))
                pos_canto = of_rimanti_list.index(canto) + 1
                pos_verso = math.ceil(canto.index(of_sublist)/3)
                value = [pos_canto, pos_verso]
                two_rimanti_dic[key]['OF'].append(value)
    
    for canto in dante_canti:
        for dante_sublist in canto:
            if sorted(dante_sublist) in two_rimanti_sorted:
                key = '_'.join(sorted(dante_sublist))
                if dante_canti.index(canto) <= 33:
                    posotion_canto = (dante_canti.index(canto)) + 1
                    value = [posotion_canto, (canto.index(dante_sublist))*3]
                    two_rimanti_dic[key]['IF'].append(value)
                if dante_canti.index(canto) > 33 and dante_canti.index(canto) <= 66:
                    posotion_canto = (dante_canti.index(canto)) - 33
                    value = [posotion_canto, (canto.index(dante_sublist))*3]
                    two_rimanti_dic[key]['PG'].append(value)
                if dante_canti.index(canto) > 66 and dante_canti.index(canto) < 100:
                    posotion_canto = (dante_canti.index(canto)) - 66
                    value = [posotion_canto, (canto.index(dante_sublist))*3]
                    two_rimanti_dic[key]['PD'].append(value)

    with open ('tesi_master/json_files/dictionaries_json/groups_of_two.json', 'w') as dic:
        json.dump(two_rimanti_dic, dic)

if __name__ == "__main__":
    main()