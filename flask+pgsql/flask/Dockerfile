#Dockerfile for python

FROM alpine

WORKDIR /prj
COPY . .
RUN apk -v --update add --no-cache python3 py3-pip && python3 -m venv /opt/venv
# python3 -m venv /opt/venv и PATH="/opt/venv/bin:$PATH" используются для предотвращения ошибки pip externally-managed-environment, 
# которая возникает когда устанавливаешь пакеты из ПИП не в виртуальном окружении. Эту ошибку сделали, чтобы исключить запутывание зависимосте
# стандартного менеджера пакетов АПТ(АПК) и ПИП
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install -r requirements.txt

EXPOSE 5050

ENTRYPOINT ["python3","main.py"]