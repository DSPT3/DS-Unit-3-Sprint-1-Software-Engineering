docker
docker create --help #or docker COMMAND -help but fill in your own command

docker run hello-world #runs a sample container with some text
docker container ls -a #gives a list of all containers (aka instances)
docker image ls #gives list of images (aka templates)
docker container prune #deletes all containers from workspace

which apk
apk add nano
nano #inside nano make sampletext file and save
ls

docker run -it debian /bin/bash #runs debian container
echo 'sample text in debian' > debian_file
ls
exit #exits out of debian back into general workspace
ls

# Contents of Dockerfile

FROM debian

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pandas numpy && \
pip3 install -i https//test.pypi.org/simple/ lambdata-Krissy && \
python3 -c "import lambdata_Krissy; print('hooray hooray hooray!')"

### Then go back to playground and type

28. docker build . t lambdata


### After build is successful

docker run -it lambdata /bin/bash # Builds lambdata container and puts you in it

python 3 # opens python inside the container

### python code to look at what is in the container

import lambdata_krissy as lambdata
lambdata
dir(lambdata)
lambdata.ONES

quit() #Leaves python
exit #leaves container

ls # returns Dockerfile and sampletex
