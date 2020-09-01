#ifndef SERIAL_H_INCLUDED
#define SERIAL_H_INCLUDED

int setup_ser(int fd);
void move(int fd, int motor, int deg);
void idle(int fd);

#endif