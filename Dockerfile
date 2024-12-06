FROM nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.6.1tw 

WORKDIR ./

COPY requirements.txt ./
RUN apt-get install python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . ./agri

CMD ["/bin/bash", "./agri/start.sh"]
