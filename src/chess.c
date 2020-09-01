#include "chess.h"
#include <stdio.h>

void pgn(void) {
    int color;
    printf("Do you want to be white or black (w/b)? "); color = getchar();

    if (color == 'w') printf("You chose white");
    else printf("You chose black");
    //FILE *game;
    //game = fopen("../game.pgn", "a+");
}