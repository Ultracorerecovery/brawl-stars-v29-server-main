from Utils.Writer import Writer


class LoginFailed(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.reason = "Unsupported version!"

    def encode(self):
        self.writeInt(8)  # error code
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()  # update URL
        self.writeString(self.reason)
        self.writeHexa('''2E0000012C000000000000000000''')
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeVInt(0)
        print("[*] Message LoginFailed has been sent.")