#!/bin/bash
mkdir dist
cd items-service/ && poetry build && cp dist/**  ../dist/  && cd ..