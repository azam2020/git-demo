#include<stdio.h>
#include<stdlib.h>

int main()
{
  system("sudo iwlist wlan0 scan > scan_result.text");
  return 0;
}
