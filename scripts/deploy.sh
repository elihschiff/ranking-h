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
cd deployment
docker build -f Dockerfile -t ranking_deploy_2 .
echo \"Done building docker image\"
pwd
docker image ls
whoami



kubectl apply -f ./kubernetes/deployment.yml
# kubectl get all
"
