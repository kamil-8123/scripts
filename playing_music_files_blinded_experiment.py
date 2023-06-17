from argparse import ArgumentParser
from os import system
from random import sample

EXTENSIONS = ("flac", "mp3", "ogg")

parser = ArgumentParser(description="Blinded experiment of playing music files.")


parser.add_argument(
    "-f",
    "--files",
    action="store",
    help="files to be played",
    metavar="FILES",
    nargs="+",
    required=True,
)

parser.add_argument(
    "-p",
    "--player",
    action="store",
    default="mpv",
    help="player command",
    metavar="PLAYER",
    nargs=1,
)

parser.add_argument(
    "-r",
    "--repeat",
    action="store",
    default=1,
    help="how many times files should be played",
    metavar="REPETITION",
    nargs="?",
    type=int,
)

parser.add_argument(
    "-e",
    "--expose",
    action="store_true",
    default=False,
    help="expose file names during playing",
)

args = parser.parse_args()

files = [f for f in args.files if f.split(".")[-1].lower() in EXTENSIONS]

queue = [sample(files, k=len(files)) for _ in range(args.repeat)]

print("Press CTRL+C to break playing.")

feedback = {file: [] for file in files}

exit_flag = False
for i, row in enumerate(queue):
    if exit_flag:
        break
    print(f"--- Round {i+1} of {len(queue)} ---")
    for j, file in enumerate(row):
        print(f"Playing file {j+1} of {len(row)}... ", end="", flush=True)
        if args.expose:
            print(f"({file}) ", end="", flush=True)
        system(f"{''.join(args.player)} {file} > /dev/null 2>&1")
        try:
            comment = input("done. Please provide feedback: ")
            feedback[file].append(comment)
        except KeyboardInterrupt:
            print("\nTo exit press CTRL+D while providing feedback, not CTRL+C.")
        except EOFError:
            print("You've pressed CTRL+D. Bye.")
            exit_flag = True
            break

print("\n\n### YOUR FEEDBACK ###")
for file, comments in feedback.items():
    print(f"\nFor: {file} you've provided:")
    for comment in comments:
        print(f"- {comment}")
