"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGES
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)