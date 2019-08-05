# adapted from https://github.com/opsani/servo-ec2asg-newrelic/blob/master/Dockerfile
FROM python:3.6-slim

WORKDIR /servo

# Install dependencies
RUN pip3 install requests PyYAML python-dateutil boto3 && \
	apt-get update && apt-get install -y --no-install-recommends \
    apache2-utils \
    python3-boto \
    python3-botocore

# Change /usr/bin/python3 => /usr/local/bin/python3, since the first is older,
# so that import of boto3 works
RUN rm -f /usr/bin/python3 && \
	ln -s /usr/local/bin/python3 /usr/bin/python3

RUN mkdir encoders/

# Install servo:  ec2win adjust (which uses the servo base adjust.py) and
# apache benchmark measure (which uses the servo base measure.py) and
# dotnet encoder (which users encoders/base.py)
ADD https://raw.githubusercontent.com/opsani/servo/master/servo \
    https://raw.githubusercontent.com/opsani/servo/master/adjust.py \
    https://raw.githubusercontent.com/opsani/servo/master/measure.py \
    https://raw.githubusercontent.com/kumulustech/servo-ec2win/master/adjust \
    https://raw.githubusercontent.com/opsani/servo-ab/master/measure \
    /servo/

# TODO: remove when testing complete
RUN sed -i 's/10000000,   # request limit/100,   # request limit/' measure
RUN sed -i 's/30,         # warmup time in seconds/0,         # warmup time in seconds/' measure

ADD https://raw.githubusercontent.com/opsani/servo/master/encoders/base.py \ 
    https://raw.githubusercontent.com/kumulustech/encoder-dotnet/master/encoders/dotnet.py \
    /servo/encoders/ 

RUN chmod a+rwx /servo/adjust /servo/measure /servo/servo
RUN chmod a+rw /servo/measure.py /servo/adjust.py encoders/base.py encoders/dotnet.py

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python3", "servo" ]