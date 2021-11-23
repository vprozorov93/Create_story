import os


def _sort_text_for_story(sketch_list):
    sketch_list = sorted(sketch_list, key=lambda k: k['line_num'])
    return sketch_list


def _get_text_from_sketch():
    sketch_list = []
    for file_name in [file for file in os.listdir(os.getcwd()) if '.txt' in file]:
        file_result = {}
        text = ''
        line_num = 0
        path = os.path.join(os.getcwd(), file_name)
        with open(path, 'rt', encoding='utf-8') as file:
            line_of_doc = file.readline()
            text += f'{line_of_doc}'
            while len(line_of_doc) > 0:
                line_of_doc = file.readline()
                text += f'{line_of_doc}'
                line_num += 1
        file_result['line_num'] = int(line_num)
        file_result['file_name'] = file_name
        file_result['text'] = text
        sketch_list.append(file_result)
        sketch_list = _sort_text_for_story(sketch_list)
    return sketch_list


def create_story_from_sketch():
    sketches = _get_text_from_sketch()

    path = os.path.join(os.getcwd(), 'new_story.txt')
    story_text = ''

    for sketch in sketches:
        story_text += f'{sketch["file_name"]}\n{sketch["line_num"]}\n{sketch["text"]}\n'

    with open(path, 'wt', encoding='utf-8') as file:
        file.write(story_text)

    print(f'История создана в {path}')


def main():
    create_story_from_sketch()


if __name__ == '__main__':
    main()
