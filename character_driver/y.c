#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
        int fd;
        char option;
        fd = open("/dev/test_file", O_RDWR);
        if(fd < 0) {
                printf("Cannot open device file...\n");
                return 0;
        }
	else
	{
	 printf("dmesg to see you are in the driver's open function\n");
	}

        while(1) {
                printf("****Please Enter the Option******\n");
                printf("        1. Write               \n");
                printf("        2. Read                 \n");
                printf("        3. Exit                 \n");
                printf("*********************************\n");
                scanf(" %c", &option);
                printf("Your Option = %c\n", option);
                
                switch(option) {
                        case '1':
                                printf("dmesg to see that you are in the driver's write function\n");
				break;
                        case '2':
                                printf("dmesg to see that you are in the driver's read function\n");
                                break;
                        case '3':
				printf("dmesg to see that you are in the driver's close function\n");
                                close(fd);
                                exit(1);
                                break;
                        default:
                                printf("Enter Valid option = %c\n",option);
                                break;
                }
        }
        close(fd);
}
