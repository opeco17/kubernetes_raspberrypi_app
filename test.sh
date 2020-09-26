sudo docker build -t opeco17/web_nginx ./web_nginx
kubectl delete -f web.yaml
kubectl apply -f web.yaml
