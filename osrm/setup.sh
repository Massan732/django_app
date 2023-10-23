# OSRMのDockerイメージを取得
docker pull osrm/osrm-backend

# 関西圏のオープンストリートマップを取得
sudo apt install wget
sudo wget -O ./data/kansai-latest.osm.pbf http://download.geofabrik.de/asia/japan/kansai-latest.osm.pbf

# OSRMの初期設定
docker run --rm -t -v "${PWD}/data:/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/kansai-latest.osm.pbf
docker run --rm -t -v "${PWD}/data:/data" osrm/osrm-backend osrm-partition /data/kansai-latest.osrm
docker run --rm -t -v "${PWD}/data:/data" osrm/osrm-backend osrm-customize /data/kansai-latest.osrm