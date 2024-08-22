import socket

# عنوان IP والمنفذ
ip_address = '149.154.167.51'
port = 443  # المنفذ الذي تريد الاتصال به، استخدم المنفذ المناسب لخدمتك

def check_connection(ip, port):
    try:
        # إنشاء سوكت
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(300)  # تعيين مهلة الاتصال
            s.connect((ip, port))
            print(f"تم الاتصال بالخادم {ip} على المنفذ {port} بنجاح.")
    except socket.error as e:
        print(f"فشل الاتصال بالخادم {ip} على المنفذ {port}: {e}")

if __name__ == "__main__":
    check_connection(ip_address, port)
