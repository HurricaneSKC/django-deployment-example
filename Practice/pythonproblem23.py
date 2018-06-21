class Animal:

    def __init__(self, birthType="Unknown",
                 apperance="Unknown",
                 blooded = "Unknown"):

        self.birth = birthType
        self.apperance = apperance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def apperance(self):
        return self.__apperance

    @apperance.setter
    def apperance(self, apperance):
        self.__appearance = apperance

    @property
    def blooded(self):
        return self.__blooded

    @birthType.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birthType, self.apperance, self.blooded)

class Mammal(Animal):
    def __init__(self, birthType="born alive",
                 apperance= "hair or fur",
                 blooded="warm blooded",
                 nuresYoung=True):

        Animal.__init__(self, birthType, apperance, blooded)

        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + " add it is {} they nurse their young".format(self.nurseYoung)

class