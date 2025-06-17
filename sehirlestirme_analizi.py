import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Görüntü dosyalarını oku
    img_2014 = cv2.imread('image1.png')
    img_2024 = cv2.imread('image2.png')

    # Gri tonlamaya çevir
    gray_2014 = cv2.cvtColor(img_2014, cv2.COLOR_BGR2GRAY)
    gray_2024 = cv2.cvtColor(img_2024, cv2.COLOR_BGR2GRAY)

    # Eşikleme ile beton alanı tespiti
    _, mask_2014 = cv2.threshold(gray_2014, 180, 255, cv2.THRESH_BINARY)
    _, mask_2024 = cv2.threshold(gray_2024, 180, 255, cv2.THRESH_BINARY)

    # Alan hesaplama (beyaz piksellerin sayısı)
    area_2014 = np.sum(mask_2014 == 255)
    area_2024 = np.sum(mask_2024 == 255)

    # Değişim oranı hesapla (%)
    change_rate = ((area_2024 - area_2014) / area_2014) * 100

    print(f"2014 şehirleşme alanı: {area_2014} piksel")
    print(f"2024 şehirleşme alanı: {area_2024} piksel")
    print(f"Değişim oranı: %{change_rate:.2f}")

    # Sonuçları görselleştir
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(mask_2014, cmap='gray')
    plt.title("2014 Şehirleşme Alanı")

    plt.subplot(1, 2, 2)
    plt.imshow(mask_2024, cmap='gray')
    plt.title("2024 Şehirleşme Alanı")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
