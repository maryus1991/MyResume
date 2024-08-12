FROM django

WORKDIR /Django_Project/MyResumProject

COPY . /Django_Project/MyResumProject

RUN pip install -r req.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver" ]
