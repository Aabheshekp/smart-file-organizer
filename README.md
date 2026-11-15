# Smart File Organizer

A small Python CLI that groups files into folders based on common extensions. It is deliberately **preview-only by default**; moving files requires the explicit `--apply` flag. Existing filenames are preserved, and collisions get a numbered suffix.

## Requirements

Python 3.10+. No third-party dependencies.

## Preview

```sh
python organize.py "C:/Users/you/Downloads"
```

## Apply after reviewing the preview

```sh
python organize.py "C:/Users/you/Downloads" --apply
```

Choose another destination with `--output PATH`. The tool scans only top-level files, so its default output folder can be inside the source. Never choose the source folder itself as output. Review your backup practices before moving important files.

### Category

Additional project | Python, argparse, pathlib
