FROM condaforge/miniforge3:latest

WORKDIR /workspace

RUN pip install --upgrade pip

RUN pip install \
    python-dotenv \
    pandas \
    numpy \
    matplotlib \
    inputimeout \
    boto3