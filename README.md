# Malaysia Traffic Sign Recognition

Detect and recognize traffic sign on Malaysia's road using YoloV5 model trained on the Extended Malaysian Traffic Sign Dataset (EMTD) [1].

## Setup 

1. Clone this repo
    ```
    git clone https://github.com/haizadtarik/malaysia-traffic-sign-recognition.git
    ```
    
2. Download EMTD datasets from [here](https://zenodo.org/record/1217105#.Yc_sa9sRU5k) and place images in datasets/EMTD/images and `GT.csv` in `datasets/EMTD/images`. Run the following to create labels in yolo format.
    ```
    python export_yolo.py
    ```
3. Clone yolov5 repo
    ```
    git clone https://github.com/ultralytics/yolov5.git
    cd yolov5
    python -m pip install -r requirements.txt
    ```
4. Copy EMTD config files
    ```
    cp ../datasets/EMTD/EMTD.yaml ./data
    ```
    
5. Train 
    ```
    python train.py --data EMTD.yaml --img 640 --batch 32 --epochs 500 --weights yolov5s.pt
    ```
    
6. Inference
    ```
    python detect.py --source <INPUT> --weights runs/train/exp/weights/best.pt
    ```
    
**Notes**
Trained model is available in models
 

**Reference**

[1] Reilly, Sean, Clancy, Ian, Foy, Stephen, & Madden, Michael. (2018). Extended Malaysian Traffic Sign Dataset (EMTD) (Version 1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.1217105
