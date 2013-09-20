import subprocess

try:
	subprocess.check_call(['executable'])
except subprocess.CalledProcessError:
	pass # handle errors in the called executable
except OSError:
	print('\n  executable not found.\n') #