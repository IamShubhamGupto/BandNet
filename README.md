<!-- # WSSL-Weighted-Self-Supervised-Learning-for-Image-Inpainting -->
<br />
<p align="center">

  <h1 align="center">Analysis and application of multispectral data for water segmentation using machine learning</h1>
  
  <p align="center">
    Water Segementation from Sentinel-2. Work published in <a href="https://link.springer.com/book/9789811978685">CVMI 2022</a>
    <br />
  </p>
</p>

# Abstract
<p align="justify">
    Monitoring water is a complex task due to its dynamic nature, added pollutants, and land build-up. The availability of high-resolution data by Sentinel-2 multispectral products makes implementing remote sensing applications feasible. However, overutilizing or underutilizing multispectral bands of the product can lead to inferior performance. In this work, we compare the performances of ten out of the thirteenbands available in a Sentinel-2 product for water segmentation using eight machine learning algorithms. We find that the shortwave infrared bands (B11 and B12) are the most superior for segmenting water bodies.B11 achieves an overall accuracy of 71% while B12 achieves 69% across all algorithms on the test site. We also find that the Support Vector Machine (SVM) algorithm is the most favourable for single-band water segmentation. The SVM achieves an overall accuracy of 69% across the tested bands over the given test site. Finally, to demonstrate the effectiveness of choosing the right amount of data, we use only B11 reflectance data to train an artificial neural network, BandNet. Even with abasic architecture, BandNet is proportionate to known architectures for semantic and water segmentation, achieving a 92.47 mIOU on the test site. BandNet requires only a fraction of the time and resources to train and run inference, making it suitable to be deployed on web applications to run and monitor water bodies in localized regions. Our codebase is available at https://github.com/IamShubhamGupto/BandNet
    <br />
</p>

<br>
<p align="center">
    <img src="./assets/reflectance-workflow.drawio.png" alt="workflow"> 
</p>

# Environment 
All dependencies are prvided in the form of a conda environment yml file. The file is generated on a Windows 11 machine.
```
cd BandNet
conda env create -f environment.yml

```
## Additional software and resources
Users are required to download and install [SNAP](https://step.esa.int/main/download/snap-download/) to setup the python interface ```snappy```. <b>This cannot be installed by conda or pip directly.</b> This [link](https://senbox.atlassian.net/wiki/spaces/SNAP/pages/50855941/Configure+Python+to+use+the+SNAP-Python+snappy+interface) might be helpful in setting up snappy.
# Dataset
We use Sentinel-2 products available from [Copernicus](https://scihub.copernicus.eu/dhus/#/home). Data used to train bandnet is available under the `data` folder. For training DeepLabv3+, we release our generated dataset [here](https://drive.google.com/drive/folders/124Z0PhPc5ewjNr2rwXs04FRWaQ_668X5?usp=sharing)

# Pretrained weights
**NOTE**: The goal of BandNet is to quickly train and segment water bodies over localized regions and we do not expect it to generalize over other geographical terrains.

We release our pretrained models weights [here](https://drive.google.com/drive/folders/124Z0PhPc5ewjNr2rwXs04FRWaQ_668X5?usp=sharing). 


# Results
| <b> Annotation </b>    | <b> [DeepWaterMapv2](https://github.com/isikdogan/deepwatermap) </b>| <b> [WatNet](https://github.com/xinluo2018/WatNet) </b>|<b> BanNet </b>|
| ------------- | -------------| -------------| -------------|
| <img src="./assets/a1.png" alt="annotation 1"> | <img src="./assets/dwm1.png" alt="deepwatermap 1">| <img src="./assets/wn1.png" alt="watnet 1">| <img src="./assets/bn1.png" alt="bandnet 1" width="195">|
| <img src="./assets/a2.png" alt="annotation 2"> | <img src="./assets/dwm2.png" alt="deepwatermap 2">| <img src="./assets/wn2.png" alt="watnet 2">| <img src="./assets/bn2.png" alt="bandnet 2" width="195">|
# Reference
If you find our work useful, please cite using
### bibtex
```latex
@InProceedings{10.1007/978-981-19-7867-8_56,
author="Gupta, Shubham
and Uma, D.
and Hebbar, R.",
editor="Tistarelli, Massimo
and Dubey, Shiv Ram
and Singh, Satish Kumar
and Jiang, Xiaoyi",
title="Analysis and Application of Multispectral Data for Water Segmentation Using Machine Learning",
booktitle="Computer Vision and Machine Intelligence",
year="2023",
publisher="Springer Nature Singapore",
address="Singapore",
pages="709--718",
abstract="Monitoring water is a complex task due to its dynamic nature, added pollutants, and land build-up. The availability of high-resolution data by Sentinel-2 multispectral products makes implementing remote sensing applications feasible. However, overutilizing or underutilizing multispectral bands of the product can lead to inferior performance. In this work, we compare the performances of ten out of the thirteen bands available in a Sentinel-2 product for water segmentation using eight machine learning algorithms. We find that the shortwave-infrared bands (B11 and B12) are the most superior for segmenting water bodies. B11 achieves an overall accuracy of {\$}{\$}71{\backslash}{\%}{\$}{\$}71{\%}while B12 achieves {\$}{\$}69{\backslash}{\%}{\$}{\$}69{\%}across all algorithms on the test site. We also find that the Support Vector Machine (SVM) algorithm is the most favorable for single-band water segmentation. The SVM achieves an overall accuracy of {\$}{\$}69{\backslash}{\%}{\$}{\$}69{\%}across the tested bands over the given test site. Finally, to demonstrate the effectiveness of choosing the right amount of data, we use only B11 reflectance data to train an artificial neural network, BandNet. Even with a basic architecture, BandNet is proportionate to known architectures for semantic and water segmentation, achieving a 92.47 mIOU on the test site. BandNet requires only a fraction of the time and resources to train and run inference, making it suitable to be deployed on web applications to run and monitor water bodies in localized regions. Our codebase is available at https://github.com/IamShubhamGupto/BandNet.",
isbn="978-981-19-7867-8"
}
```

## License
This work is licensed under the [MIT License](./LICENSE)
