/*******************************
PURPOSE: (Simulate flight of a paper airplane)
********************************/

#include "../include/Airplane.hh"
#include "trick/integrator_c_intf.h"
#include "trick/exec_proto.h"
#include <stdio.h>
#include <stddef.h>
#include <math.h>

/*
    Data for Mass, Wing Area, Coefficient of Drag and Coefficient of Lift from
    http://www.lactea.ufpr.br/wp-content/uploads/2018/08/On_the_Aerodynamics_of_Paper_Airplanes.pdf
*/

const int numElements = 14;
const double angles[numElements] = {0, 5, 10, 15, 20, 25, 30, 35, 38, 40, 42, 43, 44, 46};
const double ClArray[numElements] = {0, .15, .31, .49, .66, .80, .89, .94, .94, .93, .92, .91, .90, .87};
const double CdArray[numElements] = {0, 0.04, 0.075, 0.15, .25, .375, .52, .66, .74, .79, .84, .86, .88, .91};

int Airplane::default_data()
{
    init_speed = 20.0;
    angleDeg = 48.0;
    angle = angleDeg / 180 * M_PI;

    pos[0] = 0.0;
    pos[1] = 0.0;

    impactTime = 0.0;
    impact = false;

    mass = .5;
    surfaceArea = 0.023;
    crossArea = 0.008;

    Cl = 0.17;
    Cd = 0.03;

    airDensity = 1.225;
    
    return 0;

}

/*initializing data*/
int Airplane::initial_data()
{
    vel0[0] =  init_speed * cos(angle);
    vel0[1] =  init_speed * sin(angle);

    vel[0] =  vel0[0];
    vel[1] =  vel0[1];

    Cl = InterpolateCl(angleDeg, angles, ClArray);
    Cd = InterpolateCd(Cl, CdArray, ClArray);

    return 0;
}
/* Equations for plane flight */
int Airplane::airplane_deriv()
{
    double velocitySquared = pow(vel[0], 2) + pow(vel[1], 2);
    double velocity = sqrt(velocitySquared);
    double forceGravity = mass * -9.81;


    double forceLift = 0.5 * Cl * airDensity * surfaceArea * velocity * velocity;

    double forceDrag = -0.5 * Cd * airDensity * crossArea * velocity * velocity;

    double forceY = forceGravity + cos(angle) * forceLift - forceDrag * sin(angle);
    double forceX = forceDrag * cos(angle) - sin(angle) * forceLift; 

    if (!impact)
    {
        acc[0] = forceX / mass;
        acc[1] = forceY / mass; 
    }
    else
    {
        acc[0] = 0.0;
        acc[1] = 0.0;
        vel[0] = 0.0;
        vel[1] = 0.0;
    }
    return 0;
}

int Airplane::airplane_integ()
{
    int ipass;
    load_state(
        &pos[0],
        &pos[1],
        &vel[0],
        &vel[1],
        NULL);

    load_deriv(
        &vel[0],
        &vel[1],
        &acc[0],
        &acc[1],
        NULL);

    ipass = integrate();

    unload_state(
        &pos[0],
        &pos[1],
        &vel[0],
        &vel[1],
        NULL);

    return ipass;
}

/*interpolating through the Cl table to calculate Cl*/
double Airplane::InterpolateCl(double x, const double xValues[], const double yValues[])
{
    for (i = 0; i+2 < numElements && xValues[i] < x; i++)
    {
        if(xValues[i + 1] == x)
        {
            return yValues[i + 1];
        }
    }

    double lowerX = xValues[i - 1];
    double upperX = xValues[i];
    double lowerY = yValues[i - 1];
    double upperY = yValues[i];

    if (x < lowerX)
    {
        return ClArray[0];
    }
    else if (x > upperX)
    {
        return ClArray[numElements - 1];
    }
    else
    {
        return (((upperY - lowerY) / (upperX - lowerX)) * (x - lowerX) + lowerY);
    }
}

/*interpolating through Cd table to get value for Cd*/
double Airplane::InterpolateCd(double y, const double xValues[], const double yValues[])
{
    if (yValues[i] == y)
    {
       return xValues[i];
    }
    
    double lowerX = xValues[i - 1];
    double upperX = xValues[i];
    double lowerY = yValues[i - 1];
    double upperY = yValues[i];

    return ((y - lowerY) * (upperX - lowerX)) / (upperY - lowerY) + lowerX;

}

/*updating in real time for plane impact*/
double Airplane::airplane_impact()
{
    double tgo;
    double now;

    rf.error = pos[1];

    now = get_integ_time();
    tgo = regula_falsi( now, &rf);

    if (tgo == 0.0) 
    {                     
        now = get_integ_time() ;
        reset_regula_falsi( now, &rf) ; 
        impact = true ;
        impactTime = now ;
        vel[0] = 0.0 ;
        vel[1] = 0.0 ;
        acc[0] = 0.0 ; 
        acc[1] = 0.0 ;
        fprintf(stderr, "\n\nIMPACT: t = %.9f, pos[0] = %.9f\n\n", now, pos[0] ) ;
    }

    return tgo;
}

int Airplane::shutdown()
{
    double t = exec_get_sim_time();
    printf( "========================================\n");
    printf( "      Paper Airplane State at Shutdown     \n");
    printf( "t = %g\n", t);
    printf( "pos = [%.9f, %.9f]\n", pos[0], pos[1]);
    printf( "vel = [%.9f, %.9f]\n", vel[0], vel[1]);
    printf( "vel0 = [%.9f, %.9f]\n", vel0[0], vel0[1]);
    printf( "acc = [%.9f, %.9f]\n", acc[0], acc[1]);
    printf( "========================================\n");
    return 0 ;
}
