#ifndef SERIAL_H_INCLUDED
#define SERIAL_H_INCLUDED

int setup_ser(int fd);
void write_ser(int fd, int motor, int deg);

#endif