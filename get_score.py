import requests
import json
from twilio.rest import Client
import datetime


match = "https://www.cricbuzz.com/match-api/livematches.json"

resp = requests.get(match)
resp_json = resp.json()

match_list = []

for i in resp_json["matches"]:
    match_list.append(i)


for i in match_list:
    if(resp_json["matches"][i]["state_title"]) == "Live":
        try:
            match_id = (i)
            t1 = resp_json["matches"][i]["team1"]["name"]
            t2 = resp_json["matches"][i]["team2"]["name"]
            vs = t1+" vs "+t2
            toss = (resp_json["matches"][i]["toss"]["winner"],"win's the toss")                                  
            decision = (resp_json["matches"][i]["toss"]["decision"])                                                            
            current_status = (resp_json["matches"][i]["status"])                                                            
        
            try:
                batsman_at_strike = (resp_json["matches"][i]["score"]["batsman"][0]["id"])                                        
                batsman_at_strike_r = (resp_json["matches"][i]["score"]["batsman"][0]["r"])
                batsman_at_strike_b = (resp_json["matches"][i]["score"]["batsman"][0]["b"])
                batsman_at_strike_4s = (resp_json["matches"][i]["score"]["batsman"][0]["4s"])
                batsman_at_strike_6s = (resp_json["matches"][i]["score"]["batsman"][0]["6s"])
                for j in resp_json["matches"][i]["players"]:
                    if j["id"] == batsman_at_strike:
                        c_strike = (j["name"]+" is at strike now.\n"+batsman_at_strike_r+" runs in "+batsman_at_strike_b+" balls with "+batsman_at_strike_4s+" 4's & "+batsman_at_strike_6s+" 6's\n")
            except IndexError as i:
                print("out")
        
            try:
                batsman_at_running = (resp_json["matches"][i]["score"]["batsman"][1]["id"])                                       
                batsman_at_running_r = (resp_json["matches"][i]["score"]["batsman"][1]["r"])
                batsman_at_running_b = (resp_json["matches"][i]["score"]["batsman"][1]["b"])
                batsman_at_running_4s = (resp_json["matches"][i]["score"]["batsman"][1]["4s"])
                batsman_at_running_6s = (resp_json["matches"][i]["score"]["batsman"][1]["6s"])
                for j in resp_json["matches"][i]["players"]:
                    if j["id"] == batsman_at_running:
                        c_runner = (j["name"]+" is at running now.\n"+batsman_at_running_r+" runs in "+batsman_at_running_b+" balls with "+batsman_at_running_4s+" 4's & "+batsman_at_running_6s+" 6's")
            except IndexError as i:
                print("out")
                
            bowler = (resp_json["matches"][i]["score"]["bowler"][0]["id"])                              
            bowler_o = (resp_json["matches"][i]["score"]["bowler"][0]["o"])
            bowler_r = (resp_json["matches"][i]["score"]["bowler"][0]["r"])
            bowler_w = (resp_json["matches"][i]["score"]["bowler"][0]["w"])
            if bowler_w == '1' or '0':
                w = "wicket"
            else:
                w = "wickets"
            for j in resp_json["matches"][i]["players"]:
                if j["id"] == bowler:
                    c_bowler = (j["name"]+" is bowling now.\ntook "+bowler_w+" "+w+" in "+bowler_o+" overs with loss of "+bowler_r+" runs\n")
        
        
            crr = (resp_json["matches"][i]["score"]["crr"])                                             
            current_score = (resp_json["matches"][i]["score"]["batting"]["score"])                      
            prev_overs = (resp_json["matches"][i]["score"]["prev_overs"])                           
            c_over = prev_overs.split("|")
            current_over = c_over[0]
            print(current_over)
            print(current_status)
            print(current_score)
            t2_squad = (resp_json["matches"][i]["team2"]["squad"])
            t2_squad_bench = (resp_json["matches"][i]["team2"]["squad_bench"])
            print(len(t2_squad),"+",len(t2_squad_bench))
        
        
            t1_squad = (resp_json["matches"][i]["team1"]["squad"])
            t1_squad_bench = (resp_json["matches"][i]["team1"]["squad_bench"])
            print(len(t1_squad),"+",len(t1_squad_bench))
            break
        except KeyError as e:
            pass
else:
    print("currently no match is going-on")



final_msg = vs+"\n"+current_status+"\n"+c_strike+"\n"+c_runner+"\n"+c_bowler

print(type(final_msg),"\n",final_msg)

if __name__ == "__main__":
    Twilio_account_sid = "(your id)"
    Twilio_auth_token = "(your token)"
    client = Client(Twilio_account_sid,Twilio_auth_token)
    to_whatsapp_number = "whatsapp:+91(your number)"
    from_whatsapp_number = "whatsapp:(twilio number)"
    messages = client.messages.create(body = final_msg, from_ = from_whatsapp_number,to = to_whatsapp_number)
    print("done")