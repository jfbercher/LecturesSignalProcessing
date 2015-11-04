def sysfileopen(filepath):
    import subprocess, os
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filepath))
    elif os.name == 'nt':
            os.startfile(filepath)
    elif os.name == 'posix':
#            subprocess.call(('xdg-open', filepath))
            subprocess.Popen(["xdg-open", filepath])

# Import useful read-write for wav files
from scipy.io.wavfile import read as wavread, write as wavwrite

def sound(var):
    from scipy.io.wavfile import write as wavwrite
    scaled = np.int16(var/np.max(np.abs(var)) * 32767)
    stmp=asarray(scaled,dtype=np.int16)
    wavwrite('stmp.wav',8820,stmp)
    sysfileopen("stmp.wav")
