🔒 Pixelock
Pixelock is a secure, private, and anonymous file-sharing and personal storage platform built with Django. It features end-to-end encryption for file transfers and a PIN-protected "Locker" system for personal storage, all wrapped in a modern Dark Mode UI.
--------------------------------------------------------------------------------------------------------
🚀 Features
1. Secure File Transfer (transferApp)

End-to-End Encryption: Files are encrypted using the Fernet (symmetric encryption) standard before being saved.

Drag & Drop Interface: Modern, intuitive UI for uploading files.

Multiple Sharing Options:

6-Digit Code: Simple retrieval for quick sharing.

QR Code: Generated instantly (powered by Segno) for mobile scanning.

Direct Link: Copy-paste shareable links.

Password Protection: Optional additional layer of security for transfers.
------------------------------------------------

2. Personal Locker (lockerApp)

No-Hassle Authentication: No complex registration or email verification links required.

Smart Access: Simply enter your Email and PIN.

If the account exists: The system logs you in.

If it's new: The system automatically creates a secure locker for you.

PIN Hashing: User PINs are hashed securely in the database.

Persistent Storage: Keep your important files safe and accessible across sessions.
------------------------------------------------

3. Session History (coreApp)

Activity Log: Tracks your last 50 sent and received transfers on the current device.

Privacy Focused: History is session-based and designed for user convenience without compromising privacy.
--------------------------------------------------------------------------------------------------------
🛠️ Tech Stack
Backend: Python, Django 5.x

Frontend: HTML5, CSS3, Bootstrap 5, FontAwesome

Security & Utils:

cryptography: For Fernet encryption/decryption.

segno & pypng: For lightweight, pure-Python QR code generation (no heavy image libraries required).
--------------------------------------------------------------------------------------------------------
📸 Screenshots
Send Content	Receive Content
(Place your send.png here)	(Place your receive.png here)
Drag & Drop Uploads	QR Code & Link Sharing
Locker Access	Personal Dashboard
(Place your locker_login.png here)	(Place your locker_dashboard.png here)
PIN-Based Login/Register	Secure File Management
⚙️ Installation & Setup
Follow these steps to run Pixelock locally.

1. Clone the Repository

Bash
git clone https://github.com/yourusername/pixelock.git
cd pixelock
------------------------------------------------
2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

Bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
------------------------------------------------
3. Install Dependencies

Bash
pip install django cryptography segno pypng
------------------------------------------------
4. Database Setup

Initialize the SQLite database and create the necessary tables.

Bash
python manage.py makemigrations
python manage.py migrate
------------------------------------------------
5. Create a Superuser (Optional)

To access the Django Admin panel:

Bash
python manage.py createsuperuser
------------------------------------------------
6. Run the Server
--------------------------------------------------------------------------------------------------------
🤝 Contributing
Contributions are welcome! If you have suggestions for improving encryption standards or UI enhancements:

Fork the repository.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.
