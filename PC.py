import customtkinter as ctk
from PIL import Image, ImageDraw, ImageTk
import psutil
import platform
import cpuinfo
import subprocess
import re
import tkinter.font as tkFont
from mistralai import Mistral

api_key = "PRNU3mr2ydQUFVZOPBW4lTiljn9cOVgx"
model = "mistral-large-latest"
client = Mistral(api_key=api_key)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class RoundedWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Закруглённые углы окна")
        self.geometry("400x300")
        self.overrideredirect(True)
        self.wm_attributes("-topmost", True)

        self.create_rounded_corners()

        self.label = ctk.CTkLabel(self, text="Менюшка:")
        self.label.place(relx=0.1, rely=0.2, anchor="nw")
        
        self.label = ctk.CTkLabel(self, text="Настройки:")
        self.label.place(relx=0.7, rely=0.2, anchor="nw")

        self.price_entry = ctk.CTkEntry(self, placeholder_text="Цена", width=150)
        self.price_entry.place(relx=0.6, rely=0.5, anchor="nw")
        self.price_entry.bind("<Return>", self.add_price_to_menu)

        self.new_button = ctk.CTkButton(self, text="Получить информацию", command=self.show_system_info)
        self.new_button.place(relx=0.1, rely=0.05, anchor="nw")

        self.update_button = ctk.CTkButton(self, text="Создать пк", command=self.clear_text)
        self.update_button.place(relx=0.58, rely=0.05, anchor="nw")

        self.condition_state = "Бу"
        self.device_type_state = "ПК"

        self.condition_button = ctk.CTkButton(self, text="Бу/Новый", command=self.toggle_condition)
        self.condition_button.place(relx=0.6, rely=0.3, anchor="nw")

        self.device_type_button = ctk.CTkButton(self, text="ПК/Ноут/Моноблок", command=self.toggle_device_type)
        self.device_type_button.place(relx=0.6, rely=0.4, anchor="nw")

        self.new_button = ctk.CTkButton(self, text="Проверка", command=self.open_new_window)
        self.new_button.place(relx=0.6, rely=0.7, anchor="nw")

        self.new_button = ctk.CTkButton(self, text="Ozon", command=self.add_text)
        self.new_button.place(relx=0.1, rely=0.8, anchor="nw")
        
        self.new_button = ctk.CTkButton(self, text="Avito", command=self.add_text)
        self.new_button.place(relx=0.2, rely=0.9, anchor="nw")
        
        self.new_button = ctk.CTkButton(self, text="WB", command=self.add_text)
        self.new_button.place(relx=0.5, rely=0.8, anchor="nw")
        
        self.new_button = ctk.CTkButton(self, text="DNS", command=self.add_text)
        self.new_button.place(relx=0.6, rely=0.9, anchor="nw")

        self.textbox = ctk.CTkTextbox(self, width=200, height=150)
        self.textbox.place(relx=0.1, rely=0.3, anchor="nw")

        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.on_move)

    def open_new_window(self):
        new_window = ctk.CTkToplevel(self)
        new_window.title("Проверка")
        new_window.geometry("300x200")

        button1 = ctk.CTkButton(new_window, text="Мышка", command=lambda: print("Окно где можно рисовать и снизуй пишет проведите с разной скоростью мышку и проверьте как она срывается"))
        button1.pack(pady=10)

        button2 = ctk.CTkButton(new_window, text="Звук", command=lambda: print("Просто пик какой небудь"))
        button2.pack(pady=10)

        button3 = ctk.CTkButton(new_window, text="Микрофон", command=lambda: print("Сделать типо экволайзера справа от менюшки при нажатии кнопки слушется микрофон 1 потмо сделать выбор миерофона и кнопка слышать себя"))
        button3.pack(pady=10)
        
        button3 = ctk.CTkButton(new_window, text="Моник", command=lambda: print("Открывается на весь экран разные цвета потом при нажати на экран мишью включается белый экран для проверки битых пикселей потом емли ещё раз нажать то нопадёт меню прога окно останется"))
        button3.pack(pady=10)

    def create_rounded_corners(self):
        width = 400
        height = 300

        image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        for i in range(height):
            r = int(255 - (255 * (i / height)))
            g = int(165 * (i / height))
            b = 0
            draw.line([(0, i), (width, i)], fill=(r, g, b))

        radius = 20
        draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=(0, 0, 0, 0))

        self.photo = ImageTk.PhotoImage(image)
        self.label_bg = ctk.CTkLabel(self, image=self.photo)
        self.label_bg.place(relx=0.5, rely=0.5, anchor="center")

    def toggle_condition(self):
        if self.condition_state == "Бу":
            self.condition_state = "Новый"
        else:
            self.condition_state = "Бу"
        self.textbox.insert("end", f"{self.condition_state}\n")

    def toggle_device_type(self):
        if self.device_type_state == "ПК":
            self.device_type_state = "Ноут"
        elif self.device_type_state == "Ноут":
            self.device_type_state = "Моноблок"
        else:
            self.device_type_state = "ПК"
        self.textbox.insert("end", f"{self.device_type_state}\n")

    def add_price_to_menu(self, event):
        price_text = self.price_entry.get()
        if price_text:
            self.textbox.insert("end", f"Цена: {price_text}\n")
            self.price_entry.delete(0, 'end')

    def add_text(self):
        price_text = self.price_entry.get()
    
        if price_text:
            self.textbox.insert("end", price_text)
            self.price_entry.delete(0, 'end')

    def clear_text(self):
        budget = self.price_entry.get()
        device_type = self.device_type_state
        condition = self.condition_state

        response = self.get_mistral_response(device_type, budget, condition)

        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", response)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

        if event.x <= 10 and event.y <= 10:
            self.destroy()
        elif event.x >= self.winfo_width() - 10 and event.y <= 10:
            self.destroy()
        elif event.x <= 10 and event.y >= self.winfo_height() - 10:
            self.iconify()
        elif event.x >= self.winfo_width() - 10 and event.y >= self.winfo_height() - 10:
            self.iconify()

    def on_move(self, event):
        x = self.winfo_x() - self.x + event.x
        y = self.winfo_y() - self.y + event.y
        self.geometry(f"+{x}+{y}")

    def get_system_info(self):
        info = {}

        gpu_info = self.get_gpu_info()
        info['Видеокарта'] = gpu_info if gpu_info else 'Не найдено'

        cpu = cpuinfo.get_cpu_info()
        info['Процессор'] = cpu['brand_raw']

        ram = psutil.virtual_memory()
        info['Оперативная память (ГБ)'] = ram.total / (1024 ** 3)

        ram_info = self.get_ram_info()
        info['Оперативная память (плашки)'] = len(ram_info)
        info['Информация о оперативной памяти'] = ", ".join(ram_info)

        info['Материнская плата'] = self.get_motherboard_info() or 'Не найдено'
        info['Блок питания'] = self.get_power_supply_info() or 'Неизвестно'

        disk_info = self.get_disk_info()
        info['Количество жёстких дисков'] = len(disk_info)
        info['Информация о жёстких дисках'] = "\n".join(disk_info)

        return info

    def get_gpu_info(self):
        try:
            if platform.system() == "Windows":
                command = "wmic path win32_VideoController get name"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().split('\n')[1:]
                gpus = [line.strip() for line in lines if line.strip()]
                return ', '.join(gpus) if gpus else 'Не найдено'

            elif platform.system() == "Linux":
                command = "lspci | grep -i vga"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().split('\n')
                return ', '.join(lines) if lines else 'Не найдено'

        except Exception as e:
            return f'Ошибка при получении информации: {str(e)}'

    def get_ram_info(self):
        ram_info = []
        try:
            if platform.system() == "Windows":
                command = "wmic memorychip get capacity, speed, manufacturer, partnumber"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().split('\n')[1:]
                for line in lines:
                    if line.strip():
                        parts = line.split()
                        capacity = int(parts[0]) / (1024 ** 3)
                        manufacturer = parts[2]
                        part_number = ' '.join(parts[3:])
                        ram_info.append(f"{manufacturer} {part_number}: {capacity:.2f} ГБ")

            elif platform.system() == "Linux":
                command = "sudo dmidecode --type memory"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if "Size:" in line:
                        size = line.split(":")[1].strip()
                        ram_info.append(size)

        except Exception as e:
            ram_info.append(f'Ошибка при получении информации: {str(e)}')

        return ram_info

    def get_motherboard_info(self):
        try:
            if platform.system() == "Windows":
                command = "wmic baseboard get product"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                return result.stdout.strip().split('\n')[1]

            elif platform.system() == "Linux":
                command = "sudo dmidecode -t baseboard"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    if "Product Name:" in line:
                        return line.split(":")[1].strip()

        except Exception:
            return None

    def get_disk_info(self):
        disk_info = []
        try:
            if platform.system() == "Windows":
                command = "wmic diskdrive get model, size"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().split('\n')[1:]
                for line in lines:
                    if line.strip():
                        parts = line.split()
                        model = parts[0]
                        size = int(parts[1]) / (1024 ** 3)
                        disk_info.append(f"{model}: {size:.2f} ГБ")

            elif platform.system() == "Linux":
                command = "lsblk -o NAME,SIZE,TYPE | grep disk"
                result = subprocess.run(command, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().split('\n')
                for line in lines:
                    parts = line.split()
                    model = parts[0]
                    size = parts[1]
                    disk_info.append(f"{model}: {size}")

        except Exception as e:
            disk_info.append(f'Ошибка при получении информации: {str(e)}')

        return disk_info

    def get_power_supply_info(self):
        return "Информация о блоке питания недоступна"

    def show_system_info(self):
        info = self.get_system_info()
        formatted_info = "\n".join([f"{key}: {value}" for key, value in info.items()])

        font = ctk.CTkFont(family="Helvetica", size=9)
        self.textbox.configure(font=font)
        
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", formatted_info)

    def get_mistral_response(self, device_type, budget, condition):
        prompt = (
            f"Собери {device_type}. "
            f"Пиши только итоговый список комплектующих без объяснений, "
            f"только полное название и цены комплектующего. "
            f"Итого: цена. "
            f"Бюджет: {budget} руб. "
            f"Запрос: {condition}\n\n"
            "Ответ:\n"
        )
        
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        return chat_response.choices[0].message.content

if __name__ == "__main__":
    app = RoundedWindow()
    app.mainloop()
