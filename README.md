[![Maintainability](https://api.codeclimate.com/v1/badges/83366286ac7b976376a7/maintainability)](https://codeclimate.com/github/agrazh/low-code-API-layer-for-RDBMS/maintainability)
[![Build Status](https://travis-ci.org/agrazh/low-code-API-layer-for-RDBMS.svg?branch=master)](https://travis-ci.org/agrazh/low-code-API-layer-for-RDBMS)

# Low-code API layaer for RDBMS

Flask + SQLAlchemy based low-code API layer to trigger predefined SQL queries and retrieve results.

The intent of this project is to enable data retrieving over API for low-code platforms like Creatio CRM. 

Currently this is just a PoC and many thigs have to be done.

Configuration by using GUI is not available yet, as there is an issue with zombie subprocess [#433](https://github.com/r0x0r/pywebview/issues/433).

Prerequisite: Python 3+

Installation: `make install` or `pip install -r requirements.txt`

Configuration: `app/config.yaml`

Start service: `make start` or `python app/app.py`
