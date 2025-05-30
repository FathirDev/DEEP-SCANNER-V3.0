
#DEEP SCANNER V3.0 - **THE DARK EDITION**

> **⚠️ PERINGATAN:**  
> Alat ini hanya untuk **KEPERLUAN EDUKASI**  
> **PENGGUNAAN UNTUK ILEGAL SANGAT DILARANG!**

![Banner](https://i.giphy.com/1gLZ32bMP5pY52PBsm.webp)

---

## Fitur
-  **Bruteforce Subdomain** (100k+ wordlist)  
-  **Deteksi Kebocoran Cloud** (AWS/GCP/Azure)  
-  **Simulasi Eksploitasi** (SQLi/XSS/RCE)  
-  **Deteksi Malware** (menggunakan aturan YARA)  
-  **Database CVE Offline** (2020-2025)  
-  **Mesin Fuzzing AI** untuk payload tingkat lanjut  

---

## Disclaimer
Alat ini hanya untuk **pengujian keamanan resmi dan keperluan edukasi**.  
**Pengembang (gua) tidak bertanggung jawab atas penyalahgunaan atau kerusakan yang disebabkan oleh penggunaan yang tidak tepat.**  

Tetap etis, tetap aman. Selamat mencoba!

---

# Panduan Setup

###Setup Windows
```bash
python -m ensurepip --upgrade
pip install -r requirements.txt

# Instal yara-python (manual atau AppVeyor)
pip install yara_python-[versi].whl
# Atau gunakan build dari AppVeyor
```

### Setup Linux
```bash
sudo apt update
sudo apt install python3 python3-pip libyara-dev
pip3 install -r requirements.txt
pip3 install yara-python
```

---

# Panduan Penggunaan

### Pindai Target Domain
```bash
python main.py scan example.com
```

### Simulasi Eksploitasi
```bash
python main.py exploit example.com
```

### Pemeriksaan Malware
```bash
python main.py hunt suspicious.php
```

---

## Pembuat & Kontak
- **ZexoGiza**  
- [contact@tirzznesia.me](mailto:contact@tirzznesia.me)  
- https://tirzznesia.me
