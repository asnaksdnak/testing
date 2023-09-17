import re

hkid_regex = r'[A-Z]+\d{6}\(\d{1}\)'
Phone_number_regex = r'(\+852|\b)\d{8}\b'
Website_link_regex = r'(https?):\/\/[\w\.-]+([/\w-_]+)?(\?[\w=&]+)?(#[\w]+)?'

sample_text = '''
I am Harvey. My HKID number is AB123456(7).
My phone number is 91234888.
Here is my portfolio website: https://harvey.me/portfolio/#section1.
Please feel free to contact me if needed.

Hi I am interested in the position.
Please visit http://jason-portfolio.com?cv=1 to see my previous works.
Below is my information.
Name: Jason
Tel: +85299243321
Id card number: D922118(1)
Reference number : 203476912746
'''

regex_results = re.finditer(hkid_regex,sample_text)

for regex_result in regex_results:
    print(regex_result.group(0))