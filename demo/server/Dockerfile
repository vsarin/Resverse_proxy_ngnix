# Base image
FROM nginx:latest

# Remove default Nginx configurations
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/

# Expose ports
EXPOSE 80
EXPOSE 5000
# Start Nginx
CMD ["nginx", "-g", "daemon off;"]

