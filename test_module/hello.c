#include<linux/init.h>
#include<linux/module.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("AZAM");
MODULE_DESCRIPTION("A simple kernel module");

static int hello_init(void)
{
  printk(KERN_ALERT "Hi, From Init Function\n");
 return 0; 
}

static void hello_exit(void)
{
 printk(KERN_ALERT "Good bye, From Exit Function\n");
}

module_init(hello_init);
module_exit(hello_exit);

