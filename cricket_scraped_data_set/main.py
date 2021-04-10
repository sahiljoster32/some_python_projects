import requests
from bs4 import BeautifulSoup


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

if __name__ == "__main__":
    url = "https://www.bcci.tv/players/1124/jasprit-bumrah"
    res = requests.get(url)
    res_html = res.text
    soup = BeautifulSoup(res_html, "html.parser")

    matches_list = ["test","odi","t20i"]
    for match in matches_list:
        path = f"player-stats__table-row t-{match}"
        players_table = soup.find_all("tr", class_=path)
        data = data_getters(players_table)
        data_bat, data_bowl = splitter(data)
        print(f"batting for {match}")
        print(data_bat)
        print(f"bowling for {match}")
        print(data_bowl)