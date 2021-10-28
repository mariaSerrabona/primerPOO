from SerVivo import SerVivo
from Utilidades import *
class Guerrero(SerVivo):
    __max_target = 10
    def __init__(self, name):
        SerVivo.__init__(self)
        self._target = self.__generateTargetToDie()
        self._name = name
    def get_name(self):
        return self._name
        # No se crea un set porque los guerreros no pueden cambiar de nombre
        '''
        def set_name(self, name):
        return self._name = name
        '''
    def get_target(self):
        return self._target
    def shoot(self):
        '''
        Shoot if the warrior is alive generating a randome number between 0
        and the ____max_target
        :returns the number to shoot if the warrior is alive, -1 otherwise
        '''
        if(self._vivo):
            shot = generaIntAleatorio(0,Guerrero.__max_target)
            print(self._name + " dispara " + str(shot))
            return shot
        else:
            return -1
    def get_shot(self, shot):
        '''
        if the target is guessed by the shoot, then the warrior dies.
        :param shoot: int with the shoot against the soldier:returns True if the shot kills
        the warrior (shot is the target and
        the warrior is alive), False otherwise
        '''
        isTarget = False
        if(self._vivo == True and self._target == shot):
            self._vivo = False # The SerVivoDIES!
            isTarget = True
            print(self._name + " se muere por el disparo " + str(shot))
        return isTarget
        def __generateTargetToDie(self):
            '''
            Private method to generate the target to get shot
            '''
            return generaIntAleatorio(0,Guerrero.__max_target)
        ''' TODO IF NEEDED OVERRIDE METHODS EQUALITY, COMPARISON, HASH , etc.
        '''
        def __str__(self):
            '''Override method toString to identify the objects and know their
            states
            '''
            return self._name
        @staticmethod
        def get_maxTarget():
            return Guerrero.__max_target
