from pymavlink import mavutil

conn=mavutil.mavlink_connection('tcpin:127.0.0.1:7777')

conn.wait_heartbeat()

print("Heartbeat from system (system %u component %u)" %(conn.target_system, conn.target_component))

conn.mav.param_request_list_send(
        conn.target_system, conn.target_component
        )

while True:

    try:
        msg=conn.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
        print(len(msg))
        #print('Name: %s\tValue: %f\tType %d' %(msg['param_id'], msg['param_value'], msg['param_type']))
    except Exception as error:
        print(error)

