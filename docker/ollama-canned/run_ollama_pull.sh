#!/bin/bash


ollama serve &
SERVER_PID=$!

# Wait for the server to start
while ! nc -z localhost 11434; do   
  sleep 0.1 # wait for 100ms before check again
done

echo "pulling $1"
ollama pull $1

kill $SERVER_PID
