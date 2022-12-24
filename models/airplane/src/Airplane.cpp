/*******************************
PURPOSE: (Simulate flight of a paper airplane)
********************************/

#include "../include/Airplane.hh"
#include "trick/integrator_c_intf.h"
#include "trick/exec_proto.h"
#include <stdio.h>
#include <math.h>

int Airplane::default_data()
{
    init_speed = 20.0;
    angle = M_PI / 4;

    pos[0] = 0.0;
    pos[1] = 0.0;

    impactTime = 0.0;
    impact = false;

    /*
     *Data for Mass, Wing Area, Coefficient of Drag and Coefficient of Lift from
     *http://www.lactea.ufpr.br/wp-content/uploads/2018/08/On_the_Aerodynamics_of_Paper_Airplanes.pdf
    */

    Cd = .03;
    Cl = .17;
    
    mass = .005;
    surfaceArea = .023;
    crossArea = .008;

    airDensity = 1.225;
    
    return 0;

}

int Airplane::initial_data()
{
    vel0[0] =  init_speed * cos(angle);
    vel0[1] =  init_speed * sin(angle);

    vel[0] =  vel0[0];
    vel[1] =  vel0[1];

    return 0;
}

int Airplane::airplane_deriv()
{
    double forceGravity = mass * acc[1];

    double forceLift = 0.5 * Cl * airDensity * surfaceArea * pow(hypot(vel[0], vel[1]), 2);

    double forceDrag = 0.5 * Cd * airDensity * crossArea * pow(hypot(vel[0], vel[1]), 2);

    double forceY = forceGravity + forceLift;
    double forceX = forceDrag;

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

int Airplane::shutdown()
{
    double t = exec_get_sim_time();
    printf( "========================================\n");
    printf( "      Cannon Ball State at Shutdown     \n");
    printf( "t = %g\n", t);
    printf( "pos = [%.9f, %.9f]\n", pos[0], pos[1]);
    printf( "vel = [%.9f, %.9f]\n", vel[0], vel[1]);
    printf( "========================================\n");
    return 0 ;
}
