
/**
 * PURPOSE: (Show intial conditions of a paper airplane)
*/

#ifndef AIRPLANE_H
#define AIRPLANE_H

typedef struct 
{
    double vel0[2];
    double pos0[2];
    double init_speed;
    double init_angle;

    double acc[2];
    double vel[2];
    double pos[2];
}

#endif