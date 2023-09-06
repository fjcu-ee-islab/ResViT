## ResVIT environment

This paper uses Kuberun to establish the docker environment

Downloads [docker image](https://hub.docker.com/layers/moeaidb/aigo/cu11.1-dnn8.0.5-gpu-pytorch-20.12/images/sha256-d8e407d9e7c4d80434c2957de892f127761dee0be1406c79150f96ef3bdc14b1?context=explore)
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
