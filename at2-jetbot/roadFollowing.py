import torchvision
import torch
import torchvision.transforms as transforms
import torch.nn.functional as F
import cv2
import PIL.Image
import numpy as np
from IPython.display import display
import ipywidgets
import traitlets
from jetbot import Camera, bgr8_to_jpeg

class RoadFollowing:
    
    def __init__(self, model, robot):
        self._robot = robot
        self._model = model
        
        self._mean = None
        self._std = None
        
        # turning angle
        self._angle = 0.0
        self._angle_last = 0.0
        
        # initial values (magic numbers based off of testing)
        self._speedGain = 0.12
        self._steeringGain = 0.04
        self._steeringDGain = 0.02
        self._steeringBias = 0.0
        
        # robot speed and steering
        self._speed = 0.0
        self._steering = 0.0
        
        self.initModel()
        return
        
        
    def initModel(self):
        # sets the model and details
        #self._model = torchvision.models.resnet18(pretrained=False)
        #self._model = torch.nn.Linear(512, 2)
        
        # adjust this model to use the road following training data
        #self._model.load_state_dict(torch.load('best_steering_model_xy.pth'))
        
        # transferring model to work via GPU, for obvious reasons
        self._device = torch.device('cuda')
        self._model = self._model.to(self._device)
        self._model = self._model.eval().half()
        
        # alter the formatting for the model to work with the front camera
        self._mean = torch.Tensor([0.485, 0.456, 0.406]).cuda().half()
        self._std = torch.Tensor([0.229, 0.224, 0.225]).cuda().half()
        return

        
    def preprocess(self, imgToProcess):
        imgToProcess = PIL.Image.fromarray(imgToProcess)
        imgToProcess = transforms.functional.to_tensor(imgToProcess).to(self._device).half()
        imgToProcess.sub_(self._mean[:, None, None]).div_(self._std[:, None, None])
        return imgToProcess[None, ...]

    
    def execute(self, change):
        currentImage = change['new']
        xy = self._model(self.preprocess(currentImage)).detach().float().cpu().numpy().flatten()
        x = xy[0]
        y = (0.5 - xy[1]) / 2.0

        # x_slider.value = x
        # y_slider.value = y

        self._speed = self._speedGain

        self._angle = np.arctan2(x, y)
        pid = self._angle * self._steeringGain + (self._angle - self._angle_last) * self._steeringDGain
        self._angle_last = self._angle

        self._steering = pid + self._steeringBias
        
        #self._robot.left_motor.value = max(min(self._speed + self._steering, 1.0), 0.0)
        #self._robot.right_motor.value = max(min(self._speed - self._steering, 1.0), 0.0)

        # return a tuple of the left and right motor values
        return [max(min(self._speed + self._steering, 1.0), 0.0), max(min(self._speed - self._steering, 1.0), 0.0)]