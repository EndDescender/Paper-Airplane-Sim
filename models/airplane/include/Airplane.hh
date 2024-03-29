/*********************************************************
 * PURPOSE: (Show intial conditions of a paper airplane)
*********************************************************/

#ifndef AIRPLANE_H
#define AIRPLANE_H
#include "trick/regula_falsi.h"

class Airplane
{
    public:
        double vel0[2] ;    /* *i m Init velocity of plane */
        double pos0[2] ;    /* *i m Init position of plane */
        double init_speed ; /* *i m/s Init plane speed */
        double angle ;      /* *i rad Angle of plane */
        double angleDeg;    /* *i degree Angle of plane in degrees*/

        double acc[2] ;     /* m/s2 xy-acceleration  */
        double vel[2] ;     /* m/s xy-velocity */
        double pos[2] ;     /* m xy-position */

        bool impact ;       /* -- Has impact occured? */
        double impactTime;  /* s Time of Impact */

        double mass;        /* kg */
        double Cd;          /* -- Coefficient of Drag*/
        double Cl;          /* -- Coefficient of Lift*/
    

        double surfaceArea;  /* m^2 */
        double crossArea;    /* m^2 */

        double airDensity;   /* -- Constant air density at sea level*/

        int i;               /* -- Looping variable*/

        REGULA_FALSI rf;

        int default_data();
        int initial_data();
        int airplane_deriv();
        int airplane_integ();
        double InterpolateCl(double x, const double xValues[], const double yValues[]); /*values from list of values from Airplane.cpp */
        double InterpolateCd(double y, const double xValues[], const double yValues[]);
        int shutdown();
        double airplane_impact();
};

#endif
