import time
import pyautogui


print("""
 _   _                        _     
| | | |   __ _   ____   ___  | |    
| |_| |  / _` | |_  /  / _ \ | |    
|  _  | | (_| |  / /  |  __/ | |___ 
|_| |_|  \__,_| /___|  \___| |_____|
""")


# -----------------------------------[CONFIG]-----------------------------------
with open('coordonnees.txt', 'r') as fichier_texte:
    contenu = fichier_texte.read()
exec(contenu)
# ------------------------------------------------------------------------------
temps_attente = 10                                                            
nombres_ecoutes = 10000
compteur = 0
nombres_musique = 5
# ------------------------------------------------------------------------------
print("------------------------------------------")
print("[SYSTEM] - Les Bot vont se lancer .....")
print("------------------------------------------")
temps_debut = time.time()
time.sleep(5)
# ---------------------
pyautogui.moveTo(coo_BOT1)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 1] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT2)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 2] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT3)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 3] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT4)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 4] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT5)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 5] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT6)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 6] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT7)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 7] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT8)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 8] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT9)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 9] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT10)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 10] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT11)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
time.sleep(0.5)
print("[SYSTEM]- [BOT 11] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT12)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
time.sleep(0.5)
print("[SYSTEM]- [BOT 12] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT13)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 13] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT14)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 14] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT15)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 15] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT16)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 16] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT17)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 17] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT18)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 18] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT19)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 19] - READY")
# ---------------------
pyautogui.moveTo(coo_BOT20)
pyautogui.click(button='left')
time.sleep(0.5)
pyautogui.moveTo(coo_PLAY)
pyautogui.click(button='left')
print("[SYSTEM]- [BOT 20] - READY")
# ---------------------

print("------------------------------------------")
# -----------------------------------[BOT 1]-----------------------------------

while True:

        for _ in range(nombres_musique):
                pyautogui.moveTo(coo_BOT1)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 1] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 2]-----------------------------------
                pyautogui.moveTo(coo_BOT2)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 2] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 3]-----------------------------------
                pyautogui.moveTo(coo_BOT3)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 3] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")  
                time.sleep(0.5)          
        # -----------------------------------[BOT 4]-----------------------------------
                pyautogui.moveTo(coo_BOT4 )
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 4] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 5]-----------------------------------
                pyautogui.moveTo(coo_BOT5)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 5] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 6]-----------------------------------
                pyautogui.moveTo(coo_BOT6)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 6] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 7]-----------------------------------
                pyautogui.moveTo(coo_BOT7)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 7] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 8]-----------------------------------
                pyautogui.moveTo(coo_BOT8)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 8] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 9]-----------------------------------
                pyautogui.moveTo(coo_BOT9)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 9] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 10]-----------------------------------
                pyautogui.moveTo(coo_BOT10)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 10] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
         # -----------------------------------[BOT 11]-----------------------------------
                pyautogui.moveTo(coo_BOT11)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 11] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 12]-----------------------------------
                pyautogui.moveTo(coo_BOT12)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 12] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 13]-----------------------------------
                pyautogui.moveTo(coo_BOT13)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 13] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")          
        # -----------------------------------[BOT 14]-----------------------------------
                pyautogui.moveTo(coo_BOT14 )
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 14] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 15]-----------------------------------
                pyautogui.moveTo(coo_BOT15)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 15] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 16]-----------------------------------
                pyautogui.moveTo(coo_BOT16)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 16] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 17]-----------------------------------
                pyautogui.moveTo(coo_BOT17)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 17] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 18]-----------------------------------
                pyautogui.moveTo(coo_BOT18)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 18] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 19]-----------------------------------
                pyautogui.moveTo(coo_BOT19)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 19] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 20]-----------------------------------
                pyautogui.moveTo(coo_BOT20)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART)
                pyautogui.click(button='left')
                pyautogui.click(button='left')
                compteur += 1
                temps_ecoule = time.time() - temps_debut
                temps_en_minutes = temps_ecoule / 60
                print(f"[SYSTEM]-[BOT 20] Ecoute N°{compteur} / Temps écoulé : {temps_en_minutes:.2f} minutes")
        # -----------------------------------[BOT 21]-----------------------------------
          
        
                        
        for _ in range(1):
                print("------------------------------------------")
                pyautogui.moveTo(coo_BOT1)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                time.sleep(0.5)
                print("[SYSTEM]- [BOT 1] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT2)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                time.sleep(0.5)
                print("[SYSTEM]- [BOT 2] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT3)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 3] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT4)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 4] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT5)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 5] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT6)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 6] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT7)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 7] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT8)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 8] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT9)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 9] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT10)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 10] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT11)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                time.sleep(0.5)
                print("[SYSTEM]- [BOT 11] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT12)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                time.sleep(0.5)
                print("[SYSTEM]- [BOT 12] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT13)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 13] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT14)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 14] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT15)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 15] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT16)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 16] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT17)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 17] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT18)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 18] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT19)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 19] - RESTART ALBUM")
                # ---------------------
                pyautogui.moveTo(coo_BOT20)
                pyautogui.click(button='left')
                time.sleep(0.5)
                pyautogui.moveTo(coo_RESTART_ALBUM)
                pyautogui.click(button='left')
                print("[SYSTEM]- [BOT 20] - RESTART ALBUM")
                # ---------------------
               
        if compteur > 3000:
                print("Le compteur a dépassé 10000, le script s'arrête.")
                break