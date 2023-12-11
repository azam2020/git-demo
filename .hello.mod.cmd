cmd_/home/pi/azam/hello.mod := printf '%s\n'   hello.o | awk '!x[$$0]++ { print("/home/pi/azam/"$$0) }' > /home/pi/azam/hello.mod
