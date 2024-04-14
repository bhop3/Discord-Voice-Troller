import tls_client
import os
import ctypes
import time
import random

class xyzVCAnnoyer:
    def __init__(self):
        global session
        os.system("mode 80, 20")
        self.clear()
        session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)

        self.xyz_main()
    
    def clear(self):
        os.system("cls")
    
    def setTitle(self, _str):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")
    
    @staticmethod
    def check_status(status_code: int):
        status_messages = {
            200: "Success",
            201: "Success",
            204: "Success",
            400: "Detected Captcha",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method not allowed",
            429: "Too many Requests"
        }
        return status_messages.get(status_code, "Unknown Status")
    
    def xyz_main(self):
        self.setTitle("Free Tool to annoy People → discord.gg/xyzshop → dev: bhop3")

        def kicker(guildid, channelids):
            payload = {"channel_id": None}
            headerz = {"authorization": "YOUR_DISCORD_TOKEN"}
            request_count = 0
            start_time = time.time()

            while True:
                # this Shit is for Discord Ratelimit, since you get 7-8 Seconds by discord !
                if request_count >= 5:
                    current_time = time.time()
                    if current_time - start_time < 5:
                        time.sleep(5 - (current_time - start_time))
                    start_time = time.time()
                    request_count = 0

                r = session.patch(f"https://discord.com/api/v9/guilds/{guildid}/members/{random.choice(channelids)}", json=payload, headers=headerz)
                request_count += 1

                match r.status_code:
                    case 200:
                        print(f'({xyzVCAnnoyer.check_status(r.status_code)}) → [Disconnected Random]')
                    case 429:
                        retry_after = float(r.json().get('retry_after', 5))
                        print(f"Something fucked up, wait >> {retry_after} << seconds...")
                        time.sleep(retry_after)
                    case _:
                        print(f"Error {xyzVCAnnoyer.check_status(r.status_code)}")

        guildid = input(f'Guild ID: ')
        channel = input(f'MemberIDS ID1 ID2 ID3 ...: ')
        channelids = channel.replace(" ", ",").split(',')

        kicker(guildid, channelids)
        
xyzVCAnnoyer()