# Deconvolution-based-on-SVR
The method was created and based on the citation "Deconvolution of bulk gene expression profiles from complex tissues to quantify the subsets of immune cells".
The tool is to estimate the fraction of immune cells. Immune cells contain CD8 T cells, CD4 T cells, alternatively activated macrophages, classically activated macrophages, Regulatory T cells, T helper cells, Natural killer ells, Dendritic cells.

# Requirements
* R
* python 3

# Tutorial

The gene in `Pre.reference.csv` is in order to estimate the fraction of immune cells. Before analysis you might run `pre-process.R`, it deal with duplicate genes in the input data. The ``pre-process.R` and `Reference.csv` are provided by `pre-process.R`. Finally run `SCORE.py`, you will obtain `score.csv`, `bar.pdf` and `boxplot.dpf`. The visualization of the fraction of immune cells depends on `bar.pdf` and `boxplot.pdf`. The fraction of immune cells you can find it in `score.csv`.

## Run

    Rscript pre-process.R -i "input data name"

    python SCORE.py

## Contribution
