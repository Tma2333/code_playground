#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

#ifndef DT_DIR
    #define DT_DIR 4
#endif

struct device{
    char* devAddr;
    char* devName;
    struct device* next;
};

void locUSBdev(const char dirp [1024], struct device *current){
    struct dirent *ent;
    DIR *dir;
    char nextDir[1024];

    if (!strstr(dirp, "/sys/bus/usb/dev/devices/usb")){
        if ((dir = opendir(dirp)) != NULL){
            while ((ent = readdir(dir)) != NULL){
                if (strcmp(ent->d_name, ".") != 0 && strcmp(ent->d_name, "..") != 0 && ent->d_type == DT_DIR){
                    strcpy(nextDir, dirp);
                    strcat(nextDir, ent->d_name);
                    strcat(nextDir, "/");
                    locUSBdev(nextDir, current);
                }
                else if(strcmp(ent->d_name)){
                
            }
        }
    }
    else
    {
        return;
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