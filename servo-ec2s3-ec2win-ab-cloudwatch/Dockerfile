FROM python:3.6-slim

WORKDIR /servo

# Install dependencies
RUN pip3 install requests PyYAML python-dateutil boto3 && \
	apt-get update && apt-get install -y --no-install-recommends apache2-utils curl

RUN mkdir adjust.d/ encoders/ measure.d/

ADD https://raw.githubusercontent.com/opsani/servo/master/servo \
    https://raw.githubusercontent.com/opsani/servo/master/adjust.py \
    https://raw.githubusercontent.com/opsani/servo/master/measure.py \
    https://raw.githubusercontent.com/opsani/servo-agg/master/adjust \
    https://raw.githubusercontent.com/opsani/servo-agg/master/util.py \
    https://raw.githubusercontent.com/opsani/servo-magg/master/measure \
    /servo/

ADD https://raw.githubusercontent.com/opsani/servo/master/encoders/base.py \ 
    https://raw.githubusercontent.com/kumulustech/encoder-dotnet/master/encoders/dotnet.py \
    /servo/encoders/

ADD https://raw.githubusercontent.com/kumulustech/servo-ec2s3/master/adjust \
    /servo/adjust.d/01ec2s3

ADD https://raw.githubusercontent.com/kumulustech/servo-ec2win/master/adjust \
    /servo/adjust.d/02ec2win

ADD https://raw.githubusercontent.com/opsani/servo-ab/master/measure \
    /servo/measure.d/ab

ADD https://raw.githubusercontent.com/kumulustech/servo-cloudwatch/master/measure \
    /servo/measure.d/cloudwatch

RUN chmod a+rwx /servo/adjust /servo/measure /servo/servo /servo/adjust.d/01ec2s3 /servo/adjust.d/02ec2win /servo/measure.d/ab /servo/measure.d/cloudwatch

RUN sed -i 's/30,         # warmup time in seconds/0,         # warmup time in seconds/' measure.d/ab
RUN sed -i 's/180,         # time limit in seconds/900,         # time limit in seconds/' measure.d/ab

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python3", "servo" ]
