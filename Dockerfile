FROM continuumio/anaconda3

WORKDIR /mle-training

COPY . .

COPY env.yml .

RUN conda env create -f env.yml

RUN conda init bash

RUN echo 'conda activate mle-dev' > ~/.bashrc

CMD ["python", "tests/testing_docker.py"]