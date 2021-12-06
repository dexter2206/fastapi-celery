from python:3.10-slim-buster

RUN adduser webapp
USER webapp

WORKDIR /home/webapp/
ENV PATH="/home/webapp/.local/bin:${PATH}"

RUN pip install --user --upgrade pip
COPY --chown=webapp:webapp ./requirements.txt .
RUN pip install --user -r requirements.txt


COPY --chown=webapp:webapp . .
