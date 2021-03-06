# adapted from https://github.com/opsani/servo-ec2asg-newrelic/blob/master/Dockerfile
FROM python:3.6-slim

WORKDIR /servo

# Install dependencies (use latest pip packages)
# hadolint ignore=DL3013
RUN apt-get update && apt-get install -y --no-install-recommends apache2-utils curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install requests PyYAML python-dateutil boto3

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
# RUN sed -i 's/10000000,   # request limit/100,   # request limit/' measure
RUN sed -i 's/30,         # warmup time in seconds/0,         # warmup time in seconds/' measure

RUN chmod a+rwx /servo/adjust /servo/measure /servo/servo

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python3", "servo" ]