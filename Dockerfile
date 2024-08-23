# Dockerfile
FROM python:3.11-slim

# Atualiza pip
RUN pip install --upgrade pip

# Instala dependências
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia o código da aplicação
COPY app.py app.py

# Expõe a porta 80
EXPOSE 80

# Comando para rodar a aplicação
CMD ["python", "app.py"]




