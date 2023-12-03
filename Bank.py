import generateKeys, decrypt, encrypt
import time
import serial
##Message created
CVC_1 = 338
Cardnum1 = 123787389
Amount2 = 100
epoch = time.time()
epoch = int(epoch*100/100)

message = str(CVC_1) + str(Cardnum1) + str(Amount2)
encrypt.encryptMessage(message)

##Message seperated
message = decrypt.decryptMessage()

CVC = int(message[0:3])
Cardnum = int(message[3:12])
Amount = int(message[12:])

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
ser.reset_input_buffer()

time_elapsed = 300000000000000000000000000000

if(CVC == CVC_1 and Cardnum == Cardnum1):
    print("Access Granted")
    if (time_elapsed < 60000000000000000000):
        time_amount = 0
        ser.write(b"MSTrue\n")
    else:
        time_amount = int((0.00000000000003*time_elapsed)/100000000000000)

    if(Amount >= time_amount):
        ser.write(b"LCDTrue1\n")
        Amount1 = Amount - time_amount 
        ser.write(b"LCDTrue\n")
        ser.write(b"MSTrue\n") 
        time.sleep(1)
        if ser.in_waiting > 0:
            # Decode it and print it to the console
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
    elif(Amount < time_amount):
        ser.write(b"LCDFalse\n")
        ser.write(b"MSFalse\n") 
        time.sleep(1)
        if ser.in_waiting > 0:
            # Decode it and print it to the console
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

else:
    print("Invalid")

    

