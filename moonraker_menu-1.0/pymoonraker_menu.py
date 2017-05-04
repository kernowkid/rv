from rv.rvtypes import *
from rv.commands import *
import os
import subprocess

class MoonRaker_menuMode(MinorMode):
    
    def eyePublish(self,currentShot):
        
        #get paths of all shots in 'SOURCES' list
        nodes = rv.commands.nodesOfType("RVFileSource") 
        paths = []
        
        for node in nodes:
            sources = rv.commands.sourceMediaInfoList(node)
            for source in sources:
                paths.append(source['file'])
        
        #assign the top image sequence in 'SOURCES' list to currentShot
        currentShot = paths[0]
        print currentShot
        
        #open eye pub tool
        subprocess.Popen(['python.exe','//Brsserver/brspipe/eye/tools/CreateOutput/createOutput.pyw', currentShot], shell=True)

        
    def __init__(self):
        MinorMode.__init__(self)
        self.init("py-moonraker_menu-mode", 
                [ ("Key-down--f8", self.eyePublish, "Publish") ], 
                None,                   
                [("Moonraker",  [("Publish", self.eyePublish, "F8", None)] )] 
            )
        
def createMode():
    return MoonRaker_menuMode()