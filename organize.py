import argparse, shutil
from collections import Counter
from pathlib import Path

CATEGORIES={"Images":{".png",".jpg",".jpeg",".gif",".webp",".svg"},"Documents":{".pdf",".doc",".docx",".txt",".md",".rtf",".csv",".xlsx"},"Audio":{".mp3",".wav",".m4a",".flac",".ogg"},"Video":{".mp4",".mov",".mkv",".avi",".webm"},"Archives":{".zip",".tar",".gz",".7z",".rar"},"Code":{".py",".js",".ts",".java",".html",".css",".json",".sql"}}
def category(p):
 ext=p.suffix.lower()
 return next((name for name,exts in CATEGORIES.items() if ext in exts),"Other")
def destination(p,folder):
 target=folder/category(p)/p.name
 if not target.exists():return target
 stem,suffix=p.stem,p.suffix;i=1
 while True:
  candidate=target.with_name(f"{stem} ({i}){suffix}")
  if not candidate.exists():return candidate
  i+=1
def plan(source,folder):
 return [(p,destination(p,folder)) for p in source.iterdir() if p.is_file() and p.resolve()!=Path(__file__).resolve()]
def main():
 parser=argparse.ArgumentParser(description="Preview or organize files into extension-based folders.")
 parser.add_argument("source",type=Path,help="Folder containing files")
 parser.add_argument("--output",type=Path,help="Destination folder (default: source/Organized)")
 parser.add_argument("--apply",action="store_true",help="Actually move files; without this option the tool only previews")
 args=parser.parse_args();source=args.source.expanduser().resolve();folder=(args.output.expanduser().resolve() if args.output else source/"Organized")
 if not source.is_dir():parser.error(f"Source directory does not exist: {source}")
 if folder==source:parser.error("Output must not be the source folder")
 moves=plan(source,folder);counts=Counter()
 print("PREVIEW ONLY — add --apply to move these files.\n" if not args.apply else "APPLY MODE — files will be moved.\n")
 for src,dst in moves:
  print(f"{src.name}  →  {dst.parent.name}/{dst.name}");counts[dst.parent.name]+=1
 if not moves:print("No files to organize.")
 print("\n"+", ".join(f"{n}: {c}" for n,c in sorted(counts.items())))
 if args.apply:
  for src,dst in moves:dst.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(src),str(dst))
  print(f"\nMoved {len(moves)} file(s).")
if __name__=="__main__":main()
