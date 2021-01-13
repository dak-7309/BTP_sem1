# Smart Camera for Enforcing Social Distancing

<span style="color:#FFFFFF">Aayush Gupta | Daksh Thapar</span>

# COVID-19

<img src="img\BTP_Presentation0.png" width=500px />

<img src="img\BTP_Presentation1.png" width=414px />

Figure 1: COVID\-19 figures worldwide\, from Wikipedia

# Social Distancing

<img src="img\BTP_Presentation2.jpg" width=500px />

Figure 2: Effect of social distancing and other measures on curve of COVID\-19 cases by CDC

# State of the Art

### Camio - Social Distancing & Mask Detection

<img src="img\BTP_Presentation3.png" width=500px />

Figure 3: Social Distancing & Mask Detection using Camio

- AI

- ML

- Virtual 3D floor\-plan grid\- movement

- Personalized Alerts

### FebriEye, Vehant Technologies

<img src="img\BTP_Presentation4.jpg" width=424px />

<img src="img\BTP_Presentation5.png" width=500px />

Figure 4: Social Distancing by FebriEye

- AI based Thermal Temperature Monitoring System

- Non\-Contact Detection

- Thermal Camera

- Real time alerts

### Deep Learning based Safe Social Distancing and Face Mask Detection in Public Areas for COVID-19 Safety Guidelines Adherence (Shashi Yadav, July 2020)

<img src="img\BTP_Presentation6.png" width=385px />

Figure 5:Safe Social Distancing and Face Mask Detection in Public Areas

- Computer Vision based approach

- Real\-Time automated monitoring

- Implementing model on RaspberryPi4

- Three aspects: detection\, tracking\, and validation

### DeepSOCIAL: Social Distancing Monitoring and Infection Risk Assessment in COVID-19 Pandemic

<img src="img\BTP_Presentation7.png" width=469px />

<img src="img\BTP_Presentation8.png" width=469px />

Figure 6: Red spots due to multiple breaches

- Deep Neural Network\-Based model

- Automated people detection\, tracking

- Euclidean pairwise distances

- YOLOv4\-based framework

### Monitoring COVID-19 social distancing with person detection and tracking via fine-tuned YOLOv3 and Deepsort techniques (Narinder Singh Punn, Sanjay Kumar Sonbhadra and Sonali Agarwal)

<img src="img\BTP_Presentation9.png" width=500px />

Figure 7:Monitoring social distancing with person detection and tracking

- Deep learning based framework

- YOLO v3 object detection model

- Deepsort Algorithm with bounding boxes

- Further compared with faster region\-based CNN and SNN

# Methodology

### Flow Chart

<img src="img\BTP_Presentation10.png" width=500px />

Figure 8: Approach shown by diagram

### RaspberryPi4

<img src="img\BTP_Presentation11.jpg" width=500px />

Figure 9: RPi4 Architecture

### Libraries for Object detection

##### Custom built library inspired by Pixellib

<img src="img\BTP_Presentation12.jpg" width=500px />

Figure 10: Monitoring social distancing with Pixellib

- Open\-source Computer Vision Library \(obtained from GitHub\)

- Performs instance segmentation of objects

- Deep Learning Mask R\-CNN models to obtain and distinguish between 80 types of objects present in the pre\-trained Coco dataset\.

##### YOLO v3, v4

<img src="img\BTP_Presentation13.png" width=500px />

Figure 11: Average Precision comparisons for different architectures

##### YOLO v3,v4 Architecture

<img src="img\BTP_Presentation14.png" width=500px />

Figure 12: One stage detector architecture

### Euclidean Distance

<img src="img\BTP_Presentation15.png" width=500px />

### Mapping distance using bounding boxes

<img src="img\BTP_Presentation16.png" width=62px />

Figure 13: Bounding box

We know that the average human height is 5\.5 ft\(~165cm\) and we mapped this distance to the height of every bounding box\, which gives us a relation between the pixel distance throughout the frame and the real distance\.

Let height of bounding box be h’

True height h = 165cm

i\.e\. h=165cm \-> h’

=> h=1cm \-> h’/165

=> h=182\.8cm \-> \(h’/165\)\*182\.8

where 182\.8cm= 6ft\, our threshold for social distancing

### Database Management

Here is one instance of a file name containing frame of violation:

<img src="img\BTP_Presentation17.png" width=500px />

<img src="img\BTP_Presentation18.png" width=231px />

Figure 14: Suitable format for saving snapshot

# Experiments

### Custom built library inspired by Pixellib

<img src="img\BTP_Presentation19.png" width=500px />

Figure 15: Original Image

<img src="img\BTP_Presentation20.png" width=500px />

Figure 16: Final Image

### YOLO based detection(3 Scenarios)

##### Scenario 1 (outdoor, natural illumination)

<img src="img\BTP_Presentation21.png" width=500px />

Figure 17: Original Image

##### Bounding Boxes

<img src="img\BTP_Presentation22.png" width=500px />

Figure 18: Detected humans and applied bounding boxes

##### Pairwise Distance Calculation

<img src="img\BTP_Presentation23.png" width=277px />

Figure 19: Pairwise distances

