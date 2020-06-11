import win32net, getopt, sys
from netaddr import IPNetwork


def cidrScan(target):
        print('Scanning for %s') % target
	for ip in IPNetwork(target):
		try:
			shares, _, _ = win32net.NetShareEnum(ip,0)
			print('list of shares for %s') % ip
			for share in shares:
				print(share)
		except:
			pass
	print('/FIN')
	sys.exit(2)

def singleScan(target):
        print('Scanning for %s') % target
	try:
		shares, _, _ = win32net.NetShareEnum(target,0)
		print(sharess)
		print('list of shares for %s') % ip
		for share in shares:
			print(share)
	except:
		pass
	
	print('/FIN')
	sys.exit(2)

def listScan(target):
        print('Scanning for %s') % target
	for ip in target:
		try:
			shares, _, _ = win32net.NetShareEnum(target,0)
			print('list of shares for %s') % ip
			for share in shares:
				print(share)
		except: 
			pass
	print('/FIN')
	
	sys.exit(2)

def usage():
	print('%s -l 192.168.1.1,10.10.10.1,172.16.1.1') % sys.argv[0]
	print('%s -s 192.168.1.1') % sys.argv[0]
	print('%s -c 192.168.1.1/24') % sys.argv[0]
	return
try:
    opts, args = getopt.getopt(sys.argv[1:], 'l:s:c', ['list=', 'single=', 'cidr=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    elif opt in ('-l', '--list'):
        target = arg
        listScan(target)
    elif opt in ('-s', '--single'):
        target = arg
        singleScan(target)
    elif opt in ('-c', '--cidr'):
        target = arg
        cidrScan(target)
    else:
        usage()
        sys.exit(2)
