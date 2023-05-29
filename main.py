import tkinter as tk
import requests

URL = 'https://randomuser.me/api/?nat=tr'


def create_fullname():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        user = data["results"][0]
        fullname = f"{user['name']['first']} {user['name']['last']}"
        result_label.config(text=fullname)

def create_email():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        user = data["results"][0]
        email = user['email']
        result_label.config(text=email)
def create_username():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        user = data['results'][0]
        username = user['login']['username']
        result_label.config(text=username)
def create_password():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        user = data["results"][0]
        password = user['login']['password']
        result_label.config(text=password)





window = tk.Tk()
window.title("Random User Generator")
window.geometry("500x500")

button_colors = ["#ff8c00", "#ff69b4", "#00bfff", "#7cfc00"]

welcome_label = tk.Label(window, text="Hoşgeldiniz! Ne oluşturmak istersiniz?", font=("Arial",14))
welcome_label.pack(pady=20)

fullname_button = tk.Button(window, text="İsim ve Soyisim Oluştur", command=create_fullname,bg=button_colors[0],fg="white",font=("Arial",12))
fullname_button.pack(pady=10)

email_button = tk.Button(window, text="E-Posta Adresi Oluştur", command=create_email,bg=button_colors[1],fg="white",font=("Arial",12))
email_button.pack(pady=10)

username_button = tk.Button(window, text="Kullanıcı Adı Oluştur", command=create_username,bg=button_colors[2],fg="white",font=("Arial",12))
username_button.pack(pady=10)

password_button = tk.Button(window, text="Şifre Oluştur", command=create_password,bg=button_colors[3],fg="white",font=("Arial",12))
password_button.pack(pady=10)

result_label = tk.Label(window, text="",font=("Arial",12))
result_label.pack(pady=20)


window.mainloop()