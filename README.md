# 🖥️ Email_Webcam_Detection_App

A lightweight Python application that detects when a person appears in front of your webcam and sends you an email notification — perfect for when you're away from your desk or out of the office.

---

## 🚀 Overview

**Email_Webcam_Detection_App** uses computer vision to monitor your webcam feed in real time. When a person is detected, the app automatically triggers an email alert so you know someone has arrived.

This is especially useful for:

* Home offices
* Small businesses
* Remote workers expecting visitors
* Monitoring entry points without full CCTV systems

---

## ⚙️ Features

* 🎥 Real-time webcam monitoring
* 🧍 Person detection using computer vision
* 📧 Instant email notifications
* ⏱️ Configurable detection intervals
* 🔕 Optional cooldown period to prevent email spam
* 💻 Lightweight and easy to run locally

---

## 🧠 How It Works

1. The app captures frames from your webcam.
2. A person detection model processes each frame.
3. When a person is identified:

   * An alert is triggered
   * An email is sent to the configured address
4. The system waits (optional cooldown) before sending another alert.

---

## 🛠️ Tech Stack

* Python 3.x
* OpenCV
* SMTP (for email notifications)
* (Optional) Pre-trained models (e.g., Haar Cascades / Deep Learning models)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/Email_Webcam_Detection_App.git
cd smart-presence-notifier
pip install -r requirements.txt
```

---

## ⚡ Usage

```bash
python main.py
```

Make sure your webcam is connected and accessible.

---

## ⚙️ Configuration

Update the following variables in your config file or environment:

```python
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

DETECTION_COOLDOWN = 60  # seconds
```

---

## 🔐 Security Notes

* Do **not** hardcode sensitive credentials in production
* Use environment variables or a `.env` file instead
* Consider app-specific passwords for email services

---

## 📸 Future Improvements

* 📷 Capture and attach an image when a person is detected
* ☁️ Cloud deployment support
* 📱 Push notifications (mobile integration)
* 🧠 Improved detection using deep learning (e.g., YOLO, MobileNet SSD)
* 🕒 Scheduling (active hours only)

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve functionality or add features.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

This application is intended for personal and ethical use only. Ensure you comply with local privacy laws and inform individuals if monitoring is in place.

---

## 💡 Inspiration

Built to solve a simple problem: *"Let me know when someone arrives while I’m away."*

---

## 👨‍💻 Author

Peter Thomson

---
