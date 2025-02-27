import warnings

import cupy
from cupy import testing
import cupyx
import cupyx.scipy.stats  # NOQA

import scipy.stats  # NOQA


atol = {
    'default': 1e-6,
    cupy.float16: 1e-3,
    cupy.float32: 1e-6,
    cupy.float64: 1e-14
}
rtol = {
    'default': 1e-6,
    cupy.float16: 1e-3,
    cupy.float32: 1e-6,
    cupy.float64: 1e-14
}


@testing.with_requires('scipy')
class TestBoxcox_llf:

    @testing.for_all_dtypes(no_float16=True, no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp')
    def test_array_1dim(self, xp, scp, dtype):
        if dtype in (xp.int8, xp.uint8):
            # Test with smaller shape because of tolerance
            shape = 5,
        else:
            shape = 10,
        data = testing.shaped_arange(shape, xp, dtype=dtype)
        lmb = 4.0
        return scp.stats.boxcox_llf(lmb, data)

    @testing.numpy_cupy_allclose(scipy_name='scp', rtol=5e-3)
    def test_array_1dim_float16(self, xp, scp):
        data = testing.shaped_arange((5,), xp, dtype=xp.float16)
        lmb = 4.0
        return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp', atol=atol, rtol=rtol)
    def test_array_2dim(self, xp, scp, dtype):
        data = testing.shaped_arange((3, 8), xp, dtype=dtype)
        lmb = 6.0
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp', atol=atol, rtol=rtol)
    def test_array_3dim(self, xp, scp, dtype):
        data = testing.shaped_arange((10, 3, 4), xp, dtype=dtype)
        lmb = 1.0
        return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp', atol=1e-6, rtol=1e-6)
    def test_array_multi_dim(self, xp, scp, dtype):
        data = testing.shaped_arange((3, 2, 4, 3), xp, dtype=dtype)
        lmb = 9.0
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp', atol=atol, rtol=rtol)
    def test_array_zero_lmb(self, xp, scp, dtype):
        data = testing.shaped_arange((9, 14), xp, dtype=dtype)
        lmb = 0.0
        return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp')
    def test_array_empty(self, xp, scp, dtype):
        data = testing.shaped_arange((0,), xp, dtype=dtype)
        lmb = 1
        return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp', atol=atol, rtol=rtol)
    def test_array_lmb_neg(self, xp, scp, dtype):
        data = xp.array([198.0, 233.0, 233.0, 392.0])
        lmb = -45
        return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp', atol=atol, rtol=rtol)
    def test_array_lmb_neg2(self, xp, scp, dtype):
        data = testing.shaped_arange((3, 5), xp, dtype=dtype)
        lmb = -3.0
        return scp.stats.boxcox_llf(lmb, data)

    @testing.for_all_dtypes(no_bool=True)
    @testing.numpy_cupy_allclose(scipy_name='scp', atol=atol, rtol=rtol)
    def test_array_empty_neg_lmb(self, xp, scp, dtype):
        data = testing.shaped_arange((0,), xp, dtype=dtype)
        lmb = -1.0
        return scp.stats.boxcox_llf(lmb, data)
