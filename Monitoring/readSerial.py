import serial
import sys
import os
import csv
import keyboard


def is_connected(port):
    return os.path.exists(f'/dev/{port}')

def connect_to_serial(baudrate=115200):

    PORT = input("Type the port you are tryig to connect to: ")

    if sys.platform.startswith('linux'):
        port = f'/dev/{PORT}'

    else:
        port = PORT

    while(1):
        print(f'\n\nReading in from: {port}')

        if not is_connected(PORT):

            print("Nothing is connected at that port location.\n\n")
            PORT = input("Type a new port to connect to " 
                         "(Press enter to close)...:")

            if not PORT:
                return None

        try:
            ser = serial.Serial(f'{port}', \
                                baudrate=baudrate, \
                                parity=serial.PARITY_NONE, \
                                stopbits=serial.STOPBITS_ONE,\
                                bytesize=serial.EIGHTBITS,\
                                timeout=1)
            ser.read_all()
            return ser

        except:
            raise Exception("ERROR WITH SETTING UP SERIAL CONNECTION")
        

def read_serial(serialObj):
    
    #Set DTR (Figure out what does)
    #serialObj.setDTR(1)

    #Read line
    line = serialObj.readline()
    
    if not line:
        return None
    #Decode Line
    
    decodedLine = line.decode("utf-8")
    
    #Return String
    return decodedLine 


def write_serial_to_csv(filename, serial_obj):
    fieldnames = ["index", "ecg_value", "gsr_value", "par", "q_status", "a_status"]
    idx = 0 
    ecg = None
    gsr = None
    par = None
    q_status = False
    a_status = False

    with open(filename, "w") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    
    csv_file = open(filename, 'a')

    while True:
        try:
            try:
                ecg, gsr, par = read_serial(serial_obj).strip().split(',')
            except AttributeError:
                print("ecg, gsr, are not defined\n")
                continue

            if not ecg and gsr:
                print("ecg and gsr are none")
                continue
            
            q_status = 1 * keyboard.is_pressed('i')
            a_status = 1 * keyboard.is_pressed('a')
            print(ecg, gsr, par, q_status, a_status)

            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "index": idx,
                "ecg_value": ecg,
                "gsr_value": gsr,
                "par":par,
                "q_status": q_status,
                "a_status": a_status
            }
            
            csv_writer.writerow(info)
            idx += 1

        except KeyboardInterrupt:
            print("KEYBOARDINTERRUPT")
            break

    print("ENDING TRANSMISSION LINE")
    csv_file.close()
    return 0
        

def main():
    
    # Connect to serial


    # Add to csv file fast
    log_file = input("Enter a filename to store log in:")

    serial = connect_to_serial()
    

    if not serial:
        print("issue connecting")
        return 0 
    
    print("CONNECTED SUCCESSFULLY")

    write_serial_to_csv(log_file, serial)

     
    print("closing")

    serial.close()
    return 0


#-------------------- __name__ -- __main__ --------------------

if __name__ == "__main__":
    main()
