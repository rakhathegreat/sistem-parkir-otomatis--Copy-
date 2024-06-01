import cv2
import pyzbar.pyzbar as pyzbar
import time
import keluar

 
cap = cv2.VideoCapture(0)
last_detected_time = 0
time_interval = 10  # Time interval in seconds

while True:
    _, frame = cap.read()
    decode_QR = pyzbar.decode(frame)
    for qrcode in decode_QR:
        (x, y, w, h) = qrcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + w), (0, 0, 255), 2)
        current_time = time.time()
        if current_time - last_detected_time > time_interval:
            qr_data = qrcode.data.decode('utf-8')  # Decode QR code data
            masuk.masuk(qr_data[4:len(qr_data)])  # Print QR code data
            last_detected_time = current_time  # Update last detected time
        cv2.putText(frame, qr_data, (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    
    frame_flip = cv2.flip(frame, 1)
    cv2.imshow("QR Code Scanner", frame_flip)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()