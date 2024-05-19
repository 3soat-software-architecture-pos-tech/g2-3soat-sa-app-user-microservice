ARG FUNCTION_DIR="/function"

FROM python:3.9-slim as build-image

RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev \
    git

ARG FUNCTION_DIR
RUN mkdir -p ${FUNCTION_DIR}

COPY . ${FUNCTION_DIR}

RUN pip install \
        --target ${FUNCTION_DIR} \
        awslambdaric

FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    git

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

RUN pip install \
        --target ${FUNCTION_DIR} \
        -r handlers/find_all_customers/requirements.txt

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD [ "handlers/find_all_customers/find_all_customers_handler.handler" ]