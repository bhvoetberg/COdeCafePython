from abc import ABC, abstractmethod
import pathlib


class VideoExporter(ABC):

    @abstractmethod
    def prepare_export(self, video_data):
        pass

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        pass


class VideoExporterH264BP(VideoExporter):
    def prepare_export(self, video_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class VideoExporterLossless(VideoExporter):
    def prepare_export(self, video_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class VideoExporterHi422P(VideoExporter):
    def prepare_export(self, video_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class AudioExporter(ABC):

    @abstractmethod
    def prepare_export(self, audio_data):
        pass

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        pass


class AudioExporterAAC(AudioExporter):
    def prepare_export(self, audio_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class AudioLossless(AudioExporter):
    def prepare_export(self, audio_data):
        pass

    def do_export(self, folder: pathlib.Path):
        pass


class ExporterFactory(ABC):
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        pass


class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return VideoExporterH264BP()

    def get_audio_exporter(self) -> AudioExporter:
        return AudioExporterAAC()


class HQExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return VideoExporterHi422P()

    def get_audio_exporter(self) -> AudioExporter:
        return AudioExporterAAC()


class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return VideoExporterHi422P()

    def get_audio_exporter(self) -> AudioExporter:
        return AudioLossless()


def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": HQExporter(),
        "master": MasterQualityExporter()
    }

    while True:
        export_quality = input("enter desired quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown option: {export_quality}")


def main(fac: ExporterFactory) -> None:
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    print(video_exporter)
    print(audio_exporter)


if __name__ == "__main__":
    fac = read_exporter()
    main(fac)
