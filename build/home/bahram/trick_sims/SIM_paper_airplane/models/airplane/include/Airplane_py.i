%module mf064c256b46431d6a9c6003406b00477

%include "trick/swig/trick_swig.i"


%insert("begin") %{
#include <Python.h>
#include <cstddef>
%}

%{
#include "/home/bahram/trick_sims/SIM_paper_airplane/models/airplane/include/Airplane.hh"
%}

%trick_swig_class_typemap(Airplane, Airplane)




#ifndef AIRPLANE_H
#define AIRPLANE_H

class Airplane
{
    public:
        double vel0[2] ;    

        double pos0[2] ;    

        double init_speed ; 

        double angle ;      


        double acc[2] ;     

        double vel[2] ;     

        double pos[2] ;     


        bool impact ;       

        double impactTime;  


        double mass;        

        double Cd;          

        double Cl;          


        double surfaceArea;  

        double crossArea;    


        double airDensity;   


        int default_data();
        int initial_data();
        int airplane_deriv();
        int airplane_integ();
        int shutdown();
};
#define TRICK_SWIG_DEFINED_Airplane

#endif
#ifdef TRICK_SWIG_DEFINED_Airplane
%trick_cast_as(Airplane, Airplane)
#endif
