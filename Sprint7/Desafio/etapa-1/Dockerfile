FROM condaforge/miniforge3:latest

WORKDIR /work

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "carregar_dados.py"]
