import sys
import argparse
from pathlib import Path
try:
    from .core import unlock_pdf
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_unlock.core import unlock_pdf
    from pdfjin_unlock import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="pdfjin-unlock",
        description="Decrypt and remove password security from a PDF document.",
        epilog="Online web version available at https://pdfjin.com/pages/unlock-pdf.html",
    )
    parser.add_argument("input", metavar="INPUT_PDF", help="Path to the protected PDF")
    parser.add_argument("-p", "--password", default="", help="Password of the protected PDF")
    parser.add_argument("-o", "--output", required=True, help="Destination path for unlocked PDF")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    try:
        out = unlock_pdf(args.input, password=args.password, output=args.output)
        print(f"🔓 PDF successfully unlocked -> {out}")
    except Exception as e:
        print(f"❌ Unlock failed (incorrect password or corrupted file): {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
