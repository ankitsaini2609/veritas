FROM python:3.8-slim
WORKDIR /veritas
COPY . /veritas
RUN apt update && apt upgrade -y && apt install git -y && \
    pip install -r /veritas/requirements.txt
CMD ["python3", "veritas.py"]