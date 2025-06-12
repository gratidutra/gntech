FROM continuumio/miniconda3:latest

WORKDIR /app

# Copia primeiro o environment.yml para aproveitar cache do Docker
COPY environment.yml .

# Cria o ambiente Conda
RUN conda env create -f environment.yml

# Copia o restante dos arquivos
COPY . .

# Configura o PATH para incluir o ambiente Conda
ENV PATH /opt/conda/envs/gntech/bin:$PATH

# Comando para rodar a aplicação (com --no-capture-output para ver os prints)
CMD ["conda", "run", "--no-capture-output", "-n", "gntech", "python", "-u", "main.py"]