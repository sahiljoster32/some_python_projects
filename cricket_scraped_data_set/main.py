import requests
from bs4 import BeautifulSoup
import time 
import re
import csv

#--------------------------------------------------------all function definitions-------------------------------------------------------

def all_time_run_delaye():
    pass 
#till not is used -------- until deployment-------------
def players_name(players_id):
    players_name = []
    for tag_name in players_id:
        x = re.split(provider, tag_name)
        players_name.append(x[1])
    return players_name

def type_of_matches_played(soup_player_specific):
    all_matches_played = soup_player_specific.find_all("h4", class_= "player-stats__table-match-text")
    matches = []
    for tag in all_matches_played:
        item = tag.text
        matches.append(item.lower())
    if len(matches) == 6:
        for i in range(3):
            matches.pop()
    elif len(matches) == 4:
        for i in range(2):
            matches.pop()
    return matches

def data_getters(players_table_test):
    player_bb_test_list1 = []
    for i in range(2):
        player_bb_test = players_table_test[i]
        player_bb_test_list = player_bb_test.contents
        player_bb_test_list.pop(1)
        for item in player_bb_test_list:
            if item == "\n":
                player_bb_test_list.remove("\n")
        for item in player_bb_test_list:
            player_bb_test_list1.append(item.string)
        player_bb_test_list1.pop()
        player_bb_test_list1.append(":")
    return player_bb_test_list1

def splitter(list_of_data,index,storer_value):
    list_bat = []
    list_bowl = []
    flag = 0
    for item in list_of_data:
        if item == ":":
            flag = 1
        elif flag == 0:
            list_bat.append(item)
        elif flag == 1:
            list_bowl.append(item)
    if index == 1:
        storer_data_set_2(list_bowl,index,storer_value)
        storer_value += 1
        return list_bat
    if index == 2:
       return storer_data_set_2(list_bowl,index,storer_value)
    

def storer_data_set_2(list_bowl,index,storer_value):#still getting error from here -----------------------------------------
    if index == 1:
        if storer_value == 0:
            global list_bowl1
            list_bowl1 = list_bowl
        if storer_value == 1:
            global list_bowl2
            list_bowl2 = list_bowl
        if storer_value == 2:
            global list_bowl3
            list_bowl3 = list_bowl

    if index == 2:
        storer_value -= 1
        if storer_value == 2:
            return list_bowl1
        if storer_value == 1:
            return list_bowl2
        if storer_value == 0:
            return list_bowl3

def players_id_getter(players_all_tag):
    players_id = []
    for tag in players_all_tag:
        players_id.append(tag["href"])
    return players_id

def appending_data(rowlist, data):
    for value in data:
        rowlist.append(value)
    return rowlist

def delayer():
    time.sleep(0.04)
#this is only for avoiding mass hit of server --------------- usually 30ms was limit but for safer side we used 800ms

# ------------------------------------------------------till here all functions are done ---------------------------------------------

#-------main driver code starts from here------------

if __name__ == "__main__":
    list_bowl1, list_bowl2,list_bowl3 = [], [], []
    with open("data_set_bcci.csv","w") as data_set:
        writer_obj = csv.writer(data_set, lineterminator = '\n')
        
        provider = re.compile(r"/players/[0-9]+/")

        url_team_specific = "https://www.bcci.tv/players/men"
        res_team_specific = requests.get(url_team_specific)
        res_html1 = res_team_specific.text
        soup_team_specific = BeautifulSoup(res_html1, "html.parser")

        players_all_tag = soup_team_specific.find_all("a",class_="player-item")
        players_id = players_id_getter(players_all_tag)
        players_names = players_name(players_id)
        index_name = 0
        for tag in players_id:
            url_player_specific = f"https://www.bcci.tv{tag}"
            res_player_specific = requests.get(url_player_specific)
            res_html = res_player_specific.text
            soup_player_specific = BeautifulSoup(res_html, "html.parser")
            matches = type_of_matches_played(soup_player_specific)
            storer_value = 0
            for index in [1,2]:
                flag_print = 0
                for match in matches:
                    path = f"player-stats__table-row t-{match}"
                    players_table = soup_player_specific.find_all("tr", class_=path)
                    data = data_getters(players_table)
                    delayer()
                    data_scores = splitter(data,index,storer_value)
                    if index == 1:
                        storer_value += 1 
                    if index == 2:
                        pass
                        storer_value -= 1
                    if index == 1:
                        if flag_print == 0:
                            row_heading = ["Name----------","kind_of_match","Mat","Inn","No","Runs","HS","Ave","BF","SR","100","50","4s","6s","CT","ST"]
                            writer_obj.writerow(row_heading)
                            flag_print = 1
                        row_to_added_scores = [players_names[index_name],f"Batting and Fielding Stats - {match}"]
                        row_to_added_scores = appending_data(row_to_added_scores,data_scores)
                        writer_obj.writerow(row_to_added_scores)
                    elif index == 2:
                        if flag_print == 0:
                            row_heading = ["Name----------","kind_of_match","Mat","Inn","Balls","Runs","WKTS","BBM","Econ","Ave","SR","4W","5W"]
                            writer_obj.writerow(row_heading)
                            flag_print = 1
                        row_to_added_scores = [players_names[index_name],f"Bowling Stats - {match}"]
                        row_to_added_scores = appending_data(row_to_added_scores,data_scores)
                        writer_obj.writerow(row_to_added_scores)
            index_name += 1
    data_set.close()
    
# signed by -- sahil jhangar