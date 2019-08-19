# servo-ec2win
_Optune adjust driver for EC2 Windows Instances_

This driver presently updates Windows settings relating to IIS via built-in powershell commands stored on an s3 bucket. It will also adjust the instance type of the ASG launch template as needed. If either adjustment occurs, all instances in under the `asg:` tags will be restarted so that the adjustments will be applied by the userdata of the launch template 

(__NOTE__ order of destroying instances currently does not take into account availability zones which may violate HA requirements)

When the `describe_endpoint` is configured in config.yaml, it must point to a populated json endpoint containing the resulting json from the ps1 script produced by the `encode_describe` method of the dotnet encoder class. __Note__ as new Windows settings are added, their respective `encode_describe` methods must also be implemented in order to keep the describe.ps1 script produced by the encoder up to date

__Note__ this driver requires `adjust.py` base class from the Optune servo core. It can be copied or symlinked here as part of packaging.

__Note__ this driver requires `encoders/base.py` and `encoders/dotnet.py` encoder class from the Optune encoder-dotnet. It can be copied or symlinked here as part of packaging.


# Installation
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


# How to run tests
Prerequisites:
* Python 3.5 or higher
* PyTest 4.3.0 or higher

Follow these steps: (NOTE: small tweaks have been made to the base.py herein that should be backwards compatible)
1. Pull the repository
1. Copy/symlink `adjust` (no file extension) from this repo's project folder to folder `test/`, rename to `adjust.py`
1. Copy/symlink `adjust.py` from `https://github.com/opsani/servo/tree/master/` to folder `test/`, rename to `base_adjust.py`
1. Copy/symlink `base.py` from `https://github.com/opsani/servo/tree/master/encoders` to folder `test/encoders/`
1. Copy/symlink `dotnet.py` from `https://github.com/kumulustech/encoder-dotnet` to folder `test/encoders/`
1. (Note: the two steps above can also be done by symlinking the `encoders/` folder from the above directory to `test/encoders/`)
1. Source your aws_config.env file containing your AWS service key (or ensure your /home/user/.aws folder has a populated credentials file )
1. Run `pytest` from the root folder