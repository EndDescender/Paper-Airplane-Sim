/*********************************************************
 * PURPOSE: (Show intial conditions of a paper airplane)
*********************************************************/

#ifndef AIRPLANE_H
#define AIRPLANE_H

class Airplane
{
    public:
        double vel0[2] ;    /* *i m Init velocity of cannonball */
        double pos0[2] ;    /* *i m Init position of cannonball */
        double init_speed ; /* *i m/s Init barrel speed */
        double angle ;      /* *i rad Angle of cannon */

        double acc[2] ;     /* m/s2 xy-acceleration  */
        double vel[2] ;     /* m/s xy-velocity */
        double pos[2] ;     /* m xy-position */

        double time;        /* s Model time */

        bool impact ;       /* -- Has impact occured? */
        double impactTime;  /* s Time of Impact */

        double mass;        /* *i kg */
        double Cd;          /* -- Coefficient of Drag*/
        double Cl;          /* -- Coefficient of Lift*/

        double surfaceArea;  /* m^2 */
        double crossArea;    /* m^2 */

        double airDensity;   /* -- Constant air density at sea level*/

        int default_data();
        int initial_data();
        int airplane_deriv();
        int airplane_integ();
        int shutdown();
};

#endif