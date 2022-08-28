FROM python:3.6
WORKDIR /ui
COPY requirements.txt ./requirements.txt
RUN pip install -r requiremts.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["Home.py"]

