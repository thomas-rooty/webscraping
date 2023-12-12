# Note pour monsieur le professeur
ATTENTION, j'ai utilisé Brave et non Chrome, il faudra donc modifier les premiers lignes dans les fichiers doctolib.py et les notebook Jupyter :

Il suffit juste de pointer vers Chrome, ou d'enlever la ligne option.binary_location
- doctolib.py : 
    ````py
    # Init webdriver
      driver_path = "./chromedriver.exe"
      brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
      option = webdriver.ChromeOptions()
      option.binary_location = brave_path  <-- Enlever cette ligne
      option.add_argument("--incognito")

![img.png](img.png)
