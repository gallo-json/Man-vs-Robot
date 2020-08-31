#include <stdio.h>
#include <fcntl.h>   //File Control Definitions           
#include <termios.h> // POSIX Terminal Control Definitions    
#include <errno.h>   // ERROR Number Definitions           

int setup_ser(int fd) {
    /*---------- Setting the Attributes of the serial port using termios structure --------- */

    struct termios SerialPortSettings;	// Create the structure                         

    tcgetattr(fd, &SerialPortSettings);	// Get the current attributes of the Serial port

    /* Setting the Baud rate */
    cfsetispeed(&SerialPortSettings,B9600); // Set Read  Speed as 9600                      
    cfsetospeed(&SerialPortSettings,B9600); // Set Write Speed as 9600                      

    /* 8N1 Mode */
    SerialPortSettings.c_cflag &= ~PARENB;   // Disables the Parity Enable bit(PARENB),So No Parity  
    SerialPortSettings.c_cflag &= ~CSTOPB;   // CSTOPB = 2 Stop bits,here it is cleared so 1 Stop bit
    SerialPortSettings.c_cflag &= ~CSIZE;	 // Clears the mask for setting the data size            
    SerialPortSettings.c_cflag |=  CS8;      // Set the data bits = 8                                

    SerialPortSettings.c_cflag &= ~CRTSCTS;       // No Hardware flow Control                        
    SerialPortSettings.c_cflag |= CREAD | CLOCAL; // Enable receiver,Ignore Modem Control lines       


    SerialPortSettings.c_iflag &= ~(IXON | IXOFF | IXANY);          // Disable XON/XOFF flow control both i/p and o/p
    SerialPortSettings.c_iflag &= ~(ICANON | ECHO | ECHOE | ISIG);  // Non Cannonical mode                           

    SerialPortSettings.c_oflag &= ~OPOST;/*No Output Processing*/

    if((tcsetattr(fd,TCSANOW,&SerialPortSettings)) != 0) {
        /* Set the attributes to the termios structure*/
        printf("\n  ERROR ! in Setting attributes");
    } else
        printf("\n  BaudRate = 9600 \n  StopBits = 1 \n  Parity   = none");
        
    tcflush(fd, TCIFLUSH); //Discards old data in the rx buffer 
}