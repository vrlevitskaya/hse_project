import requests


# url = "http://localhost:1337/v1/models"
# json_response = requests.get(url).json()
# print(json_response)
def generate_group1(task, number_empties):

    url = "http://localhost:1337/v1/chat/completions"

    response = []

    body = {
            "model": "llama2-70b",
            "temperature": 0.8,
            "stream": False,
            'messages': [{'role': 'system',
                          'content': f'You are a teacher of Python algorithms and structures'},
                         {'role': 'user',
                          'content': f'You need to develop assignments for computer science students. '
                                     'The essence of the task: it is necessary to test students knowledge of '
                                     'algorithms and data structures in Python.'
                                     'Students receive an algorithm code with gaps that they must fill in on their own.'
                                     f'Create {number_empties} passes in the provided code which '
                                     f'students must fill out on their own, the passes should check their '
                                     f'understanding of the algorithm.{task}'
                                     'Instead of passes write something like "oops the code is missing"'}]}
    json_response = requests.post(url, json=body).json().get('choices', [])

    for choice in json_response:
        response.append(choice.get('message', {}).get('content', ''))

    return response[0]


def generate_group2(tasks):
    url = "http://localhost:1337/v1/chat/completions"

    response = []

    body = {
        "model": "llama2-70b",
        "temperature": 0.7,
        "stream": False,
        'messages': [{'role': 'system',
                      'content': f"Based on the original serviceable code provided by the user, create a new faulty "
                                 "code in which random changes will be made and non-existent code fragments "
                                 "simulating noise will be added."
                                 "Noise may include:\n* unnecessary strings;\n* fragments that originally did not "
                                 "exist;\n*"
                                 "non-existent variables and functions.\n"
                                 "Noise must confuse students with code understanding"
                                 "The code should be similar to the working "
                                 "one, but contain noise"
                                 "which makes it difficult to complete or leads to an incorrect result.\n\
                        Reply only with the text of the resulting faulty code.\n\nexample:\n\n"
                                 "The user's account:\n\"Writing code:\n```\ndef my_function(x):\n y = x + 1\n "
                                 "return y\n``\n\"\np"
                                 "Otvet:\n```\ndef my_function(x):\n    y = x + 1\n    z = 5\n    if x > 0:\n "
                                 "print(Hello)\n    else:\n        y = x - 1\n    return y\n"},
                     {'role': 'user',
                      'content': f"The raw code {tasks}"}]}
    json_response = requests.post(url, json=body).json().get('choices', [])

    for choice in json_response:
        response.append(choice)

    return response[0]['message']['content']
