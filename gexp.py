import hypixel
import gzip
import zlib
import requests
import time
import nbt
import io
import sys
import nbt
guild = None

api_key = ({'79a681b0-45fe-473a-a8a5-444e2f67edf3'})
hypixel.setKeys({'79a681b0-45fe-473a-a8a5-444e2f67edf3'})
def fetch_uuid_uname(uname_or_uuid):
    r = requests.get(f'https://mc-heads.net/minecraft/profile/{uname_or_uuid}').json()
    return r['name'], r['id']

def decode_inventory_data(raw):
   data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw)))
   print(data.pretty_tree())

def print_armor_piece(nbt):
    piece = nbt['i']['tag']['display']['Name']
    print(piece.pretty_tree)

def get_Guild_Info(guild_id):
    data = requests.get(f'https://api.hypixel.net/guild?id={guild_id}&key=79a681b0-45fe-473a-a8a5-444e2f67edf3').json()
    return data

while True:

    Name = input("Minecraft username: ")

    #uname, uuid = fetch_uuid_uname(Name)
    Player = hypixel.Player(Name)
    print(" ")
    print('Guild Id: ' + Player.getGuildID())
    print(" ")

    guild = get_Guild_Info(Player.getGuildID())
    memberNumber = len(guild['guild']['members'])
    for x in range(memberNumber - 1):
        # print(guild['guild']['members'][x]['uuid'])
        if sum(guild['guild']['members'][x]['expHistory'].values()) < 50000:
            name = fetch_uuid_uname(guild['guild']['members'][x]['uuid'])
            print(name[0] + " does not have the required GEXP!")
        else :
            continue
    print(" ")
    input("Press any key to continue...")
    sys.exit("EXP Checked")
