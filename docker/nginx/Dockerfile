# ベースイメージを選択（Nginxを使用）
FROM nginx:latest

# Nginxの設定ファイルをコピー
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf

# Nginxを起動
CMD ["nginx", "-g", "daemon off;"]