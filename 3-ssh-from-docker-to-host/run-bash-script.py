import subprocess

script="source ./run-ssh.sh {key} {value};"
script = script.format(key = "TEST_REG_EDIT_KEY", value = "DUMMY")

# exeucte script
subprocess.Popen(['bash', '-c', script])