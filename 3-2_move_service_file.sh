#!/bin/bash

sudo mv gpuapp.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable gpuapp.service
sudo systemctl start gpuapp.service
