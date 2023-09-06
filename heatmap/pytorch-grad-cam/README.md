# AI explainability for PyTorch

| Method              | What it does                                                                                                                |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------|
| GradCAM             | Weight the 2D activations by the average gradient                                                                           |
| GradCAM++           | Like GradCAM but uses second order gradients                                                                                |
| ScoreCAM            | Perbutate the image by the scaled activations and measure how the output drops                                              |
| EigenCAM            | Takes the first principle component of the 2D Activations (no class discrimination, but seems to give great results)        |
| EigenGradCAM        | Like EigenCAM but with class discrimination: First principle component of Activations*Grad. Looks like GradCAM, but cleaner |
| LayerCAM            | Spatially weight the activations by positive gradients. Works better especially in lower layers                             |

## Visual Examples
![image](https://github.com/fjcu-ee-islab/ResViT/blob/main/heatmap/pytorch-grad-cam/example/example.png)

# Running the example script:

```
sh cam.sh
```
# Merge all heamap results into one image

'run the saveall.ipynb'
