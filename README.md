# FastConsumableQC.Vision

## Requirements
- Python 3.11
- skimage: `pip install scikit-image`
- OpenCV2: `pip install opencv-python`
- Other needed libraries will be installed automatically during the installatio of those two libraries.
- Furthermore, in my case, some are installed automatically by anaconda once I created a new environment.

## Run the code:
- Change directory: /FastConsumableQC.Vision/src/
- `python main.py`

## How to use:
- You could input whether a single image of a folder that contains many images
- by modifying the main.py
- Example for using with a folder whcih contains many images
    - `isFolder = True`
    - `dataset = 'dataset`
- Example for using with a single image
    - `isFolder = False`
    - `dataset = 'test_image\\5451.png'`
- The classification result will be printed in the terminal

## Result
- The dumped images will be store inside /FastConsumableQC.Vision/image_dump/
