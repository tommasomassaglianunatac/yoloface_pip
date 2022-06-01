import setuptools, os

PACKAGE_NAME = 'yolov5-face'
VERSION = '1.0.0'
AUTHOR = 'Rebrikov Artem'
EMAIL = 'https://github.com/elyha7'
DESCRIPTION = 'The project is a wrap over yolov5-face repo. Made simple portable interface for model import and inference.'
GITHUB_URL = 'https://github.com/tommasomassaglianunatac/yoloface_pip'

parent_dir = os.path.dirname(os.path.realpath(__file__))
import_name = os.path.basename(parent_dir)

with open('{}/README.md'.format(parent_dir), 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=GITHUB_URL,
    packages=[
        'face_detector',
        'face_detector.models',
        'face_detector.utils',
    ],
    package_dir={'yolov5-face':'.'},
    package_data={'weights': ['*.pt'],'models': ['*.yaml']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["thop",
                    "scipy",
                    "seaborn",
                    "joblib",
                    "matplotlib",
                    "torch",
                    "pandas",
                    "opencv_python",
                    "tqdm",
                    "numpy",
                    "torchvision",
                    "requests",
                    "Pillow",
                    "PyYAml",
                    "wandb"
                    ],
)