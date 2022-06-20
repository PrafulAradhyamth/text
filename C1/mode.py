from uts import *

def Manual_Air_Mode():
    ch_status_valves('AV201','ON')
    wait(30)

    ch_status_valves('AV202','ON')
    wait(10)

    ch_status_valves('V901','ON')
    wait(12)

    ch_status_valves('V901','OFF')
    wait(12)

    ch_status_valves('AV202','OFF')
    wait(12)

    ch_status_valves('AV201','OFF')
    return

def Super_Wash_Mode():
    ch_status_valves('AV201','ON')
    wait(30)

    ch_status_valves('AV202','ON')
    wait(10)

    ch_status_valves('V101','ON')
    wait(12)

    ch_status_valves('V101','OFF')
    wait(12)

    ch_status_valves('AV202','OFF')
    wait(12)

    ch_status_valves('AV203','ON')
    wait(10)

    ch_status_valves('AV206','ON')
    wait(10)

    ch_status_valves('AV205','ON')
    wait(10)

    ch_status_valves('V101','ON')
    wait(30)
    
    ch_status_valves('AV203','OFF')
    wait(30)

    ch_status_valves('AV204','ON')
    wait(30)
    
    ch_status_valves('AV204','OFF')
    wait(30)
    
    ch_status_valves('AV203','ON')
    wait(30)
    ch_status_valves('AV205','OFF')
    ch_status_valves('AV203','OFF')
    ch_status_valves('AV206','OFF')
    ch_status_valves('AV202','ON')
    wait(10)
    ch_status_valves('V101','OFF') 
    wait(10)
    ch_status_valves('AV202','OFF')
    wait(2)
    ch_status_valves('AV202','ON')
    ch_status_valves('V101','ON') 
    wait(10)
    ch_status_valves('V101','OFF') 
    wait(10)
    ch_status_valves('AV202','OFF')
    wait(2)
    ch_status_valves('AV202','ON')
    ch_status_valves('V101','ON') 
    wait(10)
    ch_status_valves('V101','OFF') 
    wait(10)
    ch_status_valves('AV202','OFF')
    ch_status_valves('AV201','OFF')
    
    return
