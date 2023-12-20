#include<linux/init.h>
#include<linux/module.h>
#include<linux/fs.h>
#include<linux/slab.h>                 //kmalloc()
#include<linux/uaccess.h>              //copy_to/from_user()
#include <linux/err.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("AZAM");
MODULE_DESCRIPTION("Character driver example");

#define mem_size 1024

uint8_t *kernel_buffer;

int driver_open(struct inode *pinode, struct file *pfile)
{
   printk(KERN_ALERT "Inside the %s function\n",__FUNCTION__);
   return 0;
}

ssize_t driver_read(struct file *pfile, char __user *buffer, size_t length, loff_t *offset)
{
   printk(KERN_ALERT "Inside the %s function\n",__FUNCTION__);
	if( copy_to_user(buffer, kernel_buffer, mem_size) )
        {
                printk(KERN_ALERT "Data Read : Err!\n");
        }
        printk(KERN_ALERT "Data Read : Done!\n");
        return mem_size;
}

ssize_t driver_write(struct file *pfile, const char __user *buffer, size_t length, loff_t *offset)
{
  printk(KERN_ALERT "Inside the %s function\n",__FUNCTION__);
	    if( copy_from_user(kernel_buffer, buffer, length) )
        {
                printk(KERN_ALERT "Data Write : Err!\n");
        }
        printk(KERN_ALERT "Data Write : Done!\n");
  return length;
}

int driver_close(struct inode *pinode, struct file *pfile)
{
  printk(KERN_ALERT "Inside the %s function\n",__FUNCTION__);
  return 0;
}

struct file_operations driver_file_operations = {
  .owner   = THIS_MODULE,
  .open    = driver_open,
  .read    = driver_read,
  .write   = driver_write,
  .release = driver_close,
};

static int driver_init(void)
{
  printk(KERN_ALERT "Hello World, From Init Function\n");
  register_chrdev(139,"Simple Char Drv",&driver_file_operations);
  kernel_buffer = kmalloc(mem_size , GFP_KERNEL);
 return 0;
}

static void driver_exit(void)
{
 printk(KERN_ALERT "Good bye, From Exit Function\n");
 kfree(kernel_buffer);
 unregister_chrdev(139,"Simple Char Drv");
}

module_init(driver_init);
module_exit(driver_exit);
