"""Method checks use independent references, not an Euler implementation copy."""

import importlib.util
from pathlib import Path

import numpy as np
import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "labs/01-ode-euler/experiments/global_error.py"
spec = importlib.util.spec_from_file_location("global_error", SCRIPT)
experiment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(experiment)


@pytest.mark.parametrize("step_size", experiment.STEP_SIZES)
def test_against_discrete_closed_form(step_size):
    times, values = experiment.explicit_euler(step_size)
    # For this linear IVP the exact discrete sequence is (1+h)^n.
    # 1e-13 relative tolerance allows roundoff over at most 100 float64 steps.
    reference = (1 + step_size) ** np.arange(len(times))
    np.testing.assert_allclose(values, reference, rtol=1e-13, atol=0)
    assert times[-1] == pytest.approx(1.0, abs=1e-14)
    assert len(times) == round(1 / step_size) + 1


def test_error_measure_and_first_order_trend():
    rows = experiment.measure_errors()
    # One Euler step gives y(1)=2; the independent continuous reference is exp(1).
    assert rows[0]["max_error"] == pytest.approx(np.e - 2, abs=1e-14)
    for previous, current in zip(rows, rows[1:]):
        assert current["max_error"] < previous["max_error"]
        assert current["endpoint_error"] == current["max_error"]
    # A finite-resolution trend check, not a proof of asymptotic order:
    # the finest pair is within 5% of the student's predicted first order.
    assert abs(rows[-1]["observed_order"] - 1) < 0.05


@pytest.mark.parametrize("step_size", [0, -0.1, float("nan"), float("inf"), 0.3, 2])
def test_invalid_grids_are_rejected(step_size):
    with pytest.raises(ValueError):
        experiment.explicit_euler(step_size)
