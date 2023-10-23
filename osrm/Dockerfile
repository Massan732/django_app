# Use an official OSRM image as the base image
FROM osrm/osrm-backend

# Copy your OSM data file to the container
RUN wget http://download.geofabrik.de/asia/japan/hokkaido-latest.osm.pbf
COPY ./kansai-latest.osm.pbf /data/kansai-latest.osm.pbf

# Extract, partition, and customize the OSM data
RUN osrm-extract -p /opt/car.lua /data/kansai-latest.osm.pbf
RUN osrm-partition /data/kansai-latest.osrm 
RUN osrm-customize /data/kansai-latest.osrm 

# Expose the OSRM port
EXPOSE 5000

# Command to run OSRM
CMD ["osrm-routed", "--algorithm", "mld", "--max-table-size", "10000", "--max-viaroute-size", "10000", "/data/japan-latest.osrm"]