#include <Python.h>
#if PY_VERSION_HEX >= 0x03000000
extern "C" {

PyObject * PyInit__m6df225a75723545a06d7f08324795258(void) ; /* /home/bahram/trick_sims/SIM_paper_airplane/S_source.hh */
PyObject * PyInit__mf064c256b46431d6a9c6003406b00477(void) ; /* /home/bahram/trick_sims/SIM_paper_airplane/models/airplane/include/Airplane.hh */
PyObject * PyInit__sim_services(void) ;
PyObject * PyInit__top(void) ;
PyObject * PyInit__swig_double(void) ;
PyObject * PyInit__swig_int(void) ;
PyObject * PyInit__swig_ref(void) ;

void init_swig_modules(void) {

    PyImport_AppendInittab("_mf064c256b46431d6a9c6003406b00477", PyInit__mf064c256b46431d6a9c6003406b00477) ;
    PyImport_AppendInittab("_m6df225a75723545a06d7f08324795258", PyInit__m6df225a75723545a06d7f08324795258) ;
    PyImport_AppendInittab("_sim_services", PyInit__sim_services) ;
    PyImport_AppendInittab("_top", PyInit__top) ;
    PyImport_AppendInittab("_swig_double", PyInit__swig_double) ;
    PyImport_AppendInittab("_swig_int", PyInit__swig_int) ;
    PyImport_AppendInittab("_swig_ref", PyInit__swig_ref) ;
    return ;
}

}
#else
extern "C" {

void init_m6df225a75723545a06d7f08324795258(void) ; /* /home/bahram/trick_sims/SIM_paper_airplane/S_source.hh */
void init_mf064c256b46431d6a9c6003406b00477(void) ; /* /home/bahram/trick_sims/SIM_paper_airplane/models/airplane/include/Airplane.hh */
void init_sim_services(void) ;
void init_top(void) ;
void init_swig_double(void) ;
void init_swig_int(void) ;
void init_swig_ref(void) ;

void init_swig_modules(void) {

    init_mf064c256b46431d6a9c6003406b00477() ;
    init_m6df225a75723545a06d7f08324795258() ;
    init_sim_services() ;
    init_top() ;
    init_swig_double() ;
    init_swig_int() ;
    init_swig_ref() ;
    return ;
}

}
#endif
