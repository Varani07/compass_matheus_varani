FROM condaforge/miniforge3:latest

WORKDIR /app

COPY environment.yaml .

RUN conda env create -f environment.yaml

ENV PATH=/opt/conda/envs/compass_env/bin:$PATH

COPY *.py .

CMD ["python", "main.py"]