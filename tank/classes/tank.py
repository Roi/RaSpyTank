from tank import GPIO 
from tank import TankGPIO
from tank import TankMove

class Tank(TankMove):
     __instance = None
     
     @staticmethod
     def getInstance():
        if Tank.__instance == None:
            Tank()
        return Tank.__instance 

     def __init__(self):
        if Tank.__instance != None:
            raise Exception("Pleash use Tank.getInstance() instead of Tank()")
        else:
            TankMove.__init__(self)
            Tank.__instance = self
    
   