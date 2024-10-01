# Code pour afficher une vidéo, trouvé sur internet.

import nibabel as nib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

image = 'database/training/patient001/patient001_4d.nii.gz'
img = nib.load(image)
data = img.get_fdata()

print(f"Dimensions de l'image : {data.shape}")

z=data.shape[2]//2  # Prendre la tranche au milieu du volume

fig, ax = plt.subplots()
im = ax.imshow(data[:,:,z, 0], cmap='gray')
def update(frame):
    im.set_data(data[:,:,z,frame])
    ax.set_title(f"Frame {frame}")
    return [im]
ani = FuncAnimation(fig, update, frames=data.shape[3], interval=200, blit=True)
HTML(ani.to_jshtml())