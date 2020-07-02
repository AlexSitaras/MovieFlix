#to leitourgiko pou tha trexei
FROM ubuntu:16.04
#onoma email maintainer     
MAINTAINER ALEX SITARAS <alekosi798@gmail.com>
#run gia update systhmatos
RUN apt-get update
#install thn python sto systhma
RUN apt-get install -y python3 python3-pip 
#install flask pymongo gia thn mongo db 
RUN pip3 install flask pymongo 
#dimiourgia fakelou ap
RUN mkdir /ap
#dimiourgia data mesa ston fakelo ap
RUN mkdir -p /ap/data
#antigrafi ton kodika apo ton ap
COPY movieflix.py /ap/movieflix.py 
#antigrafi tou fakelou me ta templates poy exei o kodikas
COPY templates /ap/templates
#ta topothetei mesa ston data fakelo 
ADD data /ap/data 
#kanei expose thn porta 5003 to container
EXPOSE 5003
#working directory pou einai idios me ton trexon
WORKDIR /ap
#trexei h python ,-u kai o kodikas movieflix otan xekinisi to container
ENTRYPOINT [ "python3","-u", "movieflix.py" ]