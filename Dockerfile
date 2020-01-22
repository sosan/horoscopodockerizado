FROM alpine
RUN apk add --no-cache  python3-dev &&\
                        pip3 install --upgrade pip

# copiar todos los archivos de esta capreta
WORKDIR /app

COPY . /app

RUN pip3 --no-cache  install -r requirements.txt
ENV FLASK_APP=src/main.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5100"]
#  docker cp src ho2:/app
# docker run --name=horo_c -p 81:5100 -v /mnt/hgfs/proyectospython/horoscopoprofe/horoscopoChino/src:/app/src  horoscopo_ima:v1

# https://dzone.com/articles/docker-backup-your-data-volumes-to-docker-hub
# docker tag hor_test:v1 sosan/horo_test:v1
# docker push sosan/horo_test:v1
