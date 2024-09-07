import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
from tkinter import font as tkfont
import tkinter.scrolledtext as st
import threading
import random

# Charger les variables d'environnement
load_dotenv()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Club")
root.configure(bg='#1B1B1B')  

title_font = tkfont.Font(family="Courier", size=24, weight="bold")
text_font = tkfont.Font(family="Courier", size=12)

banner_text = (
    "██████  ██▓   ▓██   ██▓ ▄████▄   ██▓     █    ██  ▄▄▄▄   \n"
    "▒██    ▒ ▓██▒    ▒██  ██▒▒██▀ ▀█  ▓██▒     ██  ▓██▒▓█████▄ \n"
    "░ ▓██▄   ▒██░     ▒██ ██░▒▓█    ▄ ▒██░    ▓██  ▒██░▒██▒ ▄██\n"
    "  ▒   ██▒▒██░     ░ ▐██▓░▒▓▓▄ ▄██▒▒██░    ▓▓█  ░██░▒██░█▀  \n"
    "▒██████▒▒░██████▒ ░ ██▒▓░▒ ▓███▀ ░░██████▒▒▒█████▓ ░▓█  ▀█▓\n"
    "▒ ▒▓▒ ▒ ░░ ▒░▓  ░  ██▒▒▒ ░ ░▒ ▒  ░░ ▒░▓  ░░▒▓▒ ▒ ▒ ░▒▓███▀▒\n"
    "░ ░▒  ░ ░░ ░ ▒  ░▓██ ░▒░   ░  ▒   ░ ░ ▒  ░░░▒░ ░ ░ ▒░▒   ░ \n"
    "░  ░  ░    ░ ░   ▒ ▒ ░░  ░          ░ ░    ░░░ ░ ░  ░    ░ \n"
    "      ░      ░  ░░ ░     ░ ░          ░  ░   ░      ░      \n"
    "                   ░ ░     ░                               ░ \n"
)

frame_banner_text = tk.Frame(root, bg='#FF2C2C')
frame_banner_text.pack(padx=5, pady=5)
banner_label = tk.Label(frame_banner_text, text=banner_text, font=text_font, fg="#FF2C2C", bg='#1B1B1B', padx=5, pady=5)
banner_label.pack()

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

def click_continue_in_browser(driver):
    try:
        log_output.write("Vérification de la présence du bouton 'Continuer dans le navigateur'...\n")
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Continuer dans le navigateur']"))
        )
        continue_button.click()
        log_output.write("Bouton 'Continuer dans le navigateur' cliqué avec succès.\n")
    except Exception as e:
        capture_screenshot(driver, "continue_in_browser_error")
        log_output.write(f"Erreur lors du clic sur 'Continuer dans le navigateur': {e}\n")

def login_discord(driver, discord_email, discord_password):
    try:
        log_output.write("Tentative de connexion à Discord...\n")
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
        click_continue_in_browser(driver) 
        log_output.write("Connexion réussie.\n")
    except Exception as e:
        capture_screenshot(driver, "login_error")
        log_output.write(f"Erreur lors de la tentative de connexion à Discord: {e}\n")

def wait_for_manual_captcha(driver):
    log_output.write("Veuillez résoudre le captcha manuellement si nécessaire...\n")
    try:
        WebDriverWait(driver, 300).until(
            EC.url_contains("channels")  
        )
        log_output.write("Captcha résolu. Continuation du script...\n")
    except Exception as e:
        log_output.write(f"Erreur ou délai dépassé lors de la résolution du captcha: {e}\n")
        capture_screenshot(driver, "captcha_error")

def bump_in_channel(driver):
    try:
        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
        )
        log_output.write("Zone de texte trouvée.\n")
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
        log_output.write("Commande /bump envoyée avec succès.\n")
        time.sleep(5)  
    except Exception as e:
        log_output.write(f"Erreur lors de l'envoi de la commande /bump: {e}\n")
        capture_screenshot(driver, "bump_error")

def create_driver():
    options = Options()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)

def run_cycle(cycle_number):
    accounts = [
        {
            'email': os.getenv('DISCORD_EMAIL_1'),
            'password': os.getenv('DISCORD_PASSWORD_1'),
            'servers_and_channels': [
                ("960956019700269116", "960956020165869628"),
                ("960955799163772938", "960955799163772941"),
                ("960955003084898305", "960955003084898308"),
                ("957590327374516254", "1279379464060665888")
            ]
        },
        {
            'email': os.getenv('DISCORD_EMAIL_2'),
            'password': os.getenv('DISCORD_PASSWORD_2'),
            'servers_and_channels': [
                ("941372207341383752", "1279371407544946698"),
                ("941375988279947324", "941375988279947327"),
                ("1257719108880044102", "1257719109421105273"),
                ("960533893944057896", "1278995521016565832")
            ]
        }
    ]

    for account in accounts:
        try:
            driver = create_driver()
            login_discord(driver, account['email'], account['password'])

            try:
                server_id, channel_id = account['servers_and_channels'][cycle_number]
                channel_url = f"https://discord.com/channels/{server_id}/{channel_id}"
                log_output.write(f"Navigation vers le serveur {server_id} -> salon {channel_id}...\n")
                driver.get(channel_url)
                time.sleep(10)  
                bump_in_channel(driver)
            except Exception as e:
                log_output.write(f"Erreur lors du bump dans le serveur {server_id} -> salon {channel_id}: {e}\n")

            driver.quit()  
        except Exception as e:
            log_output.write(f"Erreur générale lors du traitement du compte {account['email']}: {e}\n")

def run_all_cycles():
    cycle_count = 4  
    while True:
        for cycle in range(cycle_count):
            log_output.write(f"Début du cycle {cycle + 1}\n")
            run_cycle(cycle)
            log_output.write(f"Cycle {cycle + 1} terminé.\n")
        log_output.write("Tous les cycles terminés. Attente de 30 minutes avant de recommencer...\n")
        root.update()
        time.sleep(1800)  

threading.Thread(target=run_all_cycles, daemon=True).start()

root.mainloop()



#    ██████╗ ██╗   ██╗    ██╗      ██████╗ ██╗   ██╗███████╗██╗   ██╗ ██████╗ ██╗   ██╗
#    ██╔══██╗╚██╗ ██╔╝    ██║     ██╔═══██╗██║   ██║██╔════╝╚██╗ ██╔╝██╔═══██╗██║   ██║
#    ██████╔╝ ╚████╔╝     ██║     ██║   ██║██║   ██║█████╗   ╚████╔╝ ██║   ██║██║   ██║
#    ██╔══██╗  ╚██╔╝      ██║     ██║   ██║╚██╗ ██╔╝██╔══╝    ╚██╔╝  ██║   ██║██║   ██║
#    ██████╔╝   ██║       ███████╗╚██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝╚██████╔╝
#    ╚═════╝    ╚═╝       ╚══════╝ ╚═════╝   ╚═══╝  ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ 
