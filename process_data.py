import essentia.standard as es

def extract_features(audio_path):
    # Load audio file
    loader = es.MonoLoader(filename=audio_path)
    audio = loader()

    # Initialize algorithms
    w = es.Windowing(type='hann')
    spectrum = es.Spectrum()
    mfcc = es.MFCC()

    # Compute features frame by frame
    mfccs = []
    for frame in es.FrameGenerator(audio, frameSize=1024, hopSize=512, startFromZero=True):
        mfcc_bands, mfcc_coeffs = mfcc(spectrum(w(frame)))
        mfccs.append(mfcc_coeffs)

    # Convert list of arrays into a 2D numpy array
    import numpy as np
    mfccs = np.array(mfccs)

    # You can add more feature extraction steps here

    return mfccs.mean(axis=0)  # Returning the mean MFCCs for simplicity

# Example usage
features = extract_features('path_to_your_audio_file.wav')
print(features)
