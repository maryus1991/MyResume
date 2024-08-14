FROM python

WORKDIR /ResumSite

COPY ./req.txt /ResumSite/req.txt
RUN pip install -r req.txt

COPY . /ResumSite


# RUN virtualenv venv
# RUN source venv/bin/activate


EXPOSE 8000

CMD [ "python" , "manage.py","runserver", "0.0.0.0:8000" ]