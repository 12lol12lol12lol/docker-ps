#!/bin/bash
echo "Stop all docker containers!"
docker stop $(docker ps -aq)