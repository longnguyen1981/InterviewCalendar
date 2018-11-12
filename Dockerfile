FROM python:3

MAINTAINER  Long Nguyen <hoanglong2k@gmail.com>

WORKDIR /usr/src/app

RUN apt-get update

COPY run_api.py requirements.txt setting.py /usr/src/app/
COPY company              /usr/src/app/company

RUN pip3 install -r requirements.txt
EXPOSE 7000
CMD [ "python3", "/usr/src/app/run_api.py"]
