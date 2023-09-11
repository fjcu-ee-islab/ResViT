## ResVIT environment

This paper uses Kuberun to establish the docker environment

Downloads [docker image](https://hub.docker.com/layers/moeaidb/aigo/cu11.1-dnn8.0.5-gpu-pytorch-20.12/images/sha256-d8e407d9e7c4d80434c2957de892f127761dee0be1406c79150f96ef3bdc14b1?context=explore)

Connection method:
Enter IP/KubeRun in the browser, and you can connect to the same network domain. After connecting, you will see the following screen.


login:
Click the login button on the upper right. After logging in, the screen is as follows.
Note: There are two types of KubeRun login identities, administrator and user. Here first log in as an administrator to make settings.

![image](https://github.com/fjcu-ee-islab/ResViT/blob/main/ResViT/kuberun/login.png)

The working environment started from this interface uses the upper limit of CPU and memory.

To add a new user in the Ubuntu environment, use the command 

```sudo adduser $newuser```

Restart KubeRun to obtain the user UID GID and use the command 

```cd /var/KubernetesUI/ && sudo ./4_startDockerCompose.sh```

Add a new user, the screen is as follows. The account is the user added in step 1, the password can be set by yourself, and click Get UID
GID button.
MAX GPU In order to give the user the maximum number of GPUs that can be used at the same time, special attention is required. This UI GPU has
exclusive,
If the GPU is used by one user, it cannot be used by another user.
The Pending number is the upper limit of the number of concurrent schedules for this user.

![image](https://github.com/fjcu-ee-islab/ResViT/blob/main/ResViT/kuberun/adduser.png)

### image:

image (image file) is similar to the master film of docker, one image can create many dockers for different tasks
Add or create docker images, here take pull moeaidb/aigo:cu11.1-dnn8.0.5-gpu-pytorch-cv-20.12 as an example, as follows.

![image](https://github.com/fjcu-ee-islab/ResViT/blob/main/ResViT/kuberun/pullimage.png)

The result after successful pull is as follows.

![image](https://github.com/fjcu-ee-islab/ResViT/blob/main/ResViT/kuberun/pulldone.png)

### Custom image:

To create a docker image that can be used by each user, you must first perform the above steps to create the user and obtain the docker image to be given to the user, as follows.

![image](https://github.com/fjcu-ee-islab/ResViT/blob/main/ResViT/kuberun/custom.png)

After entering the environment, you need to install einops :
```
pip install einops
```

If you don’t have kuberun, please install the docker environment yourself

## ResVIT training & test

Downloads [training data]()

downloads training & test data put in ```./data/train```

### ResVit preprocessing

Use ```datapick.ipynb``` to select the OCT angle to train 

Run the following sh file to complete data augmentation

Parameters of crop.sh & cropsug.sh: 

rpath is the path to read the original file

spath is the storage file path after corp
                       
```
sh crop.sh
sh cropaug.sh
```
### ResVit training

Run the following sh file to complete training

Parameters of train.sh:

classname is the category name

path is the path of the training data 

num_classe is the number of categories

pick is the name of the folder where the weights are stored
```
sh train.sh
```
### ResVit test

```
sh test.sh
```
