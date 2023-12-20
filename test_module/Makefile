obj-m += hello.o

KDIR = /usr/src/linux-headers-6.1.0-rpi7-rpi-v8

all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules

clean:
	rm -rf *.o *.ko *.mod.* *.mod *.symvers *.order

