FROM condaforge/miniforge3:latest

WORKDIR /workspace

COPY environment.yaml .

RUN conda env update -n base -f environment.yaml