"""Explicit Euler global-error experiment for the student-selected y' = y IVP."""

import csv
import json
import math
from pathlib import Path
import platform
import shlex
import subprocess
import sys

import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


# Dimensionless IVP; fixed interval chosen for this experiment, no randomness.
T_START = 0.0
T_END = 1.0
Y_INITIAL = 1.0
STEP_SIZES = (1.0, 0.5, 0.1, 0.05, 0.01)


def explicit_euler(step_size, end_time=T_END):
    """Integrate y' = y, y(0) = 1 on a uniform grid ending at end_time."""
    if not math.isfinite(step_size) or step_size <= 0:
        raise ValueError("step_size must be finite and positive")
    if not math.isfinite(end_time) or end_time <= T_START:
        raise ValueError("end_time must be finite and positive")
    step_count = round((end_time - T_START) / step_size)
    if step_count < 1 or not math.isclose(
        step_count * step_size, end_time - T_START, rel_tol=1e-12, abs_tol=0.0
    ):
        raise ValueError("step_size must divide the fixed interval")
    times = T_START + np.arange(step_count + 1) * step_size
    values = np.empty(step_count + 1)
    values[0] = Y_INITIAL
    for index in range(step_count):
        values[index + 1] = values[index] + step_size * values[index]
    return times, values


def measure_errors():
    rows = []
    for step_size in STEP_SIZES:
        times, values = explicit_euler(step_size)
        errors = np.abs(np.exp(times) - values)
        maximum_error = float(errors.max())
        order = None
        if rows:
            previous = rows[-1]
            order = math.log(previous["max_error"] / maximum_error) / math.log(
                previous["h"] / step_size
            )
        rows.append({
            "h": step_size,
            "steps": len(times) - 1,
            "y_final": float(values[-1]),
            "endpoint_error": float(errors[-1]),
            "max_error": maximum_error,
            "max_error_over_h": maximum_error / step_size,
            "observed_order": order,
        })
    return rows


def main():
    lab = Path(__file__).resolve().parents[1]
    root = lab.parents[1]
    outputs = lab / "outputs"
    figures = lab / "figures"
    outputs.mkdir(exist_ok=True)
    figures.mkdir(exist_ok=True)
    rows = measure_errors()
    with (outputs / "global_error.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    figure = Figure(figsize=(6.4, 4.8), layout="constrained")
    FigureCanvasAgg(figure)
    axes = figure.subplots()
    steps = np.array([row["h"] for row in rows])
    errors = np.array([row["max_error"] for row in rows])
    axes.loglog(steps, errors, "o-", label="Maximum grid error")
    axes.loglog(steps, steps * errors[-1] / steps[-1], "--", label="Slope 1 reference")
    axes.set(xlabel="Step size h", ylabel="Absolute error", title="Explicit Euler: y' = y, y(0) = 1, T = 1")
    axes.grid(True, which="both", alpha=0.3)
    axes.legend()
    figure.savefig(figures / "global_error.png", dpi=160)

    def git(*arguments):
        return subprocess.check_output(["git", *arguments], cwd=root, text=True).strip()

    metadata = {
        "command": "uv run --locked python " + shlex.join([str(Path(__file__).resolve().relative_to(root)), *sys.argv[1:]]),
        "parameters": {"t_start": T_START, "t_end": T_END, "y_initial": Y_INITIAL, "step_sizes": STEP_SIZES, "units": "dimensionless"},
        "method": "explicit Euler", "reference": "student-supplied exact solution exp(t)",
        "error_measure": "max over all grid nodes of abs(exp(t_n) - y_n)",
        "seed": None, "arithmetic": "float64", "solver_tolerance": None,
        "grid_divisibility_relative_tolerance": 1e-12,
        "python": sys.version, "platform": platform.platform(),
        "numpy": np.__version__, "git_revision": git("rev-parse", "HEAD"),
        "source_tree_dirty": bool(git("status", "--porcelain")),
    }
    (outputs / "global_error_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print("h       N    y(T)          endpoint error  max error      max error/h  order")
    for row in rows:
        order = "—" if row["observed_order"] is None else f"{row['observed_order']:.6f}"
        print(f"{row['h']:<7g} {row['steps']:<4} {row['y_final']:.10f}  {row['endpoint_error']:.8e}  {row['max_error']:.8e}  {row['max_error_over_h']:.6f}     {order}")


if __name__ == "__main__":
    main()
