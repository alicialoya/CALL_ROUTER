# Call Router
A simple speech recognition-based call routing system using HMMs and MFCC features.  
Routes calls to departments like Sales, Support, and Billing based on spoken keywords.


## Features
- Offline speech recognition
- Keyword-based routing
- Designed for small vocabulary commands


## HMM + MFCC (Traditional Pipeline)

  ## Process:
    1) Preprocessing: Clean audio
    2) Feature Extraction: Use MFCCs (Mel-Frequency Cepstral Coefficients)
    3) Modeling: Train an HMM per keyword
    4) Decoding: Use Viterbi algorithm to find the best keyword match

## To Do
- Add audio processing
- Build routing logic
- Integrate with telephony system


## Tools:
    1) Python + python_speech_features or librosa for MFCCs
    2) hmmlearn or custom HMM code

## Installation

### 1. Python Dependencies

Make sure Python 3.13 is installed. Then run:

```bash
pip install librosa
pip install python_speech_features
pip install hmmlearn
pip install soundfile
pip install scipy

```brew installation

brew install portaudio
python3.13 -m pip install pyaudio# CALL_ROUTER
