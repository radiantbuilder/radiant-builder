#!/bin/bash

# Update package lists
sudo apt-get update

# Install Nginx web server
sudo apt-get install -y nginx

# Create a simple HTML file
echo "<html><body><h1>Welcome to RadiantBuilder</h1></body></html>" | sudo tee /var/www/html/index.html

# Start the Nginx service
sudo systemctl start nginx

# Enable Nginx to start on boot
sudo systemctl enable nginx

echo "Application deployed successfully!"
