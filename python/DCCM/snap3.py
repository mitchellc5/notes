from ophyd import Component as Cpt
from ophyd import Device, EpicsSignal, EpicsSignalRO
from pcdsdevices.interface import BaseInterface
import sys

base_pv = sys.argv[1]

class Snap(BaseInterface, Device):
    actual_position = Cpt(EpicsSignal, 'DCCM:SWITCH:MMS:TX.RBV')
    encoder_count = Cpt(EpicsSignal, 'DCCM:SWITCH:MMS:TX:PLC:nEncoderCount_RBV')
    #actual_position1 = Cpt(EpicsSignal, 'MR3K3:KBV:MMS:X.RBV')
    #encoder_count1 = Cpt(EpicsSignal, 'MR1K2:SWITCH:MMS:YRIGHT:PLC:nEncoderCount_RBV')
    

S = Snap(name="snap")
print(S.actual_position.get())
print(S.encoder_count.get())
#print(S.actual_position1.get())
#print(S.encoder_count1.get())

file1 = open("hard_notes_Tx.txt", "a")
file1.write("actual_position: " +  str(S.actual_position.get()) + " ")
file1.write(str(base_pv) + "               ")
file1.write("encoder_count: " +  str(S.encoder_count.get()) +  "\n")
#file1.write("actual_position1: " +  str(S.actual_position1.get()) + " ")
#file1.write(str(base_pv) + "               ")
#file1.write("encoder_count: " +  str(S.encoder_count1.get()) +  "\n")






