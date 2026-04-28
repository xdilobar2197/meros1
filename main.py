# meros1



class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi

    def ovoz(self):
        print('Nomalum ovoz')


class it(Hayvon):
    def __init__(self, nomi, zoti):
        super().__init__(nomi)
        self.zoti = zoti

    def ovoz(self):
        print(f'Nomi: {self.nomi}')
        print(f'Zoti: {self.zoti}')
        print('Vov Vov')

i = it("Rex", "Ovchi")
i.ovoz()
