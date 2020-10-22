import requests

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        #print('Success!', response)
        #print(f'Success! {response}')
        print(f'Success! Response {response.status_code}')
        print(f'Content {response.text}')
    else:
        print((f'Woops, there is requests failure {response.status_code}'))

except Exception as e:
    #print('There is an error', e)
    print(f'There is an error {e}')
print('Program ended')