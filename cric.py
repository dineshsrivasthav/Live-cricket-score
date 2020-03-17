import time
import requests
from bs4 import BeautifulSoup
import win10toast


def LiveScore(showNotification):
 toast = win10toast.ToastNotifier()
 url = "http://mapps.cricbuzz.com/cbzios/match/livematches"
 response = requests.get(url)
 matchData = response.json()
 inprogress = []
 completed = []
 preview = []
 inningsbreak = []
 matches = matchData["matches"]
 msg = str(len(matches)) + " cricket matches are being played."
 if(showNotification):
	 toast.show_toast("Live Score", msg)
 
 def categorizeMatches():
	 for match in matches:
		 if(match["header"]["state"] == "inprogress"):
			 inprogress.append(match)
		 elif(match["header"]["state"] == "innings break" or match["header"]["state"] == "tea" or 
		 match["header"]["state"] == "stump" or match["header"]["state"] == "lunch"):
			 inningsbreak.append(match)
		 elif(match["header"]["state"] == "complete" or match["header"]["state"] == "mom"):
			 completed.append(match)
		 else:
			 preview.append(match)

 def displayMatchData(matches):
	 if(len(matches) != 0):
		 for match in matches:
			 match_status = match["header"]["status"]
			 team1 = match["team1"]
			 team2 = match["team2"]
			 team1_name = team1["name"]
			 team2_name = team2["name"]
			 team1_id = team1["id"]
			 # team2_id = team2["id"]
			 series_name = match["series_name"]
			 match_type = match["header"]["type"]
			 msg = series_name+"\n"+team1_name+" VS " + \
			 team2_name+"\n"+match_type+"\n"+match_status
			 print(msg)
			 batting_team = match["bat_team"]
			 bowling_team = match["bow_team"]
			 if(batting_team["id"] == team1_id):
				 batting_team_name = team1_name 
				 bowling_team_name = team2_name
			 else:
				 batting_team_name = team2_name
				 bowling_team_name = team1_name
	         print("Batting :"+str(batting_team_name) + str(batting_team))
	         print("Bowling :"+str(bowling_team_name)+str(bowling_team))
	         print("-------------------------------------")
	         if(showNotification):
				 toast.show_toast("Live Score", msg)

 categorizeMatches()

 print("++++++++++++++++++INPROGRESS++++++++++++++++++")
 displayMatchData(inprogress)
 print("++++++++++++++++++COMPLETED++++++++++++++++++")
 displayMatchData(completed)
 print("++++++++++++++++++INNINGS-BREAK++++++++++++++++++")
 displayMatchData(inningsbreak)

 #print("++++++++++++++++++PREVIEW++++++++++++++++++")
 #displayMatchData(preview)
 
 for match in matches:
	 if(match["header"]["state"] != "preview"):
		  team1 = match["team1"]["name"]
		  team2 = match["team2"]["name"]
		  series_name = match["series_name"]
		  match_type = match["header"]["type"]
		  msg = series_name+"\n"+team1+" VS "+team2+"\n"+match_type
		  print(msg)
		  batting_team = match["bat_team"]
		  bowling_team = match["bow_team"]
		  print(str(batting_team))
		  print(str(bowling_team))
		  print("-------------------------------------")
		  if(showNotification):
			  toast.show_toast("Live Score", msg)
while True:
 LiveScore(showNotification=True)
 print("======================================\nNew Update\n======================================")
LiveScore(showNotification=False)
