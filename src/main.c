#include "serial.h"

#include <fcntl.h>   //File Control Definitions  
#include <unistd.h>  // UNIX Standard Definitions

void main(void) {
    /*------------------------------- Opening the Serial Port -------------------------------*/
    int fd = open("/dev/ttyUSB0", O_RDWR | O_NOCTTY);	/* ttyUSB0 is the FT232 based USB2SERIAL Converter   */
                                                        /* O_RDWR   - Read/Write access to serial port       */
                                                        /* O_NOCTTY - No terminal will control the process   */
                            
    if (fd == -1) {
        printf("\n  Error! in Opening ttyUSB0  ");
    } else
        printf("\n  ttyUSB0 Opened Successfully ");

    setup_ser(fd);
    
    char *msg = "#0 P1500\r";
    write(fd, msg, strlen(msg));

    close(fd); // Close the serial port
}