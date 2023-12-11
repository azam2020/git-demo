cmd_/home/pi/azam/character_driver/driver.mod := printf '%s\n'   driver.o | awk '!x[$$0]++ { print("/home/pi/azam/character_driver/"$$0) }' > /home/pi/azam/character_driver/driver.mod
