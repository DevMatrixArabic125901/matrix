FROM qithoniq/matrix:slim-buster

RUN git clone https://github.com/qithoniq/matrix.git /root/matrix

WORKDIR /root/matrix

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/matrix/bin:$PATH"

CMD ["python3","-m","matrix"]