Displayed at the top left of the frame during runtime\, contains pairwise euclidean distances for all pairs that are violating social distancing\, the persons are identified by unique “ids”

Displayed at the bottom left of the frame during runtime\, depicts the total number of social distancing violations

<img src="img\BTP_Presentation24.png" width=375px />

Figure 20: Number of violations

##### Comparing Distances with 6ft

<img src="img\BTP_Presentation25.png" width=500px />

Figure 21: Final Image

### Storing frames in Database, Buzzer

<img src="img\BTP_Presentation26.png" width=500px />

Figure 22: Snapshot saved in directory in desired format

### Recap of steps with Scenario 1 (YOLOv4)

<img src="img\BTP_Presentation27.png" width=500px />

<img src="img\BTP_Presentation28.png" width=500px />

<img src="img\BTP_Presentation29.png" width=500px />

Figure 23: Images for scenario 1 using YOLOv4

<img src="img\BTP_Presentation30.png" width=500px />

<img src="img\BTP_Presentation31.png" width=500px />

Figure 24: Images for scenario 1 using YOLOv3

# Scenario 2 (outdoor, natural illumination)

<img src="img\BTP_Presentation32.png" width=500px />

Figure 25: Original Image

<img src="img\BTP_Presentation33.png" width=500px />

Figure 26: Human detection and bounding boxes

<img src="img\BTP_Presentation34.png" width=500px />

Figure 27: Final Image

### Scenario 3 (indoor, artificial illumination)

<img src="img\BTP_Presentation35.jpg" width=500px />

Figure 28: Original Image

<img src="img\BTP_Presentation36.jpg" width=500px />

Figure 29: Human Detection and bounding boxes

<img src="img\BTP_Presentation37.jpg" width=500px />

Figure 30: Final Image 1

<img src="img\BTP_Presentation38.jpg" width=500px />

Figure 31: Final Image 2

# Results

### Custom built library inspired by Pixellib

<img src="img\BTP_Presentation39.png" width=500px />

Average time per frame = __15\.0029s__

Well structured bounding boxes

Clear inaccuracies in violation detection for social distancing

Figure 32: Final Image using Pixellib

### Scenario 1: YOLOv3

<img src="img\BTP_Presentation40.png" width=500px />

Figure 33: Final Image using YOLOv3

Average time per frame = __0\.2476s__

Number of social distancing violations reported =  __2__

Distance from person 3 to 5=2\.07ft

2\.07ft < 6ft=> <span style="color:#FF0000">Violation</span> of Social distancing

<img src="img\BTP_Presentation41.png" width=500px />

Figure 34: Final Image using YOLOv4

Average time per frame = __0\.15527s__

Number of social distancing violations reported = __4__

Distance from person 0 to 1 = 4\.71ft

Distance from person 2 to 6 = 1\.86ft

4\.71ft < 6ft=> <span style="color:#FF0000">Violation</span> of Social distancing

1\.86ft < 6ft=> <span style="color:#FF0000">Violation</span> of Social distancing

### Scenario 2: YOLOv4

<img src="img\BTP_Presentation42.png" width=500px />

Figure 35: Final Image using YOLOv4

Average time per frame = __0\.21384s__

Number of social distancing violations reported = __4__

Distance from person 2 to 11 = 2\.06ft

Distance from person 7 to 12 = 4\.20ft

2\.06ft < 6ft=> <span style="color:#FF0000">Violation</span> of Social distancing

4\.20ft < 6ft=> <span style="color:#FF0000">Violation</span> of Social distancing

<img src="img\BTP_Presentation43.jpg" width=500px />

True distance between humans= 6\.25ft

<img src="img\BTP_Presentation44.png" width=500px />

Figure 36: Original Image using YOLOv4

<img src="img\BTP_Presentation45.jpg" width=500px />

Number of violations=  __0__

True distance between humans= 6\.25ft

Estimated distance between humans= 6\.31ft

6\.31ft > 6ft=>  <span style="color:#00FF00">Not a violation</span>  of social distancing

<img src="img\BTP_Presentation46.png" width=500px />

Figure 37: Human detection and bounding boxes

<img src="img\BTP_Presentation47.jpg" width=500px />

Number of violations=  __2__

True distance between humans= 5\.5ft

Estimated distance between humans= 5\.55ft

5\.55ft < 6ft=>  <span style="color:#FF0000">Violation</span>  of social distancing

<img src="img\BTP_Presentation48.png" width=500px />

Figure 38: Final image at 5\.5ft

<img src="img\BTP_Presentation49.jpg" width=500px />

Number of violations=  __2__

True distance between humans= 3\.25ft

Estimated distance between humans= 3\.52ft

3\.52ft < 6ft=>  <span style="color:#FF0000">Violation</span>  of social distancing

<img src="img\BTP_Presentation50.png" width=500px />

Figure 39: Final image at 3\.25ft

# Challenges and Limitations

<img src="img\BTP_Presentation57.png" width=500px />

Figure 40: Future Hardware Prospective

<img src="img\BTP_Presentation58.png" width=500px />

Figure 41:Transformation of a 3D point on the image plane to the 2D coordinates