import os

def capture_image():
	save_dir = "\\172.20.10.2\Partage\images"
	os.makedirs(save_dir, exist_ok=True)
	width = 1920
	height = 1080

	filename = "Image1.png"
	filepath = os.path.join(save_dir, filename)

	#Capture avec libcamera-still
	os.system(f"ssh xxneonmain69xx@172.20.10.9 'libcamera-still -n --width {width} --height {height} -o {filepath}'")
	print(f"Image capturée : {filepath}")

capture_image()