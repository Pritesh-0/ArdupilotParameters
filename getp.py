from pymavlink import mavutil

pf=open("test.param","a")
pf.write("# Onboard parameters for Vehicle 1\n")
pf.write("#\n")
pf.write("# Stack: ArduPilot\n# Vehicle: Rover\n# Version: 4.2.3\n# Git Revision: 2172cfb3\n#\n# Vehicle-Id Component-Id Name Value Type\n")
#pf.close()

conn=mavutil.mavlink_connection('tcpin:127.0.0.1:7777')

conn.wait_heartbeat()

print("Heartbeat from system (system %u component %u)" %(conn.target_system, conn.target_component))

conn.mav.param_request_list_send(
        conn.target_system, conn.target_component
        )

while True:

    try:
        msg=conn.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
        #print(len(msg))
        pf.write("1\t1\t%s  %f  %d\n" %(msg['param_id'], msg['param_value'], msg['param_type']))
    except Exception as error:
        print(error)
pf.close()
