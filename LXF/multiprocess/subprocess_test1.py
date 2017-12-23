import subprocess

print('$ nslookup www.python.ort')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
