
import serial
import db_connector as db

def insert_hr_data(number):
	try:
			# set up the serial line
			# set up serial port
			# set up timeout
            #poner my puerto de arduino en la siguiente linea. Ej: COM2
		ser = serial.Serial('/dev/cu.usbmodem14101',9600, timeout = 2)
			#show the dataf
		while True:
			#get data from serial port:
			data = (str(ser.readline().decode("utf-8"))).strip();
			if data:
				print(data)
				db.insert_hr(number,data)
	except Exception as e :
		print(e)
        #print("El dispositivo no esta conectado")

# si quieren probar la lectura del puerto serial desactivar la linea 22

