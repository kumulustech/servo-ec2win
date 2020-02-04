# TODO: remove ec2s3 artifacts
# servo-ec2win

_Optune adjust driver for EC2 Instances_

This driver  updates the instance type of the configued ASG(s) launch template(s) and/or config(s). On each adjustment iteration, all instances in under the `asg:` tags will be terminated in batches, waiting for the new instances to be ready before moving to the next batch. During readyness checking, this driver supports an optional external validator from another driver (such as servo-ec2s3) via the `validator` section of the config. When specified, the `validator` must inidicate the file name from which the static `get_validator()` method will be imported and invoked (see: config.yaml.example)

__Note__ order of destroying instances currently does not take into account availability zones which may violate HA requirements

## Required IAM Permissions

The account provided for the servo requires the following permissions:

EC2 Permissions

- ec2:DescribeInstances - can be exluded if describe_endpoint is not used
- ec2:TerminateInstances
- ec2:DescribeLaunchTemplateVersions - can be exluded when using only launch configs
- ec2:CreateLaunchTemplateVersion - can be exluded when using only launch configs
- ec2:DescribeInstanceStatus

IAM Permissions

- iam:PassRole - Must apply to any instance profile associated with the target instances, can be exluded when only launch templates are used or if launch configs do not specify an instance profile

Autoscaling Permissions

- autoscaling:CreateLaunchConfiguration - can be exluded when using only launch templates
- autoscaling:DescribeAutoScalingGroups
- autoscaling:DescribeLaunchConfigurations - can be exluded when using only launch templates
- autoscaling:UpdateAutoScalingGroup - can be exluded when using only launch templates

## Installation

```bash
docker build -t opsani/servo-ec2win-ab servo/

docker run -d --name opsani-servo \
    -v /path/to/optune_auth_token:/opt/optune/auth_token \
    -v /path/to/config.yaml:/servo/config.yaml \
    opsani/servo-ec2win-ab --auth-token /opt/optune/auth_token --account my_account my_app
```

Where:

- `/path/to/optune_auth_token` - file containing the authentication token for the Optune backend service
- `/path/to/config.yaml` - config file containing (see above for details).
- `my_account` - your Optune account name
- `my_app` - the application name

## How to run tests with ec2s3 validator and dotnet encoder

Prerequisites:

- Python 3.5 or higher
- PyTest 4.3.0 or higher

Follow these steps:

1. Pull the repository
1. Copy/symlink `adjust` (no file extension) from this repo's project folder to folder `test/`, rename to `adjust_driver.py`
1. Copy/symlink `adjust.py` from `https://github.com/opsani/servo` to folder `test/`
1. (Optional) Copy/symlink `adjust` (no file extension) from  `https://github.com/kumulustech/servo-ec2s3` to folder `test/`, rename to `validation_driver`
1. Copy/symlink `base.py` from `https://github.com/opsani/servo/tree/master/encoders` to folder `test/encoders/`
1. Copy/symlink `dotnet.py` from `https://github.com/kumulustech/encoder-dotnet` to folder `test/encoders/`
1. Source your aws_config.env file containing your AWS service key (or ensure your /home/user/.aws folder has a populated credentials file )
    1. The account used must have the servo permissions detailed above
1. Add a valid `config.yaml` to folder `test/` (see config.yaml.example for a reference)
1. Run `python3 -m pytest` from the test folder
