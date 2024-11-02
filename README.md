# <p align="center"> Güneş Paneli Arıza Tespiti</p>


Bu depo, güneş panellerinde arıza tespiti amacıyla kullanılan VGG16 tabanlı bir derin öğrenme modelini içermektedir. Projede ayrıca, kullanıcıların görsel yükleyerek arıza tespiti yapabilmesini sağlayan bir Flask web uygulaması da bulunmaktadır. Bu sayede, güneş enerjisi sistemlerinin bakım süreçleri kolaylaştırılarak daha etkin yönetilmesi sağlanmaktadır.


## Proje Genel Bakış

Güneş enerjisi, sürdürülebilir bir enerji kaynağıdır; ancak, güneş panellerinde meydana gelen çatlak, kirlenme gibi çeşitli arızalar verimliliği olumsuz etkileyebilir. Bu projede, VGG16 modelini kullanarak bu tür arızaları görüntü sınıflandırma yoluyla tespit ediyoruz. Ek olarak, oluşturulan Flask tabanlı web uygulaması ile kullanıcılar, herhangi bir panel görselini yükleyerek modelden tahmin alabiliyorlar.

## Model Mimarisi

Bu projede **`VGG16`** modeli kullanılmıştır. Görüntü sınıflandırma alanında yaygın olarak kullanılan bir CNN modeli olan VGG16, ImageNet üzerinde önceden eğitilmiştir. Transfer öğrenme yöntemiyle modelin son katmanları güneş paneli arıza tespiti için özelleştirilmiştir.

## Web Uygulaması

Flask tabanlı web uygulaması, kullanıcıların kendi görsellerini yükleyerek modelden anında tahmin almasını sağlar. Uygulama arayüzünde, kullanıcılar bir görüntü seçerek yükleme yapabilir ve modelin tahmin sonuçlarını görüntüleyebilirler.

### Web Uygulaması Kurulumu ve Çalıştırılması

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/efe-eroglu/solar-panel-fault-detection.git
   cd solar-panel-fault-detection

2. Ana dosyayı çalıştırın:
   ```bash
   python app.py
   ```
   Uygulama varsayılan olarak `http://localhost:5000` adresinde çalışacaktır.

3. Tarayıcıdan `http://localhost:5000` adresine giderek uygulamayı kullanabilirsiniz.

## Proje İçi Görüntüler

![demo](https://github.com/user-attachments/assets/0564364a-317d-4941-a1ed-13dceeb365e6)



## Yapılabilecekler

* Projede şuan için **`VGG16`** modeli kullanılmıştır ilerleyen süreçler için **`VGG19`** ve **`ResNet`** modellerinin de denenmesi.
* Uygulama şuam için sadece web tabanlı olarak çalışabilmektedir. Saha çalışanlarının işlerini kolaylaştırmak adına projenin mobil cihazlara gömülmesi.

## Katkıda Bulunma
* Projede bir hata bulursanız veya bir geliştirme için pull request açabilirsizin.





<br>
<br>
<br>


# <p align="center"> Solar Panel Fault Detection</p>

This repository contains a deep learning model based on VGG16, designed for fault detection in solar panels. The project also includes a Flask web application that allows users to upload images for fault detection, facilitating the maintenance processes of solar energy systems and enabling more efficient management.

## Project Overview

Solar energy is a sustainable energy source, but various faults like cracks or dirt on solar panels can negatively impact efficiency. In this project, we use the VGG16 model to detect such faults through image classification. Additionally, a Flask-based web application enables users to upload any panel image and receive predictions from the model.

## Model Architecture

The **`VGG16`** model is used in this project. VGG16 is a widely-used CNN model for image classification and has been pre-trained on ImageNet. Through transfer learning, the final layers of the model have been customized for solar panel fault detection.

## Web Application

The Flask-based web application allows users to instantly get predictions from the model by uploading their own images. In the application interface, users can select an image, upload it, and view the model's prediction results.

### Setting Up and Running the Web Application

1. Clone the repository:
   ```bash
   git clone https://github.com/efe-eroglu/solar-panel-fault-detection.git
   cd solar-panel-fault-detection
   ```

2. Run the main file:
   ```bash
   python app.py
   ```
   The application will run by default at **`http://localhost:5000`**
3. Access the application in your browser at **`http://localhost:5000`**



## Images From The Project

![demo](https://github.com/user-attachments/assets/0564364a-317d-4941-a1ed-13dceeb365e6)

## Future Improvements

* Currently, the **`VGG16`** model is used. Testing other models like **`VGG19`** and **`ResNet`** could be beneficial in future iterations.
* The application currently opeates as a web-based tool. Embedding the project mobile devices could make it more accessible for field workers.

## Contributing
* If you encounter any issues or have suggestions for improvements, feel free to open a pull request
