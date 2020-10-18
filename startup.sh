#/bin/bash

echo "start statup.sh"

DIR="$( cd "$( dirname "/deaddict/startup.sh" )" >/dev/null 2>&1 && pwd )"

echo current $DIR

python3 -m pip3 install -r requirements.txt

export FLASK_APP="startup:app"
gunicorn --bind=0.0.0.0 --timeout 600 "startup:app"

echo "startup.sh"
