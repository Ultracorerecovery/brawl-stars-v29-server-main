from Utils.Writer import Writer
from database.DataBase import DataBase


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player
        self.maps = [7, 8, 9, 10]

    def encode(self):
        DataBase.loadAccount(self)
        self.writeVInt(2020260)
        self.writeVInt(67238)

        self.writeVInt(self.player.trophies)
        self.writeVInt(self.player.trophies)

        self.writeVInt(122)
        self.writeVInt(200)

        self.writeVInt(1200) #exp

        self.writeScID(28, self.player.profileIcon) #player thumbnails.csv

        self.writeScID(43, self.player.namecolor) #name colors

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(122)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(256)
        self.writeVInt(590552)
        self.writeVInt(50552)
        self.writeVInt(6037352)
        self.writeVInt(200)
        self.writeVInt(200)
        self.writeVInt(5)
        self.writeVInt(77)
        self.writeVInt(180)
        self.writeVInt(430)
        self.writeVInt(975)
        self.writeVInt(2238)

        self.writeVInt(4)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)

        self.writeVInt(60)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(200)
        self.writeVInt(-1)
        self.writeVInt(0)

        self.writeVInt(99999)

        self.writeVInt(0)

        self.writeScID(16, self.player.brawlerID)  # selected brawler

        self.writeString("CA")
        self.writeString("v29")

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(1)
        for x in range(1):
            self.writeVInt(2)  # current season [0 - tara bazaar, 1 - monsters summer, 2 - STARR Park]
            self.writeVInt(0)  # brawl pass tokens
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(4)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(1)
            self.writeVInt(0)

        self.writeVInt(2020260)  # shop timestamp
        self.writeVInt(100)  # 100
        self.writeVInt(10)  # 10
        self.writeVInt(30)  # big box price
        self.writeVInt(3)  # big box multiplier
        self.writeVInt(80)  # mega box price
        self.writeVInt(10)  # mega box multiplier
        self.writeVInt(40)  # token doubler price
        self.writeVInt(1000)  # token doubler amount
        self.writeVInt(550)  # ??
        self.writeVInt(0)
        self.writeVInt(999900)

        self.writeVInt(6)
        for x in [0, 30, 80, 170, 350, 0]:
            self.writeVInt(x)

        self.writeVInt(16)
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24]:
            self.writeVInt(x)

        self.writeVInt(4)
        for x in self.maps:
            self.writeVInt(1883183565)  # timestamp
            self.writeVInt(self.maps.index(x) + 1)  # slot
            self.writeVInt(0)
            self.writeVInt(75992)  # time left
            self.writeVInt(10)
            self.writeScID(15, x)  # mapID
            self.writeVInt(3)  # state
            self.writeInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(0)  # events empty

        self.writeVInt(8)
        for x in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVInt(x)

        self.writeVInt(8)
        for x in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVInt(x)

        self.writeVInt(0)  # tickets price (useless)

        self.writeVInt(0)  # tickets count (useless)

        self.writeVInt(4)
        for x in [20, 50, 140, 280]:  # coins price
            self.writeVInt(x)

        self.writeVInt(4)
        for x in [150, 400, 1200, 2600]:  # coins count
            self.writeVInt(x)

        self.writeVInt(2)
        self.writeVInt(200)
        self.writeVInt(20)
        self.writeVInt(8640)

        self.writeVInt(10)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(50)
        self.writeVInt(604800)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3)
        self.writeVInt(0)
        self.writeVInt(900104)
        self.writeVInt(0)
        self.writeVInt(-1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        # LogicClientAvatar #

        self.writeVInt(0)
        self.writeVInt(1)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        if self.player.name is None:
            self.writeString("nullptr")
            self.writeBool(False)  # name set
            DataBase.createAccount(self)   # create new account
        else:
            self.writeString(self.player.name)
            self.writeBool(True)
        self.writeInt(0)

        self.writeVInt(8)  # commodity array count

        self.writeHexa(
            '''2a170001170401170801170c01171001171401171801171c01172001172401172801172c01173001173401173801173c01178001011784010117880101179f010117a4010117a9010117ae010117b3010117b8010117bd01011782020117b1020117b6020117bc02011782030117880301178e0301179a030117a0030117a6030117ac03011797040117a8040105019f9a0c05089f9a0c05099f9a0c2710009f9a0c10019f9a0c10029f9a0c10039f9a0c10049f9a0c10059f9a0c10069f9a0c10079f9a0c10089f9a0c10099f9a0c100a9f9a0c100b9f9a0c100c9f9a0c100d9f9a0c100e9f9a0c100f9f9a0c10109f9a0c10119f9a0c10129f9a0c10139f9a0c10149f9a0c10159f9a0c10169f9a0c10179f9a0c10189f9a0c10199f9a0c101a9f9a0c101b9f9a0c101c9f9a0c101d9f9a0c101e9f9a0c101f9f9a0c10209f9a0c10229f9a0c10239f9a0c10249f9a0c10259f9a0c10269f9a0c10279f9a0c2710009f9a0c10019f9a0c10029f9a0c10039f9a0c10049f9a0c10059f9a0c10069f9a0c10079f9a0c10089f9a0c10099f9a0c100a9f9a0c100b9f9a0c100c9f9a0c100d9f9a0c100e9f9a0c100f9f9a0c10109f9a0c10119f9a0c10129f9a0c10139f9a0c10149f9a0c10159f9a0c10169f9a0c10179f9a0c10189f9a0c10199f9a0c101a9f9a0c101b9f9a0c101c9f9a0c101d9f9a0c101e9f9a0c101f9f9a0c10209f9a0c10229f9a0c10239f9a0c10249f9a0c10259f9a0c10269f9a0c10279f9a0c00271000a0161001a0161002a0161003a0161004a0161005a0161006a0161007a0161008a0161009a016100aa016100ba016100ca016100da016100ea016100fa0161010a0161011a0161012a0161013a0161014a0161015a0161016a0161017a0161018a0161019a016101aa016101ba016101ca016101da016101ea016101fa0161020a0161022a0161023a0161024a0161025a0161026a0161027a01627100008100108100208100308100408100508100608100708100808100908100a08100b08100c08100d08100e08100f08101008101108101208101308101408101508101608101708101808101908101a08101b08101c08101d08101e08101f081020081022081023081024081025081026081027088402178c0101178d0101178e0101178f010117900101179101011792010117930101179401011795010117960101179701011798010117990101179a0101179b0101179c0101179d0101179e010117a3010117a8010117ad010117b2010117b7010117bc01011781020117860201178702011788020117890201178a0201178b0201178c0201178d0201178e0201178f020117900201179102011792020117930201179402011795020117960201179702011798020117990201179a0201179b0201179c0201179d0201179e0201179f020117a0020117a1020117a2020117a3020117a4020117a5020117a6020117a7020117a8020117a9020117aa020117ac020117ae020117af020117b0020117b5020117ba020117bb020117800301178103011786030117870301178c0301178d030117920301179303011798030117990301179e0301179f030117a4030117a5030117aa030117ab030117b0030117b10301179b040117ac040117b3040117b4040117b2030117b3030117b4030117b5030117b6030117b7030117b8030117b9030117ba030117bb030117bc030117bd030117be030117bf030117800401178104011782040117830401178404011785040117860401178704011788040117890401178a0401178b0401178c0401178d0401178e0401178f040117900401179104011792040117930401179404011795040117960401179d040117ae040117b5040127100002100102100202100302100402100502100602100702100802100902100a02100b02100c02100d02100e02100f02101002101102101202101302101402101502101602101702101802101902101a02101b02101c02101d02101e02101f021020021022021023021024021025021026021027029f9a0c00a301a40100000000000000''')

        self.writeVInt(2)  # tutorial state
        self.writeVInt(0)
        print("[*] Message OwnHomeData has been sent.")