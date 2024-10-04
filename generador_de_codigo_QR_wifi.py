import qrcode

def generar_qr_wifi(ssid, contraseña, tipo='WPA'):  
    """Genera un código QR para conectarse a una red Wi-Fi."""  
    
    wifi_data = f"WIFI:S:{ssid};T:{tipo};P:{contraseña};;"  

    qr = qrcode.QRCode(  
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )  
 
    qr.add_data(wifi_data)  
    qr.make(fit=True)  

    img = qr.make_image(fill_color="black", back_color="white")  
 
    img.save("codigo_qr_wifi.png")  
    print("Código QR de Wi-Fi generado y guardado como 'codigo_qr_wifi.png'")  

if __name__ == "__main__":  
    ssid = "Fibertel WiFi9997 2.4GHz"  
    contraseña = "thebeatles1990"  
    generar_qr_wifi(ssid, contraseña)