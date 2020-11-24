import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


# write your code here

class Browser:

    def __init__(self):
        self.name_dir = str(args[1])
        self.txt_fw = None
        self.list_tabs = []

    # Main menu

    def menu(self):
        self.inp_url = input()
        self.file_name = self.inp_url.split(".")[0]
        self.choice = "http://www." + self.inp_url
        while True:
            if "." in self.inp_url:
                if self.inp_url == "bloomberg.com":
                    self.txt_fw = bloomberg_com
                    self.create_file()
                elif self.inp_url == "nytimes.com":
                    self.txt_fw = nytimes_com
                    self.create_file()
                else:
                    print("error")
            elif self.inp_url == "exit":
                exit()
            # elif "." not in self.inp_url:
            #     if self.inp_url == "exit":
            #         exit()
            #     elif self.file_name in self.list_tabs:
            #         self.file_open()
            #
            #     else:
            #         print("Error")
            #         break

    # Checking directory and create if not exist

    def check_dir(self):
        if not os.path.exists(f"{self.name_dir}"):
            os.mkdir(f"{self.name_dir}")

    # Creating page file

    def file_open(self):
        with open(f'{self.name_dir}/{self.file_name}', 'r') as r_file:
            print(r_file.read())
            self.menu()

    def create_file(self):
        with open(f'{self.name_dir}/{self.file_name}', 'w') as r_file:
            print(self.txt_fw)
            r_file.write(self.txt_fw)
            self.list_tabs.append(self.file_name)


args = sys.argv
my_browser = Browser()
my_browser.check_dir()
my_browser.menu()
