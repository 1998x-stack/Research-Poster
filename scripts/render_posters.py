#!/usr/bin/env python3
"""Build reproducible PPTX, PDF and PNG from trusted poster sources on main."""
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
def run(*args):
    print("+", " ".join(args),flush=True)
    subprocess.run(args,cwd=ROOT,check=True)
def main():
    count=0
    for source in sorted((ROOT/"posters").glob("*/*/*/make_poster.py")):
        base=source.parent
        run(sys.executable,str(source))
        pptx=base/"poster.pptx";pdf=base/"poster.pdf";preview=base/"preview.png"
        if not pptx.is_file() or pptx.stat().st_size<1024:raise RuntimeError("PPTX missing/empty")
        # Rebuild derived assets from the latest PPTX, even when older files
        # were already committed to this repository. Never serve stale previews.
        pdf.unlink(missing_ok=True)
        preview.unlink(missing_ok=True)
        run("libreoffice","-env:UserInstallation=file:///tmp/lo_research_poster","--headless","--convert-to","pdf","--outdir",str(base),str(pptx))
        if not pdf.exists() or pdf.stat().st_size<1024:raise RuntimeError("PDF missing/empty")
        run("pdftoppm","-f","1","-l","1","-singlefile","-scale-to","2200","-png",str(pdf),str(base/"preview"))
        if not preview.exists() or preview.stat().st_size<1024:raise RuntimeError("PNG missing/empty")
        count+=1
    print("Rendered",count,"poster(s)")
if __name__=="__main__":main()
