# servo-ec2win

_Optune adjust driver for EC2 Instances_

This driver presently updates settings of EC2 instances using commands stored on an s3 bucket. The types of commands and supported EC2 targets are dependent on the bundled encoder. It will also adjust the instance type of the ASG launch template or config as needed. On each adjustment iteration, all instances in under the `asg:` tags will be terminated in batches, waiting for the new instances to be ready before moving to the next batch.

__Note__ order of destroying instances currently does not take into account availability zones which may violate HA requirements

__Note__ this driver requires `adjust.py` and `encoders/base.py` base classes from the [Optune servo core](https://github.com/opsani/servo/). They can be copied or symlinked here as part of packaging. 

__Note__ An encoder class will also be required. While this driver is mostly intended for use with the [dotnet encoder class](https://github.com/kumulustech/encoder-dotnet/) (`encoders/dotnet.py`), other encoders based on the Opsani base should be compatible. See `servo/Dockerfile` and `servo-jvm/Dockerfile` in this repo for examples

When the `describe_endpoint` is configured in config.yaml, it must point to a web endpoint populated with content that is parsable by the bundled encoder. Once retrieved and parsed, the endpoint data is used to verify the settings have taken effect. (__Note__ the text encoding of the endpoint is currently expected to be UTF_16LE).

When `describe_endpoint` is used with the dotnet encoder, the endpoint contains resulting json from the ps1 script produced by the `encode_describe` method of said dotnet encoder class. __Note__ as new Windows settings are added, their respective `encode_describe` methods must also be implemented in order to keep the describe.ps1 script produced by the encoder up to date. See `describe_endpoint_dotnet.ps1.example` and `user_data_dotnet.example` for usage

## Installation (encoder-dotnet)

1. Echo optune token into docker secret: `echo -n 'YOUR AUTH TOKEN' | docker secret create optune_auth_token -`
1. Run `docker build servo/ -t example.com/servo-ec2win-ab`
1. Referring to `config.yaml.example` create file `config.yaml` in driver's folder. It will contain settings you'd want to make adjustable on your Windows Server instance.
1. Create `.aws` folder with needed credential and permission
1. Create a docker service:

```
docker service create -t
    --name DOCKER_SERVICE_NAME \
    --secret optune_auth_token \
    --env AB_TEST_URL= APACHED_BENCHMARK_URL \
    --mount type=bind,source=/PATH/TO/config.yaml,destination=/servo/config.yaml \
    --mount type=bind,source=/PATH/TO/.aws/,destination=/root/.aws/ \
    example.com/servo-ec2win-ab \
    APP_NAME  \
    --account USER_ACCOUNT \
```

## How to run tests with dotnet encoder

Prerequisites:

* Python 3.5 or higher
* PyTest 4.3.0 or higher

Follow these steps:

1. Pull the repository
1. Copy/symlink `adjust` (no file extension) from this repo's project folder to folder `test/`, rename to `adjust.py`
1. Copy/symlink `adjust.py` from `https://github.com/opsani/servo/tree/master/` to folder `test/`, rename to `base_adjust.py`
1. Copy/symlink `base.py` from `https://github.com/opsani/servo/tree/master/encoders` to folder `test/encoders/`
1. Copy/symlink `dotnet.py` from `https://github.com/kumulustech/encoder-dotnet` to folder `test/encoders/`
1. Source your aws_config.env file containing your AWS service key (or ensure your /home/user/.aws folder has a populated credentials file )
1. Run `pytest` from the root folder
