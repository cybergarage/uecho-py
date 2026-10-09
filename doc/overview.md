![logo](https://raw.githubusercontent.com/cybergarage/uecho-py/refs/heads/main/doc/img/logo.png)

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/cybergarage/uecho-py)
[![pytest](https://github.com/cybergarage/uecho-py/actions/workflows/pytest.yml/badge.svg)](https://github.com/cybergarage/uecho-py/actions/workflows/pytest.yml)
![](https://img.shields.io/badge/python-3.6-blue.svg)
![](https://img.shields.io/badge/python-3.7-blue.svg)
![](https://img.shields.io/badge/python-3.8-blue.svg)
![](https://img.shields.io/badge/python-3.9-blue.svg)
![](https://img.shields.io/badge/python-3.10-blue.svg)

`uecho-py` is a portable, cross-platform framework for developing [ECHONET Lite][enet] controllers and devices in Python. ECHONET Lite is an open standard for IoT devices in Japan. It defines more than 100 device types, including security sensors, air conditioners, and refrigerators.

`uecho-py` is designed to simplify development of ECHONET Lite devices and controllers on Raspberry Pi. It has also been tested on Raspberry Pi OS.

![](https://raw.githubusercontent.com/cybergarage/uecho-py/main/doc/img/monolight-sense.jpg)

## Installation

Install the `uecho` package with `pip`:

```sh
pip install uecho
```

## Table of Contents

- Controller
  - [Overview of Controller](https://github.com/cybergarage/uecho-py/blob/main/doc/controller_overview.md)
- Device
  - [Overview of Device](https://github.com/cybergarage/uecho-py/blob/main/doc/device_overview.md)
  - [Inside of Device](https://github.com/cybergarage/uecho-py/blob/main/doc/device_inside.md)
- [Examples](https://github.com/cybergarage/uecho-py/blob/main/doc/examples.md)

## Related projects

[uecho-simulator](https://github.com/cybergarage/uecho-simulator) is a small ECHONET Lite development simulator with virtual lighting, air conditioning, and temperature sensing. It provides a full-screen terminal UI and a live, read-only browser preview, runs offline by default, and implements limited device profiles.

## References

* [API documentation (docstrings)](https://cybergarage.github.io/uecho-py/)

[enet]:https://echonet.jp/english/
