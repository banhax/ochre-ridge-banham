**OCHRE RIDGE LITHIUM MINE - JETBOT PIPELINE**  
**AT2 Documentation**  
**Student:** Xavier Banham - 20094400  
**Date:** 13/11/2026  

### 1. Pipeline Overview

This pipeline utilises the camera on a Jetbot robot to drive around a track and stop at obstacles that are in front of it. It does this by taking each frame of the video feed, and processing each between both models (road following, and collision avoidance). These two models interact in the main pipeline notebook, where the robot is stopped when necessary.

### 2. Road Following

|Parameter     | Value | Effect of increasing | Effect of decreasing |
|--------------|-------|----------------------|----------------------|
|Speed gain    |0.12   | Too fast             | Too slow             |
|Steering gain |0.04   | Oversteer            | Understeer           |
|Steering kd   |0.02   | Twitchy steering     | Too slow steering    |
|Steering bias |0.00   | Too far to the right | Too far to the left  |

I arrived at these values by a lot of trial and error, my process to test and tune the values was rather simple and quite brute force; I let the robot move along the track and adjusted the values as I felt was necessary by observing its movements visually.

### 3. Collision Avoidance
|Item                               | Value                                   |
|-----------------------------------|-----------------------------------------|
|Model used                         | Resnet18, two classes (free, blocked)   |
|Training dataset and image counts  | 133 images in total                     |
|Blocked probability threshold      | Greater than 0.6                        |
|Rationale for threshold            | It was a good balance with our dataset  |
|False positive rate at threshold   | 5 percent or lower                      |
|False negative at threshold        | 10-15%                                  |

The classifier is reliable when the road is clear and a flat black colour, with a distinctive enough change in contrast to the obstacle. The classifier degrades when the road's texture isn't as smooth and uniform, as well as if the room is dark.

### 4. Combined Behaviour

Both of the models are running side-by-side, though, whenever a block is detected, execution of the road following model is halted until the collision avoidance model determines that it is no longer blocked. Every time the camera gets a new frame, it runs the base robotLoop (which handles the road following and stopping on obstacle detection).

### 5. Test Evidence
(these were all done in-person at TAFE, so there isn't much variance in lighting and obstacle use)

|Run     |Obstacle and distance|Lighting |Blocked probability at stop|Stopped and resumed|Result|
|--------|---------------------|---------|---------------------------|-------------------|------|
|1       |Duck model           |Well lit | ~75%                      | Yes               | Good |
|2       |Duck model           |Well lit | ~56%                      | Stopped too early | Fail |
|3       |Duck model           |Well lit | N/A                       | Failed to stop    | Fail |
|4       |Duck model           |Well lit | ~70%                      | Yes               | Good |
|5       |Duck model           |Well lit | ~72%                      | Yes               | Good |

Overall, there were 4 successful loops out of the total of 5. With a success rate of 60%.  
You can find the collision-avoidance-notes.md file in the root of the at2-jetbot folder.

### 6. Known Limitations and Edge Cases

1. Road following fails if the steering and speed values are incorrect, or more importantly, the camera is too low or too high.
2. As mentioned above, the classifier failed when contrast was limited (due to inadequate lighting or a non uniform road surface)
3. This current setup is extremely bare-bones and it would not be able to cope if it were suddenly placed into a mine. There would need to be a complete re-training of the model with relevant test data.

### 7. Knowledge Evidence

1. The road following model controls the actual movement and turning of the jetbot, whereas the collision avoidance model either stops or allows movement depending on whether or not it is blocked.

2. I entirely re-trained based off of a data set that we collected ourselves, it required 700+ images for the road following to behave as expected.

3. TensorRT compiles for specific hardware, meaning that if you were training for TensorRT, you would have to train it on the device that you are running it on.

4. The trade off between too relaxed of a threshold is that it may more often miss the obstacles, whereas too strict of one would detect obstacles either too early or things that it shouldn't detect. My threshold was greater than 0.6 = blocked.