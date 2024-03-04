#!/bin/bash

total_steps=100

for ((i=1; i<=total_steps; i++)); do
    # Your script logic here
    
    # Calculate percentage completion
    percentage=$((i * 100 / total_steps))
    
    # Print progress bar
    printf "\rProgress: [%-50s] %d%%" "$(printf '#%.0s' $(seq 1 $((i * 50 / total_steps))))" "$percentage"
    
    # Optional: Sleep to slow down the loop for demonstration purposes
    sleep 0.1
done

echo -e "\nScript completed!"
