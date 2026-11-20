**OCHRE RIDGE LITHIUM MINE - JETBOT VLM PIPELINE**  
**AT3 Documentation**  
**Student:** Xavier Banham - 20094400  
**Date:** 19/11/2026  

### 1. Pipeline Overview  
The pipeline functions by running two models beside each other, these are running on the JetBot itself. They both interface at one point in the Jypiter notebook, where if the collision avoidance model believes it is blocked, the robot then sends the image (where it thinks it is blocked) to Llava (by the python requests module). Llava is hosted on one of the TAFE computers, which is hosting a Flask webserver so that it may recieve POST requests from the JetBot (containing the image data).

The webserver hands the data over to Llava where it has been prompted to format a JSON response with a verdict of either 'BLOCKED' or 'FREE', and is told to answer whether or not there are any obstacles on the road in the image. The Flask server takes the result, and sends it back to the Jetbot which is translated into either True or False. If the answer was True, then the JetBot stops, if the answer was False, then the JetBot keeps driving.

### 2. System Architecture  

1. JetBot Camera  
2. Road Following & Collision Avoidance  
3. Drive until blocked above 0.5 threshold  
4. Send camera frame where 'blocked' to the webserver via POST request  
5. Process the answer and recieve it back > Either stop or keep driving  
6. Repeat  

### 3. VLM Configuration  

| Parameter       | Value    | Notes |
|-----------------|----------|-------|
| Model           | llava:7b |  N/A  |
| Prompt strategy | N/A      | "Examine the image and determine whether or not the road is blocked by an obstacle. The road should be considered 'BLOCKED' when there is ANYTHING on the road as the vehicle on the road is unable to turn. Only when the road is entirely clear, should the road be considered 'FREE'. Format your response into JSON with the provided format template. The value for 'llava_verdict' should ONLY be either 'BLOCKED' or 'FREE'. The value for 'action' should ONLY be either 'STOP' or 'KEEP DRIVING'. The value for 'description' should ONLY be a single short sentence explanation of what you see in the image. The value for 'objected_detected' should be a short and concise name of the object with no prose. All other values should remain UNCHANGED." |
| Classifier threshold | >= 5.0 is blocked | Good middle ground |
| Inference time per frame | 23660611600 | Far too long |
| Frames per minute | less than ~10 | The latency with this setup was far too great to meaningfully measure (robot lacking processing power, slow internet, etc.) |

### 4. Data Classification and Security  
There isn't any classification other than 'yes there is an obstacle', or 'no there is not an obstacle'. The data isn't stored anywhere, as soon as it has been used it is gone. The VLM processes the image sent via POST, and it is not saved or stored anywhere.

### 5. Sample Output
A sample of the JSON output provided by the model is as follows...

The webserver shows the POST requests, and the model's response like so:

BLOCKED OUTPUT
```json
{
    'timestamp': '2026-11-20T15:26:25.822538', 
    'location': 'Testing track', 
    'trigger': 'Collision avoidance above threshold', 
    'classifier_blocked_prob': 0.994140625, 
    'llava_verdict': 'BLOCKED', 
    'action': 'STOP', 
    'description': 'An obstacle is blocking the road, causing the vehicle to stop' 
    'object_detected': 'Duck'
}
```

FREE OUTPUT
```json
{
    'timestamp': '2026-11-20T15:27:20.553472', 
    'location': 'Testing track', 
    'trigger': 'Collision avoidance above threshold', 
    'classifier_blocked_prob': 0.984375, 
    'llava_verdict': 'FREE', 
    'action': 'KEEP DRIVING', 
    'description': 'No obstacles on the road', 
    'object_detected': 'None'
}
```

### 6. Known Limitations
1. There is astounding latency with the process of sending an image and awaiting a result.
2. The robot physically is unable to stop in enough time due to the lag on processing frames.
3. The 2GB JetBot does not have enough processing power to facilitate running two models on it at once effectively, and with the extra lag of waiting for a VLM to respond via HTTP, this solution is infeasible.
4. Llava seems to enjoy answering incorrectly from time to time, so some level of exception-handling is necessary
