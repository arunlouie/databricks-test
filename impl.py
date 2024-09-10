#!/bin/bash

# Check if module name is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <module_name>"
    exit 1
fi

# The module name is the first script argument
MODULE_NAME=$1

# Use pip show command to get module info
MODULE_INFO=$(pip show "${MODULE_NAME}")

# Check if pip show returned information about the module
if [ -z "$MODULE_INFO" ]; then
    echo "Module '${MODULE_NAME}' not found."
    exit 1
fi

# Extract Location using grep and awk
LOCATION=$(echo "${MODULE_INFO}" | grep "Location:" | awk '{print $2}')

if [ -n "$LOCATION" ]; then
    echo "Module '${MODULE_NAME}' is installed at: ${LOCATION}"
else
    echo "Location for module '${MODULE_NAME}' not found."
fi
