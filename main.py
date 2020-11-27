import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore

# write your code here

class Browser:

    def __init__(self):
        self.name_dir = str(args[1])
        self.txt_fw = None
        self.stack_pages = []
        self.text = ""

    # Main menu

    def menu(self):
        while True:
            self.inp_url = input()
            self.list_tabs = os.listdir(self.name_dir)
            self.list_tabs1 = list(self.list_tabs)
            self.file_name = self.inp_url.split(".")[0]
            if "." in self.inp_url:
                if "https://" not in self.inp_url:
                    self.inp_url = "https://" + self.inp_url
                    self.txt_fw = self.read_site()
                    self.create_file()
                    self.stack_pages.append(self.file_name)
            elif self.inp_url == "exit":
                break
            elif self.inp_url in self.list_tabs:
                self.file_open()
                self.stack_pages.append(self.file_name)

            elif self.inp_url == "back":
                self.stack_pages.pop()
                self.file_name = self.stack_pages[-1]
                self.file_open()
            else:
                print("error")

    # Requests
    def read_site(self):
        r = requests.get(self.inp_url)
        if r:
            soup = BeautifulSoup(r.content, 'html.parser')
            el = soup.find_all('div')

            for i in el:
                if "p" in i.text or "ul" in i.text or "ol" in i.text or "li" in i.text:
                    self.text += str(i.text) + "\n"
                elif "a" in i.text:
                    self.text += Fore.BLUE + i.text + "\n"
                
            
            # r.encoding = 'utf-8'
            return self.text
        else:
            return "Error"

    # Checking directory and create if not exist
    def check_dir(self):
        if not os.path.exists(f"{self.name_dir}"):
            os.mkdir(f"{self.name_dir}")

    # Read page file
    def file_open(self):
        with open(f'{self.name_dir}/{self.file_name}', 'r') as r_file:
            print(r_file.read())

    # Create page file
    def create_file(self):
        with open(f'{self.name_dir}/{self.file_name}', 'w') as r_file:
            print(self.txt_fw)
            r_file.write(self.txt_fw)

if __name__ == "__main__":
    args = sys.argv
    my_browser = Browser()
    my_browser.check_dir()
    my_browser.menu()
