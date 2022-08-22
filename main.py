import os
from PIL import Image

def webp_conv(in_file, out_file, quality=75, size=(500, 500)):
    im = Image.open(in_file)
    im.thumbnail(size)
    return im.save(out_file, "WEBP", quality=quality)


def main():
    webp_conv(
        input("Enter the image file path: "),
        input("Enter the output file name: "),
        quality = int(input("Enter the quality (0-100): ")),
        size=(int(input("Enter the width: ")), int(input("Enter the height: ")))
    )

    print("Done!!!")
    print(".\n.\n.\n")
    rerun = input("Do you want to run again? (y/n): ")
    if rerun == "y":
        main()
    else:
        print("\n")
        print("Goodbye!")
        print("\n")
        exit()


if __name__ == "__main__":
    main()
    exit()
