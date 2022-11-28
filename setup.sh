#!/bin/bash

set -euo pipefail

env_dir=.venv

python3 -m venv "${env_dir}"

source "${env_dir}/bin/activate"

pip install .

echo "Success"