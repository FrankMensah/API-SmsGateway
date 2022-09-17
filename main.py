import requests
import random
import time
import math

def run_dem():
    messagis = []

    how_many = input("How Many Different Message?: \n")

    how_much = input("How many Messages do you want to send? Mini/Max 100: \n")

    multiply_sms = int(math.ceil(int(how_much) / int(how_many)))

    messin = []
    for ioi in range(int(how_many)):
        messag = input(f"\nEnter Message #{ioi + 1}: ")

        messin.append(messag)
        total = messin * multiply_sms
        random.shuffle(total)

    for opi in total:

        response = requests.get("https://cutt.ly/api/api.php?key=" + cut_api + "&short=" + shorten_link)

        json_data = response.json()

        messagis.append(opi + " " + json_data["url"]["shortLink"])

    with open(nums_dir, 'r', encoding="mbcs") as f:
        number_lines = f.readlines()

    num = 0
    for number, message in zip(number_lines, messagis):
        num += 1

        response = requests.get("https://example.me/services/send.php?key=" + Api_key + "&number=" + number.strip() + "&message=" + message.strip() + "&devices=" + device_No + "&type=sms&prioritize=0")

        time.sleep(2)

        res_code = response.status_code

        stt_code = 200

        if res_code == stt_code:
            print(f"{num} Message Sent")


        else:
            print("Failed")



#mess_dir = input("Enter Message(s) Directory:\n""->")

nums_dir = input("\nEnter Phone Number(s) Directory:\n""->")

Api_key = input("\nEnter SMS API \n""->")

cut_api = input("\nEnter Cuttly Api\n""->")

shorten_link = input("\nEnter URL to shorten Link\n""->")

device_No = input("\nDevice Number\n""->")


print("\nSMS GATEWAY")
print("###########\n")

run_dem()
