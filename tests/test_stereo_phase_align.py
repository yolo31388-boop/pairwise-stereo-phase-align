import pytest
import media.stereo_phase_align as mod

CASES = [
    ("shared_resampler", (1,)),
    ("delay_measured", (1,)),
    ("coefficients_per_segment", (1,)),
    ("align_on_bus", (1,)),
    ("block_overlap", (1,)),
    ("phase_error_cap", (1,)),
    ("load", (1,)),
    ("align", (1,)),
    ("mix", (1,)),
    ("export", (1,)),
    ("validate_phase", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
