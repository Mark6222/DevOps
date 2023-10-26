import subprocess

cmd = "scp -i MarksEC2Key.pem monitoring.sh ec2-user@3.80.216.188:."
cmd2 = "ssh -i MarksEC2Key.pem ec2-user@3.80.216.188 'chmod 700 monitoring.sh'"
cmd3 = "ssh -o StrictHostKeyChecking=no -i MarksEC2Key.pem ec2-user@3.80.216.188 './monitoring.sh'"
result = subprocess.run(cmd, shell=True)
print (result.returncode)
result = subprocess.run(cmd2, shell=True)
print (result.returncode)
result = subprocess.run(cmd3, shell=True)
print (result.returncode)
