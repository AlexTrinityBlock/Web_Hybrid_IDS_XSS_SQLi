FROM python:3.10-bullseye
WORKDIR /app

# Install python package stack
RUN pip install fastapi==0.100.1
RUN pip install uvicorn[standard]==0.23.1
RUN pip install numpy==1.25.1
RUN pip install pandas==2.0.3
RUN pip install tflite-runtime==2.13.0
RUN pip install tensorflow==2.13.0
RUN pip install typing-extensions==4.7.1
RUN pip install gunicorn==21.2.0
RUN pip install sqlalchemy==2.0.19
RUN pip install openai==0.27.8
RUN pip install SQLAlchemy==2.0.19