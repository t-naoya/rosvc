import librosa
from scipy.io import wavfile
from tqdm import tqdm

for i in tqdm(list(librosa.util.find_files('./'))):
    sr, x = wavfile.read(i)
    x = x[0:sr*6]
    wavfile.write(i, sr, x)