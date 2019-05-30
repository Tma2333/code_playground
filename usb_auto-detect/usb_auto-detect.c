#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>

struct device{
    char* devAddr;
    char* devName;
    struct device* next;
};

void locUSBdev(const char *dirp, struct device *current){
    struct dirent *ent;
    DIR *dir;
    struct stat s;
    
    if (!strstr(dirp, "/sys/bus/usb/dev/devices/usb")){
        if ((dir = opendir(dirp)) != NULL){
            while ((ent = readdir(dir)) != NULL){
                if (strcmp(ent->d_name, ".") != 0 && strcmp(ent->d_name, "..") != 0 ){
                    
                }
            }
        }
    }
}



void usbDevList(struct device *head){
    // variables
    struct dirent *ent;
    DIR *dir;

    // checking all folder under 
    dir = opendir("/sys/bus/usb/devices/");
    

}


int main(){
    struct device* head = NULL;
    
    return 0;
}