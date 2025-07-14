#!/bin/bash

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"
cd /home/kai/myapp/api
exec uvicorn apis:app --host 0.0.0.0 --port 8404
