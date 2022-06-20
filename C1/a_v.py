from uts import *
from mode import *
from datetime import datetime
  
class Switcher(object):
    def numbers_to_modes(self, argument):
        """Dispatch method"""
        method_name = 'mode_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid mode")
        # Call the method as we return it
        return method()
 
    def mode_1(self):
        Manual_Air_Mode()
        return 
 
    def mode_2(self):
        Manual_Air_Mode()
        return 
 
    def mode_3(self):
        Super_Wash_Mode()
    
        return
