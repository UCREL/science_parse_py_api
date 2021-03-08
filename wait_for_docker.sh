#!/bin/bash

while [ $(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080) != "200" ]; do
	sleep 10
	echo "Waiting"
done

echo "Completed"
