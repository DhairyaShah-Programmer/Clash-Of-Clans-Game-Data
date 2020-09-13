#   _____ _           _      ______                  _        _____ _        _       
#  /  __ \ |         | |     | ___ \                | |      /  ___| |      | |      
#  | /  \/ | __ _ ___| |__   | |_/ /___  _   _  __ _| | ___  \ `--.| |_ __ _| |_ ___ 
#  | |   | |/ _` / __| '_ \  |    // _ \| | | |/ _` | |/ _ \  `--. \ __/ _` | __/ __|
#  | \__/\ | (_| \__ \ | | | | |\ \ (_) | |_| | (_| | |  __/ /\__/ / || (_| | |_\__ \
#   \____/_|\__,_|___/_| |_| \_| \_\___/ \__, |\__,_|_|\___| \____/ \__\__,_|\__|___/
#                                         __/ |                                      
#                                        |___/                                       
# Developed By Dhairya Shah 
import requests
from prettytable import PrettyTable
from time import *
headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjlkZGM2ZDc5LTY1OTMtNGFjMy05ZmU2LTA1YmI1NmRlOGYxNSIsImlhdCI6MTU5OTk4OTA4NSwic3ViIjoiZGV2ZWxvcGVyL2ZkNTIxOTg0LTYxM2QtZGRkYS0yYWUxLTBkNjQxMzY3ZGZkZiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIzNS4yMzEuNjkuMTc3IiwiNDkuMzQuMjQuMzgiXSwidHlwZSI6ImNsaWVudCJ9XX0.MeLv_P54zHHc68xbpy-ERzanfHhsh50_kqD99XwkhPPGQM3qncMnwVyUo2ADkuYtdSzQTLtKtphPWPHssfMrsQ'
}

p_name = input("Enter your player tag: ")
print("\n")
def player_info(p_name):
  response = requests.get('https://api.clashroyale.com/v1/players/%23' + p_name, headers=headers)
  u_json = response.json()
  name = u_json['name']
  p_trp = u_json['trophies']
  arena = u_json['arena']
  arena_name = arena['name'] 
  favourite_card = u_json['currentFavouriteCard']   
  fav_card = favourite_card['name']   
  l = [[name, p_trp, fav_card, arena_name]]
  table = PrettyTable(['Username', 'Trophies', 'Favourite Card', 'Arena/League'])
  for rec in l:
    table.add_row(rec)

  print(table)


player_info(p_name)

sleep(20)
