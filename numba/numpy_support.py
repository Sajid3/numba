import numba.core.errors as _errors
from numba.core.utils import PYVERSION as _PYVERSION

_moved_mod = "numba.np.numpy_support"

if _PYVERSION >= (3, 7):
    __getattr__ = _errors.deprecate_moved_module_getattr(__name__, _moved_mod)
else:
    from numba.np.numpy_support import *  # noqa: F403, F401

_errors.deprecate_moved_module(__name__, _moved_mod)
