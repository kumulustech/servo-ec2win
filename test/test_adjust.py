import pytest

import sys
import io

from adjust import Ec2WinDriver, DESC, HAS_CANCEL, VERSION

adjust_json_stdin = '''\
{
    "application": {
        "components": {
            "web": {
                "settings": {
                    "UriEnableCache": {"value": 1},
                    "UriScavengerPeriod": {"value": 260},
                    "WebConfigCacheEnabled": {"value": 0},
                    "WebConfigEnableKernelCache": {"value": 1}
                }
            },
            "ws2012-sandbox-asg": {
                "settings": {
                    "inst_type": {"value": "t2.nano"}
                }
            }
        }
    }
}
'''

def test_version(monkeypatch):
    with monkeypatch.context() as m:
        # replicate command line arguments fed in by servo
        m.setattr(sys, 'argv', ['', '--version', '1234'])
        driver = Ec2WinDriver(cli_desc=DESC, supports_cancel=HAS_CANCEL, version=VERSION)
        with pytest.raises(SystemExit) as exit_exception:
            driver.run()
        assert exit_exception.type == SystemExit
        assert exit_exception.value.code == 0

def test_info(monkeypatch):
    with monkeypatch.context() as m:
        # replicate command line arguments fed in by servo
        m.setattr(sys, 'argv', ['', '--info', '1234'])
        driver = Ec2WinDriver(cli_desc=DESC, supports_cancel=HAS_CANCEL, version=VERSION)
        with pytest.raises(SystemExit) as exit_exception:
            driver.run()
        assert exit_exception.type == SystemExit
        assert exit_exception.value.code == 0

def test_query(monkeypatch):
    with monkeypatch.context() as m:
        # replicate command line arguments fed in by servo
        m.setattr(sys, 'argv', ['', '--query', '1234'])
        driver = Ec2WinDriver(cli_desc=DESC, supports_cancel=HAS_CANCEL, version=VERSION)
        with pytest.raises(SystemExit) as exit_exception:
            driver.run()
        assert exit_exception.type == SystemExit
        assert exit_exception.value.code == 0

def test_adjust(monkeypatch):
    with monkeypatch.context() as m:
        # replicate command line arguments fed in by servo
        m.setattr(sys, 'argv', ['', '1234'])
        m.setattr(sys, 'stdin', io.StringIO(adjust_json_stdin))
        driver = Ec2WinDriver(cli_desc=DESC, supports_cancel=HAS_CANCEL, version=VERSION)
        driver.run()
        assert True
