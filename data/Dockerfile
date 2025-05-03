# Use a minimal Debian-based image
FROM debian:stable-slim

# Set non-interactive mode for apt to avoid prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies, Azure CLI, Azurite, and a shell
RUN apt-get update && apt-get install -y \
    curl apt-transport-https lsb-release gnupg software-properties-common bash \
    && curl -sL https://aka.ms/InstallAzureCLIDeb | bash \
    && apt-get install -y nodejs npm \
    && npm install -g azurite \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy initialization script into the container
COPY . /data/

# Make the script executable
RUN chmod +x /data/init_azurite_data.sh

# Expose Azurite ports
EXPOSE 10000 10001 10002

# Run the initialization script and start Azurite
CMD ["/bin/bash", "/data/init_azurite_data.sh"]