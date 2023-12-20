cmd_/home/pi/Azam/git-demo/test_module/hello.mod := printf '%s\n'   hello.o | awk '!x[$$0]++ { print("/home/pi/Azam/git-demo/test_module/"$$0) }' > /home/pi/Azam/git-demo/test_module/hello.mod
