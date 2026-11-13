import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import cv2
import PIL.Image
import numpy as np
import traitlets
from IPython.display import display
import ipywidgets.widgets as widgets
from jetbot import Camera, bgr8_to_jpeg
import time

class CollisionAvoidance:
    
    def __init__(self, model, robot):
        self._robot = robot
        self._model = model
        
        self._mean = None
        self._std = None
        self._normalize = None
        
        self.initModel()
        return


    def initModel(self):
        # transferring model to work via GPU, for obvious reasons
        self._device = torch.device('cuda')
        self._model = self._model.to(self._device)
        self._model = self._model.eval().half()
        
        # alter the formatting for the model to work with the front camera
        self._mean = torch.Tensor([0.485, 0.456, 0.406]).cuda().half()
        self._std = torch.Tensor([0.229, 0.224, 0.225]).cuda().half()
        self._normalize = torchvision.transforms.Normalize(self._mean, self._std)
        return


    def preprocess(self, imgToProcess):
        imgToProcess = PIL.Image.fromarray(imgToProcess)
        imgToProcess = transforms.functional.to_tensor(imgToProcess).to(self._device).half()
        imgToProcess.sub_(self._mean[:, None, None]).div_(self._std[:, None, None])
        return imgToProcess[None, ...]
    
    
    def update(self, change):
        # global blocked_slider, robot
        x = change['new'] 
        x = self.preprocess(x)
        y = self._model(x)

        # we apply the `softmax` function to normalize the output vector so it sums to 1 (which makes it a probability distribution)
        y = F.softmax(y, dim=1)

        prob_blocked = float(y.flatten()[0])

        # only used for visuals
        # blocked_slider.value = prob_blocked

        # dont need to worry about going forward, as this is handled by the road following
        # so we just stop if we are blocked
        # we stop by returning 0 for both motors (tuple)
        
        #if prob_blocked >= 0.5:
        #    self._robot.stop()


        if prob_blocked < 0.7:
            #robot.forward(speed_slider.value)
            return False
        else:
            # stop robot if blocked!
            #robot.stop()
            return True

        #time.sleep(0.001)