

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io

    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    contents = response.text_annotations
    # content[0]는 모든 string을 담고 있어서 배제한다
    contents = contents[1:]

    text_list = []
    for content in contents:
        text = content.description
        text = text.replace(',','')
        text_list.append(text)
    
    return text_list



def get_password(text_list):

    password = []
    for text in text_list:
        if ':' in text:
            text = text.split(':')[-1]
        if len(text) >= 8:
            removed_text = remove_special_characters(text)
            if removed_text.isalpha() == False and removed_text.isalnum() == True:
                password.append(text)

    return password


def remove_special_characters(text):
    special_characters = "~!@#$%&*+/*?"
    for special_character in special_characters:
        text = text.replace(special_character, "")

    return text

