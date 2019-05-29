#include <stdio.h>
#include <dirent.h>

/*
char* usbDevList (){
    

}
*/

int main(){
    struct dirent *de;

    DIR *dr = opendir("/sys/bus/usb/devices/");

    while ((de = readdir(dr)) != NULL)
        printf("%s\n", de->d_name);


    return 0;
}