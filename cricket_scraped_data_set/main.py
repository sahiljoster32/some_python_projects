import requests
from bs4 import BeautifulSoup
import time 
import re

def all_time_run_delaye():
    pass


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

def splitter(list_of_data):
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
    return list_bat, list_bowl

def players_id_getter(players_all_tag):
    players_id = []
    for tag in players_all_tag:
        players_id.append(tag["href"])
    return players_id


def delayer():
    time.sleep(0.5)


if __name__ == "__main__":
    url_team_specific = "https://www.bcci.tv/players/men"
    res_team_specific = requests.get(url_team_specific)
    res_html1 = res_team_specific.text
    soup_team_specific = BeautifulSoup(res_html1, "html.parser")


    players_all_tag = soup_team_specific.find_all("a",class_="player-item")
    players_id = players_id_getter(players_all_tag)
    

    for tag in players_id:
        url_player_specific = f"https://www.bcci.tv{tag}"
        res_player_specific = requests.get(url_player_specific)
        res_html = res_player_specific.text
        soup_player_specific = BeautifulSoup(res_html, "html.parser")
        matches = type_of_matches_played(soup_player_specific)
        print("\n\n")
        for match in matches:
            path = f"player-stats__table-row t-{match}"
            players_table = soup_player_specific.find_all("tr", class_=path)
            data = data_getters(players_table)
            delayer()
            data_bat, data_bowl = splitter(data)
            print(f"batting for {match}")
            print(data_bat)
            print(f"bowling for {match}")
            print(data_bowl)