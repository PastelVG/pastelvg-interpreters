#!/usr/bin/env python3

import sys
import argparse
import json
from pastelvg import SVGDocument


def main():
    parser = argparse.ArgumentParser(description="PastelVG Interpreter for SVG files")
    parser.add_argument("file", help="Path to SVG file")
    parser.add_argument("--to-pastelvg", action="store_true", help="Output PastelVG JSON instead of SVG")
    parser.add_argument("--output", "-o", help="Path to save output (optional)")

    args = parser.parse_args()
    try:
        with open(args.file, "r", encoding="utf-8") as f:
            svg_string = f.read()

        doc = SVGDocument.from_svg(svg_string)

        if args.to_pastelvg:
            result = json.dumps(doc.to_pastelvg(), indent=2)
        else:
            result = doc.to_svg_string()

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"✅ Output written to {args.output}")
        else:
            print(result)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
