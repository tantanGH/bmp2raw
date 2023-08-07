import os
import sys
import argparse

from PIL import Image

def convert(screen_width, src_image_dir, output_file):

  frame0 = False
  frame1 = False

  with open(output_file, "wb") as f:

    for bmp_name in sorted(os.listdir(src_image_dir)):

      if bmp_name.endswith(".bmp"):

        print(bmp_name)
              
        im = Image.open(src_image_dir + "/" + bmp_name)

        im_width, im_height = im.size
        if im_width != screen_width:
          print("error: image width is not same as screen width.")
          break

        im_bytes = im.tobytes()

        if screen_width == 384 or screen_width == 512:

          grm_bytes = bytearray(512 * im_height * 2)
          for y in range(im_height):
            for x in range(im_width):
              r = im_bytes[ (y * im_width + x) * 3 + 0 ] >> 3
              g = im_bytes[ (y * im_width + x) * 3 + 1 ] >> 3
              b = im_bytes[ (y * im_width + x) * 3 + 2 ] >> 3
              c = (g << 11) | (r << 6) | (b << 1)
              if c > 0:
                c += 1
              grm_bytes[ y * 512 * 2 + x * 2 + 0 ] = c // 256
              grm_bytes[ y * 512 * 2 + x * 2 + 1 ] = c % 256
          f.write(grm_bytes)

        else:

          if frame0 is False:
            grm_bytes = bytearray(256 * im_height * 2 * 2)
            for y in range(im_height):
              for x in range(im_width):
                r = im_bytes[ (y * im_width + x) * 3 + 0 ] >> 3
                g = im_bytes[ (y * im_width + x) * 3 + 1 ] >> 3
                b = im_bytes[ (y * im_width + x) * 3 + 2 ] >> 3
                c = (g << 11) | (r << 6) | (b << 1)
                if c > 0:
                  c += 1
                grm_bytes[ y * 512 * 2 + x * 2 + 0 ] = c // 256
                grm_bytes[ y * 512 * 2 + x * 2 + 1 ] = c % 256
            frame0 = True
          elif frame1 is False:
            for y in range(im_height):
              for x in range(im_width):
                r = im_bytes[ (y * im_width + x) * 3 + 0 ] >> 3
                g = im_bytes[ (y * im_width + x) * 3 + 1 ] >> 3
                b = im_bytes[ (y * im_width + x) * 3 + 2 ] >> 3
                c = (g << 11) | (r << 6) | (b << 1)
                if c > 0:
                  c += 1
                grm_bytes[ y * 512 * 2 + 256 * 2 + x * 2 + 0 ] = c // 256
                grm_bytes[ y * 512 * 2 + 256 * 2 + x * 2 + 1 ] = c % 256
            f.write(grm_bytes)
            frame0 = False
            frame1 = False

# main
def main():

  parser = argparse.ArgumentParser()

  parser.add_argument("screen_width", help="output screen width (256,384,512)", type=int)
  parser.add_argument("src_image_dir", help="source individual image directory")
  parser.add_argument("output_file", help="output file name")

  args = parser.parse_args()

  convert(args.screen_width, args.src_image_dir, args.output_file)


if __name__ == "__main__":
    main()
