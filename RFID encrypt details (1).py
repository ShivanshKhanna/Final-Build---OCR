import generateKeys, decrypt, encrypt
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

while True:
    print('Type what you want to encrypt:')
    message = input()
    Message_Encrypted = encrypt.encryptMessage(message)
    try:
        reader.write(Message_Encrypted)
        print("Written and Encrypted")
    finally:
        GPIO.cleanup()
      
      
