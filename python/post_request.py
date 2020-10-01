import sys
import requests

def main():
	if len(sys.argv) != 2:
		print "(+) usage %s <target>" % sys.argv[0]
		print "(+) eg: %s target" % sys.argv[0]
		sys.exit(1)
	t = sys.argv[1]
	# Passing a dictionary
	dict_data = {'user': 'admin', 'pass': 'admin'}
	r = requests.post('https://%s/login.php' % t , data = dict_data)
	# Passing a string 
	#headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	#str_data = "user=admin&pass=admin;"    
	#r = requests.post('https://%s/login.php' % t , headers = headers, data = str_data)
	

if __name__ == '__main__':
	main()
