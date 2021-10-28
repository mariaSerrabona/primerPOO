class Marciano(Guerrero):
    __totalMarcianosAlive = 0
    __shotsToKillAMarciano = 3

    def __init__(self, name):
        Guerrero.__init__(self, name)
        self.__shotsToReceive = Marciano.__shotsToKillAMarciano Marciano.__totalMarcianosAlive += 1
    def get_shotsToReceive(self):
        return self.__shotsToReceive
# Overrides the method get_shot from the parent class! def get_shot(self, shot):

        isTarget = False
        if(self._vivo == True and self._target == shot):
            self.__shotsToReceive -=1
            isTarget = True
            if(self.__shotsToReceive == 0):
                Guerrero.get_shot(self,shot)
                Marciano.__totalMarcianosAlive -= 1
        return isTarget
    @staticmethod
    def get_total_marcianos_alive():
        '''
        :returns the total number of Marcianos alive '''
        return Marciano.__totalMarcianosAlive

    @staticmethod
    def get_total_marcianos_alive():
        '''
        :returns the shots needed to kill a marciano
        '''
        return Marciano.__shotsToKillAMarciano
