import os
import sys


def get_slides(slides_dir):
  slides = {}
  for current_dir, dirs, files in sorted(os.walk(slides_dir)):
    if current_dir != slides_dir:
      slides[current_dir.removeprefix(f'{slides_dir}/')] = sorted(files)
  return slides


def get_clean_chapter_name(str):
  chapter_name_parts = str.split('-')
  return chapter_name_parts[1] + ''.join(part.capitalize() for part in chapter_name_parts[2:])


def create_js_content(slides_tree, slides_dir):
  file_content = f'// One method per module\n'
  for chapter in slides_tree:
    file_content += (
      f'function {get_clean_chapter_name(chapter)}() {{\n'
      f'  return [\n'
    )

    for filename in slides_tree[chapter]:
      file_content += f'    \'{chapter}/{filename}\',\n'

    file_content += (
      f'  ];\n'
      f'}}\n\n'
    )

  file_content += (
    f'function formation() {{\n'
    f'  return [\n'
  )

  for chapter in slides_tree:
    file_content += f'    ...{get_clean_chapter_name(chapter)}(),\n'

  file_content += (f'  ].map(slidePath => {{\n'
                   f'    return {{ path: slidePath }};\n'
                   f'  }});\n'
                   f'}}\n\n'
                   f'export function usedSlides() {{\n'
                   f'  return formation();\n'
                   f'}}\n'
                   )
  return file_content


def write_to_file(slides_file, content):
  file = open(slides_file, "w")
  file.write(content)
  file.close()


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print(f'error: this program need 2 arguments !')
    print(f'usage: python3 {sys.argv[0]} [markdown dir] [slide.js file]')
    exit(1)
  slides = get_slides(sys.argv[1])
  content = create_js_content(slides, sys.argv[1])
  write_to_file(sys.argv[2], content)
