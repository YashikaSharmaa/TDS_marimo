# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.18.1"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    #24f2001055@ds.study.iitm.ac.in
    a = 12
    return


@app.cell
def _():
    b = 10
    return


@app.cell
def _(mo):
    # Add interactive widget
    slider = mo.ui.slider(1, 100)
    return (slider,)


@app.cell
def _(mo, slider):
    # Create dynamic Markdown
    mo.md(f"{slider} {'🟢' * slider.value}")
    return


if __name__ == "__main__":
    app.run()
