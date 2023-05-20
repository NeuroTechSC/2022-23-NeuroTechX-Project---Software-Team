# ML is going to give us:
#   - phoneme detected
#   - phoneme tokenized version (3 letter)
#   - EMG Voltage Data
#   - time

# Input Schema

MLInputSchema = {
    "phonemeDetected": int, # number
    "phonemeTokenizedVersion": str,
    "EMGVoltageData": dict({
        "time": int,
        "channel0": float,
        # ...
        "channelN": float,
    }),
    "time": int
}