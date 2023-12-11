cmd_/home/pi/azam/test_module/hello.mod := printf '%s\n'   hello.o | awk '!x[$$0]++ { print("/home/pi/azam/test_module/"$$0) }' > /home/pi/azam/test_module/hello.mod
