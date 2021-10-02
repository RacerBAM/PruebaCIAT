FROM       python:3.6-alpine
RUN        pip install json
COPY       ./DesarrolloPrueba/
EXPOSE     8080
WORKDIR    /DesarrolloPrueba
ENTRYPOINT ["python", "sistema.py"]