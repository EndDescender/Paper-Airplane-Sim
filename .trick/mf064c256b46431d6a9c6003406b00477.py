# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _mf064c256b46431d6a9c6003406b00477
else:
    import _mf064c256b46431d6a9c6003406b00477

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _mf064c256b46431d6a9c6003406b00477.delete_SwigPyIterator

    def value(self):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_equal(self, x)

    def copy(self):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_copy(self)

    def next(self):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_next(self)

    def __next__(self):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator___next__(self)

    def previous(self):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_previous(self)

    def advance(self, n):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _mf064c256b46431d6a9c6003406b00477:
_mf064c256b46431d6a9c6003406b00477.SwigPyIterator_swigregister(SwigPyIterator)


def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    all_keys = [attr for attr in dir(class_type) if not attr.startswith('__')and attr != '_s' ]
    data_keys = sorted(class_type.__swig_setmethods__.keys())
    method_keys = [ x for x in all_keys if x not in data_keys ]
    raise AttributeError("Type %s does not contain member %s.\n%s data = %s\n%s methods = %s" %
     (self.__class__.__name__,name,self.__class__.__name__,data_keys,self.__class__.__name__,method_keys))

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
# this line is changed to handle older swigs that used PySwigObject instead of the current SwigPyObject
        if type(value).__name__ == 'SwigPyObject' or type(value).__name__ == 'PySwigObject' :
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        all_keys = [attr for attr in dir(class_type) if not attr.startswith('__') and attr != '_s' ]
        data_keys = sorted(class_type.__swig_setmethods__.keys())
        method_keys = [ x for x in all_keys if x not in data_keys ]
        raise AttributeError("Type %s does not contain member %s.\n%s data = %s\n%s methods = %s" %
         (self.__class__.__name__,name,self.__class__.__name__,data_keys,self.__class__.__name__,method_keys))

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,1)

class Airplane(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    vel0 = property(_mf064c256b46431d6a9c6003406b00477.Airplane_vel0_get, _mf064c256b46431d6a9c6003406b00477.Airplane_vel0_set)
    pos0 = property(_mf064c256b46431d6a9c6003406b00477.Airplane_pos0_get, _mf064c256b46431d6a9c6003406b00477.Airplane_pos0_set)
    init_speed = property(_mf064c256b46431d6a9c6003406b00477.Airplane_init_speed_get, _mf064c256b46431d6a9c6003406b00477.Airplane_init_speed_set)
    angle = property(_mf064c256b46431d6a9c6003406b00477.Airplane_angle_get, _mf064c256b46431d6a9c6003406b00477.Airplane_angle_set)
    acc = property(_mf064c256b46431d6a9c6003406b00477.Airplane_acc_get, _mf064c256b46431d6a9c6003406b00477.Airplane_acc_set)
    vel = property(_mf064c256b46431d6a9c6003406b00477.Airplane_vel_get, _mf064c256b46431d6a9c6003406b00477.Airplane_vel_set)
    pos = property(_mf064c256b46431d6a9c6003406b00477.Airplane_pos_get, _mf064c256b46431d6a9c6003406b00477.Airplane_pos_set)
    impact = property(_mf064c256b46431d6a9c6003406b00477.Airplane_impact_get, _mf064c256b46431d6a9c6003406b00477.Airplane_impact_set)
    impactTime = property(_mf064c256b46431d6a9c6003406b00477.Airplane_impactTime_get, _mf064c256b46431d6a9c6003406b00477.Airplane_impactTime_set)
    mass = property(_mf064c256b46431d6a9c6003406b00477.Airplane_mass_get, _mf064c256b46431d6a9c6003406b00477.Airplane_mass_set)
    Cd = property(_mf064c256b46431d6a9c6003406b00477.Airplane_Cd_get, _mf064c256b46431d6a9c6003406b00477.Airplane_Cd_set)
    Cl = property(_mf064c256b46431d6a9c6003406b00477.Airplane_Cl_get, _mf064c256b46431d6a9c6003406b00477.Airplane_Cl_set)
    surfaceArea = property(_mf064c256b46431d6a9c6003406b00477.Airplane_surfaceArea_get, _mf064c256b46431d6a9c6003406b00477.Airplane_surfaceArea_set)
    crossArea = property(_mf064c256b46431d6a9c6003406b00477.Airplane_crossArea_get, _mf064c256b46431d6a9c6003406b00477.Airplane_crossArea_set)
    airDensity = property(_mf064c256b46431d6a9c6003406b00477.Airplane_airDensity_get, _mf064c256b46431d6a9c6003406b00477.Airplane_airDensity_set)

    def default_data(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.Airplane_default_data(self, *args)

    def initial_data(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.Airplane_initial_data(self, *args)

    def airplane_deriv(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.Airplane_airplane_deriv(self, *args)

    def airplane_integ(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.Airplane_airplane_integ(self, *args)

    def shutdown(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.Airplane_shutdown(self, *args)

    def __getitem__(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.Airplane___getitem__(self, *args)

    def __len__(self, *args):
        return _mf064c256b46431d6a9c6003406b00477.Airplane___len__(self, *args)

    def __init__(self, **kwargs):
        import _sim_services
        this = _mf064c256b46431d6a9c6003406b00477.new_Airplane()
        try: self.this.append(this)
        except: self.this = this
        if 'TMMName' in kwargs:
            self.this.own(0)
            isThisInMM = _sim_services.get_alloc_info_at(this)
            if isThisInMM:
                _sim_services.set_alloc_name_at(this, kwargs['TMMName'])
            else:
                _sim_services.TMM_declare_ext_var(this, _sim_services.TRICK_STRUCTURED, "Airplane", 0, kwargs['TMMName'], 0, None)
            alloc_info = _sim_services.get_alloc_info_at(this)
            alloc_info.stcl = _sim_services.TRICK_LOCAL
            alloc_info.alloc_type = _sim_services.TRICK_ALLOC_NEW


    __swig_destroy__ = _mf064c256b46431d6a9c6003406b00477.delete_Airplane

# Register Airplane in _mf064c256b46431d6a9c6003406b00477:
_mf064c256b46431d6a9c6003406b00477.Airplane_swigregister(Airplane)


def castAsAirplane(*args):
    return _mf064c256b46431d6a9c6003406b00477.castAsAirplane(*args)


