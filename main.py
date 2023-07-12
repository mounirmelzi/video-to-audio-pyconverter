import sys
from converter import Converter


def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 2:
        Converter.convert_folder(folder_path=argv[0], extension=argv[1])
    elif argc == 3:
        converter = Converter(video_path=argv[0])
        converter.convert(output_dir=argv[1], audio_extension=argv[2])
    else:
        print("[usage]")
        print("python main.py folder_path audio_extension")
        print("python main.py video_path output_folder audio_extension")
        print()
        print("supported video extensions: [.mp4, .ogv, .webm, .avi, .mov]")
        print("supported audio extensions: [.mp3, .wav, .ogg, .m4a] (recommended .mp3)")


if __name__ == "__main__":
    main()
