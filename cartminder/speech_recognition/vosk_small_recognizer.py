import sherpa_onnx


class VoskSmallRecognizer:
    def __init__(self):
        self.model = sherpa_onnx.OfflineRecognizer.from_transducer(
            encoder="am/encoder.onnx",
            decoder="am/decoder.onnx",
            joiner="am/joiner.onnx",
            tokens="lang/tokens.txt",
            sample_rate=16000,
            decoding_method="greedy_search"
        )


    def recognize(self, sample, sample_rate) -> str:
        s = self.model.create_stream()
        s.accept_waveform(sample_rate, sample)
        self.model.decode_stream(s)

        return s.result.text
