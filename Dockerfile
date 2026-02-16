FROM condaforge/miniforge3:latest

WORKDIR /workspace

COPY environment.yaml .

RUN conda env create -f environment.yaml

ENV PATH=/opt/conda/envs/compass/bin:$PATH