**OCHRE RIDGE LITHIUM MINE - JETBOT VLM PIPELINE**  
**AT3 Documentation**  
**Student:** Xavier Banham - 20094400  
**Date:** 19/11/2026  

### 1. Pipeline Overview  
The pipeline functions by running two models beside each other, these are running on the JetBot itself. They both interface at one point in the Jypiter notebook, where if the collision avoidance model believes it is blocked, the robot then sends the image (where it thinks it is blocked) to Llava (by the python requests module). Llava is hosted on one of the TAFE computers, which is hosting a Flask webserver so that it may recieve POST requests from the JetBot (containing the image data).

The webserver hands the data over to Llava where it has been prompted to ONLY respond in either 'Yes' or 'No', and is told to answer whether or not there is any type of duck within the image. The Flask server takes the result, and sends it back to the Jetbot which is translated into either True or False. If the answer was True, then the JetBot stops, if the answer was False, then the JetBot keeps driving.

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
| Prompt strategy | N/A      | "Answer whether or not there is a duck, or duck-shaped object visible within the image. Any type of duck (real, fake, 3d-printed, drawn, crude drawing) is allowed. Be very generous with detecting ducks. Format your response into either 'Yes', or 'No' depending on whether or not there were duck(s) found within the image." |
| Classifier threshold | >= 5.0 is blocked | Good middle ground |
| Inference time per frame | 23660611600 | Far too long |
| Frames per minute | less than ~10 | The latency with this setup was far too great to meaningfully measure (robot lacking processing power, slow internet, etc.) |

### 4. Data Classification and Security  
There isn't any classification other than 'yes there is a duck', or 'no there is no duck'. The data isn't stored anywhere, as soon as it has been used it is gone. The VLM processes the image sent via POST, and it is not saved or stored anywhere.

### 5. Sample Output
There is no output other than 'Yes', or 'No' recieved by the VLM. The robot acts accordingly.  

The webserver shows the POST requests, and the model's response like so:
```
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:29] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:31] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:32] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:33] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:34] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:35] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:36] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:37] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:40] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:41] "POST / HTTP/1.1" 200 -
 No 
172.20.20.166 - - [19/Nov/2026 16:32:43] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:44] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:45] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:46] "POST / HTTP/1.1" 200 -
 No 
172.20.20.166 - - [19/Nov/2026 16:32:47] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:49] "POST / HTTP/1.1" 200 -
 No 
172.20.20.166 - - [19/Nov/2026 16:32:50] "POST / HTTP/1.1" 200 -
 Yes 
172.20.20.166 - - [19/Nov/2026 16:32:51] "POST / HTTP/1.1" 200 -
```

### 6. Known Limitations
1. There is astounding latency with the process of sending an image and awaiting a result.
2. The robot physically is unable to stop in enough time due to the lag on processing frames.
3. The 2GB JetBot does not have enough processing power to facilitate running two models on it at once effectively, and with the extra lag of waiting for a VLM to respond via HTTP, this solution is infeasible.
