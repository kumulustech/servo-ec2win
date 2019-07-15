# servo-ec2win
_Optune adjust driver for EC2 Windows Instances_

This driver presently updates IIS server settings in real-time (without server restart) using built-in powershell commands. It does not flush the changes to the configuration file `ec2win.conf`.

__Note__ this driver requires `adjust.py` base class from the Optune servo core. It can be copied or symlinked here as part of packaging.
__Note__ this driver requires `encoders/base.py` and `encoders/dotnet.py` encoder class from the Optune encoder-dotnet. It can be copied or symlinked here as part of packaging.

<!--
## Installation
1. Referring to `config.yaml.example` create file `config.yaml` in driver's folder. It will contain settings you'd want to make adjustable on your Windows Server instance.
1. Referring to `aws_config.env.example` create file `aws_config.env` in driver's folder. It will contain the driver's access key (if only for testing purposes)
1. Alternatively, a configured /home/user/.aws folder can be mounted to the servo container's /root/.aws folder
1. TODO
-->

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