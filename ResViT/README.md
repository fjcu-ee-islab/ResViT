## ResVIT environment

This paper uses Kuberun to establish the docker environment

Downloads [docker image](https://hub.docker.com/layers/moeaidb/aigo/cu11.1-dnn8.0.5-gpu-pytorch-20.12/images/sha256-d8e407d9e7c4d80434c2957de892f127761dee0be1406c79150f96ef3bdc14b1?context=explore)

Connection method:
Enter IP/KubeRun in the browser, and you can connect to the same network domain. After connecting, you will see the following screen.


login:
Click the login button on the upper right. After logging in, the screen is as follows.
Note: There are two types of KubeRun login identities, administrator and user. Here first log in as an administrator to make settings.

To create a general user, create steps:

To add a new user in the Ubuntu environment, use the command 

```sudo adduser $newuser```

Restart KubeRun to obtain the user UID GID and use the command 

```cd /var/KubernetesUI/ && sudo ./4_startDockerCompose.sh```


```
pip install einops
```


## ResVIT training & test
### ResVit preprocessing
downloads training & test data put in ```./data/train```
```
sh crop.sh
sh cropaug.sh
```
### ResVit training
downloads training & test data put in ```./data/train```
```
sh train.sh
```
### ResVit test
downloads training & test data put in ```./data/train```
```
sh test.sh
```
