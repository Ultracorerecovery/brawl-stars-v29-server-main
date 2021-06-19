from Utils.Writer import Writer
from database.DataBase import DataBase
import random


class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        if self.player.roomID == 0:
            self.player.roomID = random.randint(0, 2147483647)
            self.writeInt(self.player.roomID)
            DataBase.replaceValue(self, 'roomID', self.player.roomID)

        else:
            self.writeInt(self.player.roomID)

        self.writeVInt(1557129593)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeScID(15, self.player.mapID) # map ID
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # high id
        self.writeInt(1)  # low id
        self.writeScID(16, self.player.brawlerID)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(99999)
        self.writeVInt(1)
        self.writeVInt(3)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString(self.player.name)  # player name
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(23)
        self.writeVInt(self.player.starpower)
        if self.player.useGadget == 1:
            self.writeVInt(23)
            self.writeVInt(self.player.gadget)
        else:
            self.writeVInt(0)
            self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(6)
        print("[*] Message TeamMessage has been sent.")
