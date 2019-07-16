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

# Set up sub dirs
RUN mkdir encoders/ adjust.d/

# Add base servo
ADD https://raw.githubusercontent.com/opsani/servo/master/servo \
    https://raw.githubusercontent.com/opsani/servo/master/adjust.py \
    https://raw.githubusercontent.com/opsani/servo/master/measure.py \
# Add agg servo
    https://raw.githubusercontent.com/opsani/servo-agg/master/adjust \
    https://raw.githubusercontent.com/opsani/servo-agg/master/util.py \
# Add servo-ab (measure)
    https://raw.githubusercontent.com/opsani/servo-ab/master/measure \
    /servo/

# Add ec2win (adjust)
ADD https://raw.githubusercontent.com/kumulustech/servo-ec2win/master/adjust \
    /servo/adjust.d/01ec2win
# Add ec2asg (adjust)
ADD https://raw.githubusercontent.com/opsani/servo-ec2asg/master/adjust \
    /servo/adjust.d/02ec2asg

# TODO: remove when testing complete
RUN sed -i 's/10000000,   # request limit/10000,   # request limit/' measure

# Add base and dotnet encoder
ADD https://raw.githubusercontent.com/opsani/servo/master/encoders/base.py \ 
    https://raw.githubusercontent.com/kumulustech/encoder-dotnet/master/encoders/dotnet.py \
    /servo/encoders/ 

RUN chmod a+rwx /servo/adjust /servo/measure /servo/servo /servo/adjust.d/01ec2win /servo/adjust.d/02ec2asg
RUN chmod a+rw /servo/measure.py /servo/adjust.py /servo/util.py /servo/encoders/base.py /servo/encoders/dotnet.py

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python3", "servo" ]