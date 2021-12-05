from json import loads
from time import sleep
from json import dumps
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import os

os.system('cls' if os.name=='nt' else 'clear')
print(
"""

               AAA               kkkkkkkk             iiii    iiii  
              A:::A              k::::::k            i::::i  i::::i 
             A:::::A             k::::::k             iiii    iiii  
            A:::::::A            k::::::k                           
           A:::::::::A            k:::::k    kkkkkkkiiiiiii iiiiiii 
          A:::::A:::::A           k:::::k   k:::::k i:::::i i:::::i 
         A:::::A A:::::A          k:::::k  k:::::k   i::::i  i::::i 
        A:::::A   A:::::A         k:::::k k:::::k    i::::i  i::::i 
       A:::::A     A:::::A        k::::::k:::::k     i::::i  i::::i 
      A:::::AAAAAAAAA:::::A       k:::::::::::k      i::::i  i::::i 
     A:::::::::::::::::::::A      k:::::::::::k      i::::i  i::::i 
    A:::::AAAAAAAAAAAAA:::::A     k::::::k:::::k     i::::i  i::::i 
   A:::::A             A:::::A   k::::::k k:::::k   i::::::ii::::::i
  A:::::A               A:::::A  k::::::k  k:::::k  i::::::ii::::::i
 A:::::A                 A:::::A k::::::k   k:::::k i::::::ii::::::i
AAAAAAA                   AAAAAAAkkkkkkkk    kkkkkkkiiiiiiiiiiiiiiii
                                                                                                     
""")
guild_id = input("Guild ID: ")
chid = input("Channel ID: ")
tokenlist = open("tokens.txt").read().splitlines()
executor = ThreadPoolExecutor(max_workers=int(1000000))
def run(token) :
    ws = WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    hello = loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    ws.send(dumps({"op": 4,"d": {"guild_id": guild_id,"channel_id": chid,"self_mute": True,"self_deaf": True}}))
    ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": guild_id,"channel_id": chid,"preferred_region": "singapore"}}))
    while True:
        sleep(heartbeat_interval/1000)
        try:
            ws.send(dumps({"op": 1,"d": None}))
        except Exception:
            break

i = 0
for token in tokenlist:
    executor.submit(run, token)
    i+=1
    print("connected ws : {}".format(i))