#!/bin/bash
echo "Remove all containers!"
docker rm $(docker ps -aq)
