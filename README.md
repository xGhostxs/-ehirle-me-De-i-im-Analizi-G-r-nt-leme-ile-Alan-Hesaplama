# Şehirleşme Değişim Analizi

Bu proje, 2014 ve 2024 yıllarına ait uydu/görüntü verileri üzerinde betonlaşma (şehirleşme) alanlarının değişimini hesaplamak için OpenCV ve NumPy kullanır.

## İşlevler

- İki farklı tarihte çekilmiş görüntüyü okur  
- Gri tonlara dönüştürür  
- Belirli eşik değerine göre betonlaşan alanları maskeleyerek tespit eder  
- Alan büyüklüklerini piksel cinsinden hesaplar  
- Değişim oranını % olarak hesaplar ve konsola yazdırır  
- Sonuçları matplotlib ile görselleştirir

## Gereksinimler

- Python 3.x  
- OpenCV (`opencv-python`)  
- NumPy  
- Matplotlib

## Kurulum
pip install opencv-python numpy matplotlib

## Kullanım
image1.png ve image2.png isimli iki görüntüyü aynı klasöre koyun.

sehirlestirme_analizi.py dosyasını çalıştırın
