#include <stdio.h>
#include <stdlib.h>
#include <3ds.h>


u8 escapeSteps (float x, float y) {
    u8 currIteration = 0;
    s8 comparisonValue = 4;
    s8 currIteration_LIMIT = 8;
    float resultantX = x;
    float resultantY = y;
    float resultant;

    // calculating first pass...
    if (comparisonValue <= (resultantX*resultantX)+(resultantY*resultantY)) {
        currIteration = 0;
    } else {
    // second pass++:
        while ((currIteration < currIteration_LIMIT)) {
            resultantY = ((resultantX*resultantY*2)+y);
            resultantX = ((resultantX*resultantX)-(resultantY*resultantY)+x);
            resultant = (resultantX*resultantX)+(resultantY*resultantY);
            
            currIteration ++;   // else increment
            
            if (resultant >= comparisonValue) 
                break;
        }
    }
    return (currIteration+1);
}



int main (int argc, char** argv)
{
    // Init services
    gfxInitDefault();
    cfguInit();
    
    // Init console for text output
    PrintConsole topScr, botScr;
    consoleInit(GFX_TOP, &topScr);
    consoleInit(GFX_BOTTOM, &botScr);
    
    
    // consoleSelect(&botScr);
    printf("topScr ptr %p\n", &topScr);
    printf("botScr ptr %p\n", &botScr);

    
    // Print asciibrot
    consoleSelect(&topScr);
    float xCord = (-22);
    float yCord = (14);
    for (; yCord > (-14); yCord--)
    {
        for (; xCord < 22; xCord++)
        {
            printf("%d", (int)escapeSteps(xCord/8, yCord/8));
        }
        xCord = (-22);
        printf("\n");
        
    }
    
    
    consoleSelect(&botScr);
    printf("press START to exit\n");
    while (aptMainLoop())
    {
        hidScanInput();
        
        // press START to exit program.
        u32 kDown = hidKeysDown();
        if (kDown & KEY_START)
            break;

        touchPosition tpos;
        hidTouchRead(&tpos);
        if (tpos.px != 0)
            printf("touch pos at: x_%d, y_%d\n", (int)tpos.px, (int)tpos.py);
        
        // Flush and swap framebuffers
        // gfxFlushBuffers();           // not really needed yet since we
        // gfxSwapBuffers();            // are not redrawing anything
        gspWaitForVBlank();
    }
    
    // Exit services
    cfguExit();
    gfxExit();
    return 0;
}