PASSWORD=$1

if [[ -z "${PASSWORD}" ]]; then
  echo "Password missing"
  exit 1
fi

echo "sshing to server to ensure deployment folder exists"
sshpass -p $PASSWORD ssh -o StrictHostKeyChecking=no schife@team-h.cs.rpi.edu "
pwd
rm -rf deployment
mkdir deployment
cd deployment
pwd
"

echo "copying code to remote server"
sshpass -p $PASSWORD rsync -r -v --progress . schife@team-h.cs.rpi.edu:~/deployment

echo "Connecting to server and running commands"
sshpass -p $PASSWORD ssh schife@team-h.cs.rpi.edu "

export DOCKER_TLS_VERIFY=\"1\"
export DOCKER_HOST=\"tcp://192.168.49.2:2376\"
export DOCKER_CERT_PATH=\"/home/schife/.minikube/certs\"
export MINIKUBE_ACTIVE_DOCKERD=\"minikube\"

docker images

cd deployment
docker build -f Dockerfile -t ranking_deploy .
echo \"Done building docker image\"

echo \"Applying kubernetes yaml\"
kubectl apply -f ./kubernetes/deployment.yml
kubectl rollout restart deployment ranking
"
