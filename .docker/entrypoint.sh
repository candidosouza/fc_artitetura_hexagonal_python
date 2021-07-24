#!/bin/bash

cp .env.example .env
python manager.py runserver 0.0.0.0:8000
