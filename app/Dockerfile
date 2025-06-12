FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

COPY . .

ENV PATH /opt/conda/envs/gntech/bin:$PATH

# O comando padrão será sobrescrito pelo docker-compose
CMD ["conda", "run", "--no-capture-output", "-n", "gntech", "python", "main.py"]
