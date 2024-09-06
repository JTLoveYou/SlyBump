import tkinter as tk
from tkinter import font as tkfont
import tkinter.scrolledtext as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
import random

root = tk.Tk()
root.title("Club")
root.configure(bg='#1B1B1B')

title_font = tkfont.Font(family="Courier", size=24, weight="bold")
text_font = tkfont.Font(family="Courier", size=12)

sly_text = (
    
"    ██████  ██▓   ▓██   ██▓ ▄████▄   ██▓     █    ██  ▄▄▄▄   \n"
"  ▒██    ▒ ▓██▒    ▒██  ██▒▒██▀ ▀█  ▓██▒     ██  ▓██▒▓█████▄ \n"
"  ░ ▓██▄   ▒██░     ▒██ ██░▒▓█    ▄ ▒██░    ▓██  ▒██░▒██▒ ▄██\n"
"    ▒   ██▒▒██░     ░ ▐██▓░▒▓▓▄ ▄██▒▒██░    ▓▓█  ░██░▒██░█▀  \n"
"  ▒██████▒▒░██████▒ ░ ██▒▓░▒ ▓███▀ ░░██████▒▒▒█████▓ ░▓█  ▀█▓\n"
"  ▒ ▒▓▒ ▒ ░░ ▒░▓  ░  ██▒▒▒ ░ ░▒ ▒  ░░ ▒░▓  ░░▒▓▒ ▒ ▒ ░▒▓███▀▒\n"
"  ░ ░▒  ░ ░░ ░ ▒  ░▓██ ░▒░   ░  ▒   ░ ░ ▒  ░░░▒░ ░ ░ ▒░▒   ░ \n"
"  ░  ░  ░    ░ ░   ▒ ▒ ░░  ░          ░ ░    ░░░ ░ ░  ░    ░ \n"
"        ░      ░  ░░ ░     ░ ░          ░  ░   ░      ░      \n"
"                   ░ ░     ░                               ░ \n"

)
frame_sly_text = tk.Frame(root, bg='#FF2C2C')
frame_sly_text.pack(padx=5, pady=5)
sly_text_label = tk.Label(frame_sly_text, text=sly_text, font=text_font, fg="#FF2C2C", bg='#1B1B1B', padx=5, pady=5)
sly_text_label.pack()

log_text = st.ScrolledText(root, width=80, height=20, bg='#1B1B1B', fg='#FF2C2C', font=text_font)
log_text.pack(pady=10)

class RedirectText:
    def __init__(self, text_widget):
        self.output = text_widget

    def write(self, string):
        self.output.insert(tk.END, string)
        self.output.see(tk.END)

    def flush(self):
        pass

log_output = RedirectText(log_text)

def capture_screenshot(driver, name="screenshot"):
    screenshot_name = f"{name}_{int(time.time())}.png"
    driver.save_screenshot(screenshot_name)
    log_output.write(f"Capture d'écran enregistrée sous {screenshot_name}\n")

def create_driver():
    options = Options()
    profile_path = "C:\\Users\\votre_nom_utilisateur\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\votre_profil"
    options.profile = profile_path
    return webdriver.Firefox(options=options)

def login_discord(driver, discord_email, discord_password):
    try:
        driver.get('https://discord.com/login')
        email_input = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys(discord_email)
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(discord_password)
        password_input.send_keys(Keys.RETURN)
        wait_for_manual_captcha(driver)
        time.sleep(5)
    except Exception as e:
        capture_screenshot(driver, "login_error")
        log_output.write(f"Erreur lors de la tentative de connexion à Discord: {e}\n")

def wait_for_manual_captcha(driver):
    try:
        WebDriverWait(driver, 300).until(
            EC.url_contains("channels")
        )
    except Exception as e:
        log_output.write(f"Erreur ou délai dépassé lors de la résolution du captcha: {e}\n")
        capture_screenshot(driver, "captcha_error")

def navigate_to_channel(driver, server_id, channel_id):
    try:
        channel_url = f"https://discord.com/channels/{server_id}/{channel_id}"
        driver.get(channel_url)
        time.sleep(10)
        current_url = driver.current_url
        if current_url != channel_url:
            raise Exception("La navigation vers le canal Discord a échoué")
        page_ready = driver.execute_script("return document.readyState === 'complete';")
        if not page_ready:
            raise Exception("Page non prête")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
        )
    except Exception as e:
        capture_screenshot(driver, "navigation_error")
        log_output.write(f"Erreur lors de la navigation vers le serveur {server_id} -> salon {channel_id}: {e}\n")
        time.sleep(10)

def bump_in_channel(driver):
    retries = 3
    while retries > 0:
        try:
            message_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
            )
            message_box.click()
            time.sleep(random.uniform(1, 3))
            message_box.send_keys('/bump')
            time.sleep(2)
            suggestion_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'autocomplete')]"))
            )
            suggestion_box.click()
            time.sleep(1)
            message_box.send_keys(Keys.ENTER)
            time.sleep(5)
            break
        except Exception as e:
            retries -= 1
            log_output.write(f"Erreur lors de l'envoi de la commande /bump: {e}\n")
            capture_screenshot(driver, "bump_error")
            time.sleep(5 + random.randint(0, 10))

def run_script():
    accounts = [
        {
            'email': 'votre_email1',
            'password': 'votre_mot_de_passe1',
            'servers_and_channels': {
                "id_du_serveur1": "id_du_salon1",
                "id_du_serveur2": "id_du_salon2",
                "id_du_serveur3": "id_du_salon3",
                "id_du_serveur4": "id_du_salon4",
            }
        },
        {
            'email': 'votre_email2',
            'password': 'votre_mot_de_passe2',
            'servers_and_channels': {
                "id_du_serveur5": "id_du_salon5",
                "id_du_serveur6": "id_du_salon6",
                "id_du_serveur7": "id_du_salon7",
                "id_du_serveur8": "id_du_salon8",
            }
        },
        {
            'email': 'votre_email3',
            'password': 'votre_mot_de_passe3',
            'servers_and_channels': {
                "id_du_serveur9": "id_du_salon9",
                "id_du_serveur10": "id_du_salon10",
                "id_du_serveur11": "id_du_salon11",
                "id_du_serveur12": "id_du_salon12",
            }
        }
    ]

    while True:
        for account in accounts:
            try:
                driver = create_driver()
                login_discord(driver, account['email'], account['password'])

                for server_id, channel_id in account['servers_and_channels'].items():
                    try:
                        navigate_to_channel(driver, server_id, channel_id)
                        bump_in_channel(driver)
                    except Exception as e:
                        log_output.write(f"Erreur lors du bump dans le serveur {server_id} -> salon {channel_id}: {e}\n")

                    log_output.write(f"Bump effectué pour serveur {server_id} -> salon {channel_id}.\n")
                    time.sleep(5)

                driver.quit()
            except Exception as e:
                log_output.write(f"Erreur générale lors du traitement du compte {account['email']}: {e}\n")

        log_output.write("Cycle complet terminé. En attente avant le prochain cycle...\n")
        root.update()
        time.sleep(1800)

threading.Thread(target=run_script, daemon=True).start()
root.mainloop()
