"""Infrastructure smoke checks; these do not validate a numerical method."""

import importlib

import pytest


@pytest.mark.parametrize("module_name", ["numpy", "scipy", "matplotlib"])
def test_scientific_dependency_imports(module_name):
    importlib.import_module(module_name)


def test_headless_figure_export(tmp_path):
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure

    figure = Figure()
    FigureCanvasAgg(figure)
    axes = figure.subplots()
    axes.set_title("Infrastructure smoke check — no experimental data")
    output = tmp_path / "smoke.png"
    figure.savefig(output)

    assert output.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
