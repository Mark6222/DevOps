import subprocess
cmd = "ls -l"
result = subprocess.run(cmd, shell=True)
print (result.returncode)