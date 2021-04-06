# Reflection

I was never able to complete this project because I was having issues with serial communication. To try to fix this, I switched to a low level programming laguange like C which would give me more control over the hardware. I was think of having the C robot program and the Python stockfish backend comminicate over a PGN (Portable Game Notation, file format for chess games) file of the game in play. That is when I realized that I really didn't know how to program in C (as of the time I'm writing this my C skills have improved), so I ditched C.

## Problems

I got USB serial commication to work really well with C (flushing, /dev ports, speed, time of moves, etc) but every other aspect was to complicated for me at the time, so I switched to Python mainly. The following problems rose.

### Servos were not moving

This was really strange since the robot code worked with C, but not with Python PySerial. I think it was a port problem, where they were not getting initalized correctly. I managed to fix the problem, but then the motors started to move way too fast, slamming the arm on the desk. This was not optimal because I had to be as precise as possible to pick up pieces and move them.

I also at some point tried to make this project in Java, to keep up with my Java skills. Quickly dropped that idea because Java serial comm libraries are trash.

### Math calculations were not working



## Improvements

### AI to detect which pieces user moved with a camera

This would be a very ambitious improvement, but OpenCV has some chess dectection tools. Instead of the user inputing their moves in the terminal, it would be pretty cool if the robot could see those moves already.