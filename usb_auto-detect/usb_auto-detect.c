#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

#ifndef DT_DIR
    #define DT_DIR 4
#endif

struct device{
    char* devPath;
    char* devName;
    struct device* next;
};

void _locUSBdev(const char dirp [1024], struct device *current){
    struct dirent *ent;
    DIR *dir;
    FILE *uevent1, uevent2;
    char nextDir[1024], uevent[1024], devEnt[64];

    if (!strstr(dirp, "/sys/bus/usb/dev/devices/usb")){
        if ((dir = opendir(dirp)) != NULL){
            while ((ent = readdir(dir)) != NULL){
                if (strcmp(ent->d_name, ".") != 0 && strcmp(ent->d_name, "..") != 0 && ent->d_type == DT_DIR){
                    strcpy(nextDir, dirp);
                    strcat(nextDir, ent->d_name);
                    strcat(nextDir, "/");
                    _locUSBdev(nextDir, current);
                }
                else if(strcmp(ent->d_name, "dev") == 0){
                    strcpy(uevent, dirp);
                    strcat(uevent, "uevent");
                    uevent1 = fopen(uevent, "r");
                    while (fscanf(fd, "%s", devEnt) != EOF){
                        if (strncmp(devEnt, "DEVNAME=bus/",13) == 0) break;
                        else if (strncmp(devEnt, "DEVNAME=", 9) == 0){
                            char devP[128];
                            strcpy(devP, "/dev/");
                            strcpy(devP, strstr(devEnt, "DEVNAME="));
                            current->devPath = devP;
                            
                            strcpy(uevent, dirp)
                            strcat(uevent, "device/uevent")
                        }
                    }

                    fclose(uevent1);
                }
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