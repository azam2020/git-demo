cmd_/home/pi/azam/Module.symvers :=  sed 's/ko$$/o/'  /home/pi/azam/modules.order | scripts/mod/modpost -m -a    -o /home/pi/azam/Module.symvers -e -i Module.symvers -T - 
