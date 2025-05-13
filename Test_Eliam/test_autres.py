import os

os.system('ssh xxneonmain69xx@172.20.10.9 "python3 /home/xxneonmain69xx/PFR/enregistrer_dist.py"')
dist_path = "\\\\172.20.10.9\Partage\distance.txt"
with open(dist_path, "r") as f:
    content = f.read()
    print(content)