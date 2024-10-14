RTMP or Real Time Midi Program is designed to accompany free form musical performance outputting MIDI based on user input.

## Installation and Setup:

RTMP uses the Python library SCAMP and others to generate real time musical output. Type the following command in the command prompt:

`pip install scamp pynput python-rtmidi`

RTMP can utilize external instrumental plugins using LoopMIDI (Windows) or IAC Driver (Mac). Use the provided comments in `generator.py` replacing the `p` variable.

## Run the app:

Configure instrument sound, run `generator.py`, and input desired information including number of notes, trichord classification, duration, octave range, and tempo.

(Running the 'All' option for trichords and durations now has a chance for an event to occur per iteration including prioritizing groupings of trichords and implied meter)

When prompted to input trichord Forte numbers, refer to: https://en.wikipedia.org/wiki/List_of_set_classes

Use i for inversions instead of B (e.g. 3-2A and 3-2B become 3-2 and 3-2i).

Used in live performance: https://www.youtube.com/watch?v=6Nc0uJ4Kql4
YouTube demonstration after setup: https://youtu.be/bExJxpnGC-s
