import sys
import platform
from time import sleep
import os
import subprocess
__version__ = "1.6.0"
def check_venv_module():
    try:
        subprocess.run(
            [sys.executable, "-m", "venv", "--help"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return True
    except Exception:
        return False

def check_in_venv():
    return (hasattr(sys, 'real_prefix') or 
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def download_lib():
    os.system("pip install -r requirements.txt")

def get_linux_distribution():
    try:
        distro = platform.linux_distribution()
        if distro[0]:
            return distro[0]
    except AttributeError:
        try:
            with open("/etc/os-release", "r") as file:
                info = {}
                for line in file:
                    key, value = line.strip().split("=", 1)
                    info[key] = value.strip('"')
                return info.get('NAME', 'Unknown')
        except FileNotFoundError:
            return "Unable to determine Linux distribution. /etc/os-release not found."
        
MESSAGES = [
            "Life in the city is full of activity. Early in the morning, people leave their houses in the manner ants do when their nest is broken. Then the streets are full of traffic. Shops and offices open, students are eager to go to their school and the day’s work begins. Many sightseers and tourists also visit many tourist attractions in the city, and businessmen from many parts of the world also come to conduct business transactions. In the evening, the offices and day schools begin to close, many of the shops are too close. There is often a traffic jam at this time because everyone wants to get home quickly. The city is described as a place of constant activity.",
            "Some people like to live downtown because of its facilities, but I prefer to live in the countryside for many reasons. First of all, life in the city is quite packed with hustle and bustle. It is really tiring and upsetting to wait for hours because of traffic jams. Second, pollution from dust and noise can cause human health to decline. Thirdly, I do not feel safe to live in the city because the criminal situations are rising. I love the silence, I love fresh air, so I love to live in the countryside.",
            "My name is Cindy, a computer science student. I’m currently studying undergraduate at the university, and I’m passionate about software development and artificial intelligence. I’m excited to connect with fellow students and professionals in the tech industry. In my free time, I also like reading books about technology. I am trying very hard to graduate well and find a good job in the industry.",
            "In many families, a generation gap is a common occurrence. This gap is the difference in views, attitudes and beliefs between generations in the family.An important reason for this gap is social development. Younger generations are exposed to technology and global lifestyles differently than their parents before them. These changes lead to different perspectives on life.The generation gap can lead to misunderstandings and conflicts within the family, as both parties perceive their own views as valid. To overcome the generation gap, open communication, empathy and respect are needed. Parents need to listen to their children’s opinions and children also need to acknowledge their parents’ life experiences.Understanding will help narrow the gap.",
            "I like listening to music in my free time. I listen to music whenever I can: on the bus, when doing housework, when I’m taking a shower,… My favorite music genres are Pop and Dance music. I listen to Pop music when I feel happy and Dance music when I want to dance my body. When I go out, I often shuffle my playlist and get excited about what song will be playing. I often download music collections of singers I like to my phone.  Music helps me relax and cheer me up after a tiring day. This has always been my favorite activity ever.",
            "The rapid development of society causes energy demand to increase. These fuels will likely run out at the rate humans are using them. Many methods have been proposed to save fuel. One is to reduce human needs in energy use by limiting non-essential needs. Utilities that consume a lot of energy should only be used when absolutely necessary. People should also replace outdated equipment with modern equipment to save fuel. Using public transportation is also a good idea. In industry, it is necessary to maintain machinery and use reasonable machinery systems. Energy saving requires support from everyone, every home.",
            "A year ago, my mother bought me a new phone for my birthday. It was a pink phone with an elegant design that made me extremely happy. This is the phone I always wanted. I mainly use my phone to contact friends, relatives and play games. This smartphone has a sharp screen and sensitive touch so I can operate the game very smoothly. I really love this phone not only because of its features but also because it is my mother’s love for me. I always try to use and preserve it carefully.",
            "Human actions are gradually leading to serious environmental damage. Water pollution, air pollution, and natural disasters occur frequently and are increasingly serious, causing a lot of damage in many countries. If we continue to be indifferent, this situation will become more serious and affect life on this planet. Environmental protection requires the cooperation of everyone. You can start with small things like throwing trash in the right place and planting trees. It is also important to increase awareness of those around you. Each of us must contribute to protecting the environment for future generations.",
            "Every individual has their own dreams and I also have plans for what I will do in the future.First, I want to continue studying. I believe that learning is essential for career growth and success. Second, I plan to start a coffee shop business. I am passionate about coffee research and also hope this passion will help me make money.Third, I find that maintaining a balance between work and life is essential. I prioritize my mental and physical health by exercising regularly and practicing mindfulness every day. In short, my plans for the future include continuously learning, building my career, and maintaining a work-life balance.",
            "There are many effective ways to improve English learning skills. Firstly, you should find yourself in an English speaking environment, it will help you increase your reflexes. Watching movies, listening to English music, participating in conversations with native speakers or English clubs,… are ways to help you have a good environment to practice. Second, reading English regularly will help increase vocabulary and improve grammar. Reading books, newspapers, comics,… will help learners come into contact with many different writing styles. Another equally effective method is to practice speaking and writing English every day. By combining many of the above methods, learners can improve their English skills.",
            "Each person’s daily routine is often different based on personality, age and lifestyle. I usually wake up at 6 am every day and the first thing I do is brush my teeth and wash my face. After that, I will make coffee and prepare breakfast for school. Meanwhile, my sister usually wakes up at 7 am and likes to drink milk instead of coffee like me.I usually study 8 hours at school and then spend 2 hours at the gym. This helps me stay in shape and stay healthier. My sister likes to jog after work and then go to the beauty spa.However, in the evening, we often spend time with our family. We had dinner together and talked about the past day. Sometimes the whole family will watch movies or listen to music together. Even though our habits are different, we all aim for a healthy and happy life",
            "Traffic in Vietnam is quite complicated and needs solutions. First of all, because there are so many vehicles on the road, hourly traffic jams often occur, especially in big cities. Second, people’s traffic awareness is still very poor. Many people often go fast, run red lights, carry bulky goods and ride motorbikes on the sidewalk. In short, traffic in Vietnam is always a difficult problem.",
            "My mother is always the person I love and admire the most. She spent a lot of time and loved raising me. Even though she has to work hard every day, she always takes time to teach us about the right things in life. Furthermore, she is also a shining example of kindness for me to follow. I admire and respect my mother not only because she raised me thoughtfully but also because she always helped me and everyone around me. She has always been a great influence on me and I hope I will give her a good life in the future.",
            "My favorite subject at school is English. The first reason I like this subject is because I really like English songs. I want to be able to confidently sing these songs. Second, I also want to be able to communicate with foreigners and find a good job in the future. Plus, learning English well can help me read books and watch movies in English. I also hope to be able to travel to many places around the world. In short, I feel English is a really interesting and useful subject.",
            "Tet is one of the most important festivals of Vietnam. This is the day a new year begins. Tet usually lasts about 7 days and has many interesting things. People often take time off and spend time visiting relatives and friends on these days. Others will travel or visit relatives’ graves. Before Tet comes, everyone decorates their houses beautifully. Special foods during Tet are usually banh chung and chicken. Tet is a time that everyone looks forward to.",
            "The Internet has many benefits and also some disadvantages. First, the internet provides a large amount of information to people, you just need to surf the web to get information. Second, you can relax by listening to music and playing games in your free time. Furthermore, the Internet helps us stay in touch with friends and family. Besides the advantages, the internet also has some disadvantages. Nowadays, there are some people addicted to surfing on the internet which affects their lives. Additionally, we can waste a lot of time sitting in front of the computer instead of studying or working. In short, the Internet will be very useful if we know how to use it effectively.",
            "One of the most outstanding features of this century is the advancement of science and its influence on all aspects of life. Scientists today are still conducting research into large areas of knowledge and mysterious problems. The advancement of science and technology has brought countries around the world closer together. We can go to distant lands in a short time, and can communicate with people far away quickly and clearly. The printing press is an invention that helps us read books about people in other countries. Science has helped humans progress faster on the evolutionary journey.",
            "Hi! My name is Ethan. I am 7 years old. My family has 4 members: my father, my mother, my younger sister and me. My father is an engineer. He is 40 years old. Currently, he works in the factory near my house so he doesn’t have to go so far to work. And my mother is 37 years old now. She is a literature teacher at Amsterdam high school, it’s also the old school where she studied a few years ago. Her students love her so much because she is a kind teacher. My younger sister is named Lisa. She is 2 years old, she is just a baby. Everyone in my family loves her very much because she is very lovely and obedient. She is very cute and I always take care of her whenever I finish my homework. I love my family very much.",
            "Hello, I’m Minh. I am studying at Hong Bang Secondary School. Located in a bustling city, it has been serving the community for many years. At Hong Bang Secondary School, we not only provide academic training but also promote the personal and social development of students. Furthermore, I also have the opportunity to participate in many interesting extracurricular activities, clubs and sports teams. Thanks to these group activities, I was able to meet many new friends. We always help each other when there are problems, we also often go out together to fun places. The teachers at my school are very enthusiastic, always ready to help students when they encounter difficulties in learning as well as in life. I think Hong Bang Secondary School is a good solution for us to study. I will definitely always remember the beautiful memories of school when I leave it.",
            "My name is Binh. I am a high school student. Today I will tell you about my hobby. I love sports the most because every time I play sports I feel really full of energy. After school I often play soccer with my friends. Besides, I also like to play basketball. I am a member of the basketball club at school. I have been in this club for over a year. In the basketball club that I join, all members are very healthy and they have admirable health. Thanks to them, I have great motivation to practice sports every day because I know that it will help me have good health and have the will to study. Moreover, you can also expand your relationships and meet valuable friends in life. I think you should try playing some sport. It’s really helpful for you.",
            "I have a very close friend; Her name is Huong. We have been playing together since we were innocent children. She is also my close neighbor. We are very close to each other, to the point that we can understand each other without the other person having to say anything. At school, she studied very well. In addition, she also actively participates in group activities. That’s why teachers and friends all love Huong. Huong has a kind heart; She always helps people around her if she can. She is a kind girl. Huong has many good qualities that I should learn from her. We often invite each other to study extra at the library on weekends. I have such good study results partly because Huong always urges me, so I feel very grateful to Huong. We will always be good friends.",
            "When I was young, my sister showed me the Harry Potter movie, and I loved it so much that I can’t remember how many times I watched it. Harry Potter is a very famous and beloved movie based on the fantasy novel by J.K. Rowling. The series tells about the adventures of a boy named Harry Potter and his friends Ron Weasley and Hermione Granger, who are studying at Hogwarts School of Witchcraft and Wizardry. They learn about the magical world, face various challenges, and eventually confront the dark wizard Lord Voldemort. The details of the movie are very dramatic and attractive. Every time I watch it, I’m so focused and can’t stop. My parents knew that I really liked the Harry Potter movie, so they bought me a model set of the characters in the movie so I could display them in my bedroom. This movie is very good, and I highly recommend everyone try watching it once.",
            "My name is Ngoc. Currently, I am a 7th grade student at Nguyen Thi Minh Khai Secondary School. At school, I learn many subjects, such as math, literature, English, biology, etc. I love all of those subjects. But the subject that I put a lot of effort into and have the best results in is English. Since I was only 3 years old, my parents have exposed me to English and taught me at a prestigious English center. Perhaps that was the best time to learn the language, so up to now, I am very fluent in English. English is very important to us in this day and age because it helps us communicate confidently and be able to travel abroad more easily. Therefore, let’s improve ourselves in English or another language.",
            "Hello, I’m Duc. I am 14 years old this year, and I am studying at Chu Van An Secondary School. I consider myself an active guy because I really like activities related to fitness and sports. The sport I love the most and the one I practice regularly is basketball. I started playing basketball when I was in 4th grade. I have been trained by my father since then. I feel like basketball is very good for us. Because it not only helps us have a healthy body but also contributes to promoting height growth. Even though I’m in 9th grade, my height is 1m80, which is much superior to my friends. It is the result of exercising and eating moderately. Please train yourself every day to have a healthy body like mine.",
            "During my holiday, I had the opportunity to explore new places, relax, and spend quality time with loved ones. I embarked on a journey to a tropical island, where I indulged in the warm sun, turquoise waters, and pristine beaches. The island was a paradise for adventure seekers, offering a range of activities such as snorkeling, scuba diving, and hiking through lush rainforests. I also took the time to immerse myself in the local culture, visiting traditional markets, sampling delicious cuisine, and learning about the rich history and customs of the island. It was a time of rejuvenation and self-discovery. Whether it was lounging by the pool with a good book, exploring hidden gems, or simply enjoying the breathtaking sunsets, my holiday provided a much-needed break from the daily routine and allowed me to create beautiful memories that I will cherish forever.",
            "Halloween is an annual festival celebrated on October 31st, typically observed in many countries around the world. It traces its roots back to ancient Celtic traditions, particularly the festival of Samhain, which marked the end of the harvest season and the beginning of winter. Halloween is associated with various customs and activities, the most notable being dressing up in costumes, carving jack-o’-lanterns, and going trick-or-treating. It is a time when people embrace the spooky and supernatural, with haunted houses and horror-themed parties becoming popular. The festival also involves the sharing of scary stories, watching horror movies, and indulging in themed treats like candy and caramel apples. Halloween captures the imagination and provides a sense of fun and excitement, allowing individuals of all ages to indulge in playful escapism. It has become a cherished tradition that brings communities together and celebrates the excitement of the supernatural and mysterious.",
            "In my dream house, I envision a tranquil retreat nestled amidst nature’s beauty. It would be a spacious and modern home, designed with large windows that offer panoramic views of lush greenery and natural landscapes. The house would feature an open floor plan, allowing for seamless flow and creating a sense of airy elegance. It would have a well-equipped gourmet kitchen where I could indulge in my passion for cooking and entertaining guests. The living spaces would be cozy, adorned with comfortable furniture and a fireplace, perfect for gathering with loved ones on chilly evenings. Additionally, my dream house would have a private library, filled with an extensive collection of books, providing the perfect sanctuary for reading and intellectual pursuits. Outside, there would be a meticulously landscaped garden, complete with a tranquil pond, a swimming pool, and a greenhouse for nurturing my love of gardening. This dream house would truly be a haven of serenity and a place where I can find solace and inspiration amidst the beauty of nature.",
            "I have participated in many music festivals, but I was most impressed with the performance of male singer Son Tung MTP. The music night took place last winter, when singer Son Tung had a performance at Bach Khoa Stadium near my home. That day, I went with my brother and I had unforgettable memories. At the performance that day, singer Son Tung sang three of my favorite songs including: Em Cua Giai Hom Qua, Lac Troi and Noi Nay Co Anh. These are all songs I like. The atmosphere that day was so exciting, everyone clapped, sang along to the music and danced with him. At the end of the music festival, he also gave gifts to the audience and made an appointment in Hanoi one day soon. The music ceremony with the presence of singer Son Tung was very impressive and I hope he will keep his promise to return to Hanoi soon.",
        ]

chu = r"""
                                                                 |                            _
                                                                 |                           ( )
                                                                 |                           |/                    
           / \  _   _| |_ ___  _ __ ___   __ _| |_(_) ___        |       _  __ _   _     _     _   _  _   _ 
          / _ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ __|       |      | |/ /| | | |   / \   | \ | || | | |
         / ___ \ |_| | || (_) | | | | | | (_| | |_| | (__        |      | ' / | |_| |  / _ \  |  \| || |_| |
        /_/___\_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___|       |      | . \ |  _  | / ___ \ | |\  ||  _  |
                                                                 |      |_|\_\|_| |_|/_/   \_\|_| \_||_| |_|
                                                                 |
                                                                 |                        _   
                                                                 |                       ( )
                                                                 |                        \|
         _____                 _____                             |       _____   ___      _     _   _            
        |  ___|   _ _ __   ___| |_(_) ___  _ __                  |      |_   _| / _ \    / \   | \ | |      
        | |_ | | | | '_ \ / __| __| |/ _ \| '_ \                 |        | |  | | | |  / _ \  |  \| |
        |  _|| |_| | | | | (__| |_| | (_) | | | |                |        | |  | |_| | / ___ \ | |\  |
        |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|                |        |_|   \___/ /_/   \_\|_| \_|
                                                                 |
        """

items = [
            "0. Info thằng Tồn Loàn",
            "=" * 105,
            "1. Auto click (trái / phải)",
            "2. Ghi nội dung bất kì",
            "3. Mở RickRoll =))",
            "4. Tự động tăng giảm âm lượng (nhập âm lượng muốn tăng hoặc giảm)",
            "5. Đo tốc độ mạng",
            "6. Spam Email",
            "7. Quét IP, Port trong mạng LAN (Cần Nmap)",
            "8. Domain -> IP Address",
            "9. Lấy các Password WiFi đã kết nối trước đó",
            "10. Spam SMS (số điện thoại)",
            "11. Ransomware (troll)",
            "12. Tạo chữ ASCII art",
            "13. Nghe file mp3",
            "14. File mp4 -> mp3",
            "15. Chương trình đang được update thêm, khi ra bản mới Tồn Loàn sẽ thông báo...",
            "=" * 105,
            "99. Exit"
                ]


print("CHECKING SYSTEM...")
sleep(1)
sy = platform.system()
if sy == "Windows":
    build = int(platform.version().split('.')[2])
    if build < 22000:
        print("Windows")
        print("OK")
        sleep(0.3)
        print("CHECKING VERSION...")
        sleep(3)
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        if not version == "3.12":
            print("\033[033mPhiên bản Python của bạn hiện tại không phải là python 3.12, vui lòng tải Python 3.12.x để sử dụng tool\033[0m")
            sys.exit(0)
        print("Python 3.12")
        print("OK...")
        sleep(0.3)
        print("CHECKING LIBRARY...")
        while True:
            try:
                from moviepy import VideoFileClip
                import pygame
                import warnings
                from datetime import datetime
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                import random
                import tkinter as tk
                import shutil
                import speedtest
                import re
                import signal
                import nmap
                from colorama import Fore, Style, init
                import pygetwindow as gw
                import pyautogui
                import msvcrt
                import keyboard
                import socket
                import threading
                import sys
                import math
                from ctypes import cast, POINTER
                from comtypes import CLSCTX_ALL
                from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                from threading import Lock
                import unicodedata
                from art import text2art
                print("OK")
                sleep(0.3)
                break
            except ModuleNotFoundError:
                sleep(2.4)
                print("DOWNLOAD FAIL, RETRYING...")
                sleep(2.4)
                download_lib()

print_lock = Lock()
pyautogui.FAILSAFE = True
init(autoreset = True)

        def find_app(app):
            windows = gw.getWindowsWithTitle(app)
            return windows

        def open_app(app):
            windows = find_app(app)
            if windows:
                windows[0].activate()
            else:
                print(f"Có vẻ bạn đã đóng {app} trước khi trả lời 'y'")

        def enter_after_write():
            pyautogui.press("Enter")

        def countdown(seconds):
            while seconds:
                mins, secs = divmod(seconds, 60)
                timer = f"{mins:02d}:{secs:02d}"
                print(f"Chương trình sẽ bắt đầu trong {timer}", end="\r")
                sleep(1)
                seconds -= 1

        def ve_chu():
            os.system("cls")
            print(Fore.CYAN + chu + Fore.RESET)

        def chuc_nang_0():
            try:
                print(f"\n!!!Kính gửi người chạy tool: Rất hân hạnh khi bạn sử dụng công cụ của tôi!\nĐây là trang info của tôi (bao gồm sdt , facebook, tiktok) : {Fore.YELLOW + "https://trankhanhtoan-py.github.io/info2" + Fore.RESET}\nNếu tool có vấn đề hoặc góp ý thì vui lòng LIÊN HỆ QUA ZALO HOẶC FACEBOOK HOẶC TIKTOK, mình KHÔNG NHẬN GỌI ĐIỆN!!!\n")
                sleep(2)
                print(Fore.RED + "Cảnh báo : Để dừng chương trình gấp, hãy đưa con trỏ chuột phía lên trên cùng góc trái.")
                sleep(5)
                while True:
                    try:
                        open_page = input("Bạn có muốn chương trình tự động mở trang info không? (y / n): ").strip().lower()
                        if open_page == "y":
                            countdown(3)
                            pyautogui.hotkey("win", "r")
                            sleep(0.3)
                            pyautogui.write("microsoft-edge:", interval = 0.001)
                            pyautogui.press("Enter")
                            print("Đã mở Edge")
                            sleep(0.7)
                            pyautogui.write("https://trankhanhtoan-py.github.io/info2", interval = 0.001)
                            pyautogui.press("Enter")
                            print("Đã mở Info Page")
                            clo = input("Bạn có muốn đóng nó không? (y / n) : ").strip().lower()
                            if clo == "y":
                                print(Fore.RED + "Cảnh báo : Hãy lưu hết dữ liệu của bạn trước khi đóng." + Fore.RESET)
                                clo2 = input("(Lần cuối) : Bạn có muốn đóng nó không? (y / n) : ").strip().lower()
                                if clo2 == "y":
                                    open_app("Edge")    
                                    print("Đã mở Edge")
                                    sleep(0.7)
                                    pyautogui.hotkey("alt", "f4")
                                    if not (find_app("Edge")):
                                        print("Đã đóng app")
                                    else:
                                        pyautogui.press("Enter")
                                        print("Đã đóng app")
                                    sleep(4.3)
                                    return
                                else:
                                    pass
                            elif clo == "n":
                                print("Cảm ơn bạn đã ủng hộ :>")
                                sleep(4)
                                return
                            else:
                                print(Fore.RED + "Vui lòng nhập đúng giá trị mà chương trình đưa ra" + Fore.RESET)
                                sleep(3)
                        elif open_page == "n":
                            print("Cảm ơn bạn đã ủng hộ :>")
                            sleep(4)
                            return
                        else:
                            print(Fore.RED + "Vui lòng nhập giá trị mà chương trình đưa ra" + Fore.RESET)
                            sleep(3)
                    except pyautogui.FailSafeException:
                        print(Fore.RED + "Đã dừng gấp chương trình" + Fore.RESET)
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET)
                sleep(4)
                return

        def chuc_nang_1():
            sleep(0.5)
            print(Fore.RED + "Cảnh báo: Để chương trình hoạt động, vui lòng không để chương trình autoclick vào terminal hoặc shell, hãy chuyển sang tab khác để có trải nghiệm tốt.\nNhập 0 vào bất kì input nào để di chuyển tới menu." + Fore.RESET)
            while True:
                sleep(2)
                rl = input("Bạn muốn click chuột trái hay chuột phải? (l / r / 0 để thoát) : ").strip().lower()
                if rl == "l":
                    try:
                        click = int(input("Nhập số lần click (0 để thoát): "))
                        if click == 0:
                            print(Fore.RED + "Đã dừng chương trình do giá trị nhập bằng 0" + Fore.RESET)
                            sleep(3)
                            return
                        countdown(3)
                        print("\n")
                        for i in range(click):
                            pyautogui.click()
                            print(f"Đã click {i + 1} lần")
                            sleep(0.001)
                        print(f"Đã click xong {click} lần")
                    except pyautogui.FailSafeException:
                        print(Fore.RED + "Đã dừng chương trình gấp" + Fore.RESET)
                        sleep(2)
                        return
                elif rl == "r":
                    try:
                        click = int(input("Nhập số lần click (0 để thoát): "))
                        if click == 0:
                            print(Fore.RED + "Đã dừng chương trình do giá trị nhập bằng 0" + Fore.RESET)
                            sleep(2)
                            return
                        countdown(3)
                        print("\n")
                        for i in range(click):
                            pyautogui.click(button='right')
                            print(f"Đã click {i + 1} lần")
                            sleep(0.3)
                        print(f"Đã click xong {click} lần")
                    except pyautogui.FailSafeException:
                        print(Fore.RED + "Đã dừng chương trình gấp" + Fore.RESET)
                        sleep(2)
                        return
                elif rl == "0":
                    print(Fore.RED + "Đã thoát chương trình do giá trị nhập bằng 0" + Fore.RESET)
                    sleep(3)
                    return
                else:
                    print(Fore.RED + "Vui lòng nhập đúng giá trị mà chương trình đưa ra" + Fore.RESET)
                    
        def chuc_nang_2():
            enter = False
            print(Fore.RED + "Cảnh báo: Vui lòng chuyển đến ứng dụng cần ghi. VD (Các ứng dụng nhắn tin : Chuyển tab đến ứng dụng và nhấn vào ô nhập văn bản)\n           Nhấn Ctrl + C để thoát chương trình khi nhập input. Di chuột về góc trái phía trên cùng màn hình để dừng chức năng." + Fore.RESET)
            while True:
                try:
                    sleep(2)
                    content = input("Nhập nội dung cần ghi vào: ").strip()
                    while True:
                        enter = input("Bạn có muốn tự động nhấn Enter? (y / n) : ").strip().lower()
                        if enter == "y":
                            enter = True
                            break
                        elif enter == "n":
                            break
                        else:
                            print(Fore.YELLOW + "Hãy nhập đúng giá trị chương trình yêu cầu" + Fore.RESET)
                            sleep(0.8)
                    print(Fore.YELLOW + "Dừng chương trình 3 giây chuyển tab" + Fore.RESET)
                    sleep(3)
                    countdown(3)
                    print("\n")
                except KeyboardInterrupt:
                    print(Fore.RED + "\nĐã dừng chức năng." + Fore.RESET)
                    sleep(0.8)
                    return
                try:
                    keyboard.write(content, delay = 0.1)
                    if enter:
                        enter_after_write()
                    print("Đã ghi xong.")
                except pyautogui.FailSafeException:
                    print(Fore.RED + "Đã dừng chương trình gấp" + Fore.RESET)
                    sleep(2)
                    return

        def chuc_nang_3():
            try:
                print(Fore.RED + "Cảnh báo : " + Fore.RESET, end = "")
                print("Không có cảnh báo gì hết. COI CHỪNG BỊ RICKROLL ĐẤY =)))")
                sleep(0.8)
                while True:
                    su = input("Bạn có chắc chắn với thao tác này không? (y / n) : ").strip().lower()
                    if su == "y":
                        countdown(3)
                        try:
                            pyautogui.hotkey("win", "r")
                            print("Đã mở hộp thoại Run")
                            sleep(1.3)
                            pyautogui.write("microsoft-edge:", interval = 0.1)
                            pyautogui.press("enter")
                            print("Đã mở Edge")
                            sleep(2)
                            pyautogui.write("https://www.yout-ube.com/watch?v=dQw4w9WgXcQ", interval = 0.1)
                            pyautogui.press("Enter")
                            sleep(5)
                            for i in range(6):
                                pyautogui.press("tab")
                                sleep(0.02)
                            pyautogui.press("enter")
                            sleep(0.001)
                            print("Đã mở video")
                            sleep(2)
                            print("Đã mở xong video RickRoll, chúc bạn được RickRoll vui vẻ.")
                            return
                        except pyautogui.FailSafeException:
                            print(Fore.RED + "Đã dừng chương trình gấp" + Fore.RESET)
                        sleep(4)
                        return
                        if clos == "n":
                            pass
                    if su == "n":
                        print(Fore.RED + "Đã dừng chương trình do người dùng nhập 'n'" + Fore.RESET)
                        return
                    else:
                        print(Fore.RED + "Hãy nhập đúng giá trị chương trình yêu cầu." + Fore.RESET)
                        sleep(4)
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET)
                sleep(3)
                return

        def chuc_nang_4():
            try:
                print(Fore.RED + "Cảnh Báo: Nhấn Ctrl + C để thoát chương trình\nNhập 0 vào các input để thoát chương trình."+ Fore.RESET)
                sleep(0.8)
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                while True:
                    current = volume.GetMasterVolumeLevelScalar()
                    print(Fore.YELLOW + f"Volume hiện tại: {round(current*100)}" + Fore.RESET)
                    try:
                        tg = input("Bạn muốn tăng hay giảm âm lượng? (+/-/Nhập 0 để thoát chương trình) : ").strip()
                        if tg == "+":
                            while True:
                                current = volume.GetMasterVolumeLevelScalar()
                                print(Fore.YELLOW + f"Volume hiện tại: {round(current*100)}" + Fore.RESET)
                                t = int(input("Bạn muốn tăng bao nhiêu? (1-100, 0 để thoát) : "))
                                if t < 0:
                                    print(Fore.YELLOW + "Không thể tăng âm lượng khi giá trị nhập bé hơn 0" + Fore.RESET)
                                    sleep(4)
                                elif t > 100:
                                    print(Fore.YELLOW + "Hãy nhập giá trị bé hơn hoặc bằng 100." + Fore.RESET)
                                    sleep(4)
                                elif t == 0:
                                    print(Fore.RED + "Đã thoát chương trình" + Fore.RESET)
                                    sleep(0.8)
                                    break
                                else:
                                    current = volume.GetMasterVolumeLevelScalar()
                                    print(Fore.YELLOW + f"Volume hiện tại: {round(current*100)}" + Fore.RESET)
                                    countdown(5)
                                    for i in range(t):
                                        current = min(current + 0.01, 1.0)
                                        volume.SetMasterVolumeLevelScalar(current, None)
                                        print(f"Âm lượng: {round(current*100)}%")
                                        sleep(0.1)
                                    print(Fore.GREEN + f"Đã tăng xong {t} âm lượng\nÂm lượng hiện tại của bạn : {round(current*100)}" + Fore.RESET)
                                    sleep(1)
                                    break
                        elif tg == "-":
                            while True:
                                g = int(input("Bạn muốn giảm bao nhiêu? (1-100, 0 để thoát) : "))
                                if g < 0:
                                    print(Fore.YELLOW + "Không thể giảm âm lượng khi giá trị nhập bé hơn 0" + Fore.RESET)
                                    sleep(0.8)
                                elif g > 100:
                                    print(Fore.YELLOW + "Hãy nhập giá trị bé hơn hoặc bằng 100" + Fore.RESET)
                                    sleep(0.8)
                                elif g == 0:
                                    print(Fore.RED + "Đã thoát chương trình do giá trị nhập bằng 0" + Fore.RESET)
                                    sleep(0.8)
                                    break
                                else:
                                    current = volume.GetMasterVolumeLevelScalar()
                                    print(Fore.YELLOW + f"Volume hiện tại : {round(current*100)}" + Fore.RESET)
                                    countdown(5)
                                    for i in range(g):
                                        current = max(current - 0.01, 0.0)
                                        volume.SetMasterVolumeLevelScalar(current, None)
                                        print(f"Âm lượng: {round(current*100)}%")
                                        sleep(0.1)
                                    print(Fore.GREEN + f"Đã giảm xong {g} âm lượng\nÂm lượng hiện tại của bạn : {round(current*100)}" + Fore.RESET)
                        elif tg == "0":
                            print(Fore.RED + "Đã dừng chương trình do người dùng nhập '0'." + Fore.RESET)
                            sleep(0.8)
                            return
                        else:
                            print(Fore.RED + "Hãy nhập đúng giá trị chương trình yêu cầu" + Fore.RESET)
                            sleep(0.8)
                    except ValueError:
                        print(Fore.YELLOW + "Số lượng tăng / giảm phải là số nguyên" + Fore.RESET)
                        sleep(0.8)
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã thoát chương trình." + Fore.RESET)
                sleep(0.8)
                return

        def show_ssid():
            result = subprocess.check_output(
            'netsh wlan show interfaces | findstr "SSID" | findstr /V "BSSID"',
            shell=True, text=True)
            ssid = result.split(":")[1].strip()
            return ssid

        def signal_handler(sig, frame):
            print(Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET)
            sleep(3)
            return

        def check_internet_speed():
            while True:
                try:
                    MAX_SPEED = float(input("\nNhập tốc độ gói cước internet của bạn (1Mbps - 1000Mbps, nhập đơn vị Mbps, mặc định : 100.0) : ") or 100)
                    if MAX_SPEED < 1 or MAX_SPEED > 1000:
                        print(Fore.YELLOW + "Hãy nhập trong phạm vi 1Mbps - 1000Mbps" + Fore.RESET)
                        sleep(3)
                    else:
                        break
                except ValueError:
                    print(Fore.YELLOW + "Giá trị nhập phải là số" + Fore.RESET)
            print("\n")
            try:
                st = speedtest.Speedtest()
                st.get_best_server()
                download_speed = st.download() / 1_000_000
                upload_speed = st.upload() / 1_000_000
                ping = st.results.ping
                percent_quality = min(100, (download_speed / MAX_SPEED) * 100)

                print(Fore.MAGENTA + "Vui lòng đợi một chút" + Fore.RESET, flush=True, end="")
                for _ in range(14):
                    print(".", end="", flush=True)
                    sleep(0.5)
                print("\n")
                print(Fore.YELLOW + "=" * 40)
                print(" KẾT QUẢ KIỂM TRA TỐC ĐỘ INTERNET ")
                print("=" * 40)
                print(f"Tốc độ tải xuống: {download_speed:.2f} Mbps")
                print(f"Tốc độ tải lên  : {upload_speed:.2f} Mbps")
                print(f"Độ trễ (ping)   : {ping:.2f} ms")
                print(f"Tín hiệu mạng   : {percent_quality:.1f} %")
                print("=" * 40 + Fore.RESET)
                return download_speed, upload_speed, ping, percent_quality
            except Exception as e:
                print(Fore.RED + f"{e} Không thể kiểm tra tốc độ internet. Vui lòng kiểm tra lại kết nối.\nKết quả khi log vào file sẽ là 0-0-0-0" + Fore.RESET)
                sleep(6)
                return 0, 0, 0, 0

        def cn():
            try:
                ssid = show_ssid()
                print(f"\nWifi hiện đang kết nối: {ssid}")
                sleep(2)
                countdown(3)
                download_speed, upload_speed, ping, percent_quality = check_internet_speed()
                log = input("Bạn có muốn log thông tin vào file NetCheck.txt không? (y/n): ").strip().lower()
                if log == "y":
                    while True:
                        dele = input("Bạn có muốn 'clear' file NetCheck.txt không? (y / n): ").strip().lower()
                        if dele == "y":
                            os.system("del NetCheck.txt")
                            print(Fore.GREEN + "Đã clear xong file" + Fore.RESET)
                            break
                        elif dele == "n":
                            break
                        else:
                            print(Fore.YELLOW + "Hãy nhập đúng giá trị chương trình yêu cầu" + Fore.RESET)
                    now = datetime.now()
                    timestamp = now.strftime("%H:%M:%S %d/%m/%Y")
                    try:
                        with open("NetCheck.txt", "a", encoding="utf-8") as f:
                            f.write(f"{timestamp}\n")
                            f.write("="*40 + "\n")
                            f.write("KẾT QUẢ KIỂM TRA TỐC ĐỘ INTERNET\n")
                            f.write("="*40 + "\n")
                            f.write(f"Tốc độ tải xuống: {download_speed:.2f} Mbps\n")
                            f.write(f"Tốc độ tải lên  : {upload_speed:.2f} Mbps\n")
                            f.write(f"Độ trễ (ping)   : {ping:.2f} ms\n")
                            f.write(f"Tín hiệu mạng   : {percent_quality:.1f} %\n")
                            f.write(f"Wifi đang kết nối: {ssid}\n")
                            f.write("="*40 + "\n\n")
                        print(Fore.GREEN + "Đã lưu kết quả vào NetCheck.txt (cùng thư mục cùng file chương trình)" + Fore.RESET)
                        sleep(1)
                    except Exception:
                        print(Fore.RED + "Lỗi khi ghi file." + Fore.RESET)
                elif log != "n":
                    print(Fore.RED + "Giá trị nhập không hợp lệ." + Fore.RESET)
            except subprocess.CalledProcessError:
                print(Fore.YELLOW + "\nKhông có kết nối mạng" + Fore.RESET)
                sleep(0.8)
                print(Fore.GREEN + "Đã thoát chương trình do không có kết nối mạng, hãy thử lại chức năng sau khi có wifi." + Fore.RESET)
                sleep(0.8)
                print(Fore.RED + "Đang thoát chương trình..." + Fore.RESET)
                sleep(2.5)
                menu_and_input()

        def chuc_nang_5():
            print(Fore.RED + "Cảnh báo : Vui lòng đợi chương trình khoảng 30-60 giây vì chương trình đưa vào độ trễ và độ tải để đo\n           Nếu kết quả đo đều hiển thị số 0 chứng tỏ không có kết nối mạng hoặc lỗi\n           Nhấn Ctrl + C để dừng chương trình." + Fore.RESET, end = "")
            print(Fore.YELLOW + "\nLưu ý : Tool này đang được bảo trì. Lý do : Đo tốc độ chưa chuẩn xác , chúng tôi sẽ sửa chữa cập nhật chúng, vui lòng thông cảm" + Fore.RESET)
            sleep(3)
            try:
                ssid = show_ssid()
                print(f"\nBạn đang kết nối vào mạng {ssid}, nếu muốn đo mạng khác thì vui lòng đổi mạng để chương trình cập nhật")
                print("Nhấn Enter để cập nhật và tiếp tục hoặc nhấn 0 để thoát chương trình", end = "")
                for i in range(3):
                    print(".", flush = True, end = "")
                    sleep(0.3)
                while True:
                    key_k = msvcrt.getch()
                    if key_k == b'0':
                        print(Fore.RED + "\nĐã thoát chương trình." + Fore.RESET)
                        sleep(2)
                        return
                    if key_k == b'\r':
                        print("\nĐang cập nhật", end = "")
                        for i in range(3):
                            print(".", flush = True, end= "")
                            sleep(0.7)
                        cn()
                        return
            except subprocess.CalledProcessError:
                print("Bạn chưa có kết nối wifi, vui lòng chọn một mạng để kết nối, sau đó nhấn Enter để tiếp tục hoặc nhấn 0 để thoát", end = "")
                for i in range(3):
                    print(".", end = "", flush = True)
                    sleep(0.2)
                while True:
                    key = msvcrt.getch()
                    if key == b'\r':
                        print("\nĐang cập nhật", end = "")
                        for i in range(3):
                            print(".", end = "", flush = True)
                            sleep(1)
                        cn()
                    elif key == b"0":
                        print(Fore.RED + "\nĐã thoát chương trình bởi người dùng" + Fore.RESET)
                        sleep(3)
                        return

        def load_accounts_from_file(filename="email.txt"):
            accounts = []
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if "|" in line:
                            email, password = line.split("|", 1)
                            accounts.append({"email": email.strip(), "password": password.strip()})
            return accounts


        def send_email(account, target_email, subject, body):
            try:
                msg = MIMEMultipart()
                msg["From"] = account["email"]
                msg["To"] = target_email
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(account["email"], account["password"])
                    server.sendmail(account["email"], target_email, msg.as_string())
                print(Fore.BLUE + f"[+] Đã gửi email tới {target_email} bằng {account['email']}" + Fore.RESET)
            except smtplib.SMTPAuthenticationError:
                print(Fore.RED + f"[-] Lỗi đăng nhập với {account['email']}, loại bỏ account này." + Fore.RESET)
            except Exception as e:
                print(Fore.RED + f"[-] Lỗi khi gửi từ {account['email']}: {e}" + Fore.RESET)


        def chuc_nang_6(TARGET, targ):
            ACCOUNTS = load_accounts_from_file()
            if not ACCOUNTS:
                print("Bạn chưa có file account email, vui lòng tạo file email.txt.")
                sleep(2)
                return
            try:
                for i in range(targ):
                    account = random.choice(ACCOUNTS)
                    message = random.choice(MESSAGES)
                    r_c = random.randint(1000, 99999)

                    send_email(
                        account,
                        TARGET,
                        f"Hello {TARGET}! - {r_c}",
                        f"{message}\n\nLần gửi {i+1}"
                    )
                    sleep(0.3)
                print(f"Thành công gửi {targ} email.")
            except KeyboardInterrupt:
                print(Fore.RED + "Đã dừng chương trình bởi người dùng" + Fore.RESET)
                sleep(2)
                return

        def scan_network(subnet="192.168.1.0/24"):
            print(Fore.YELLOW + "Đang quét IP, vui lòng chờ..." + Fore.RESET)
            nm = nmap.PortScanner()
            nm.scan(hosts=subnet, arguments='-sn')

            online_hosts = []
            print(Fore.GREEN + "Các host đang ONLINE:" + Fore.RESET)
            for idx, host in enumerate(nm.all_hosts(), 1):
                state = nm[host].state()
                if state == "up":
                    print({idx}, {host}, ":", Fore.GREEN + "OPEN" + Fore.GREEN)
                    online_hosts.append(host)
            return online_hosts

        def scan_ports(ip, start, end):
            nm = nmap.PortScanner()
            port_range = f"{start}-{end}"
            try:
                nm.scan(ip, port_range)
                if ip in nm.all_hosts():
                    for proto in nm[ip].all_protocols():
                        ports = nm[ip][proto].keys()
                        for port in sorted(ports):
                            state = nm[ip][proto][port]["state"]
                            print(f"{ip} | Port {port}/{proto}: {state}")
            except Exception as e:
                print(Fore.RED + f"Lỗi khi quét {port_range}: {e}" + Fore.RESET)

        def chuc_nang_7():
            print("CHECKING NMAP...")
            sleep(1.3)
            if shutil.which("nmap"):
                print("Máy có Nmap, đang tải chương trình...")
                sleep(2)
            else:
                print("Máy không có Nmap, vui lòng cài Nmap và chạy lại chương trình.")
                sleep(0.4)
                print(Fore.RED + "Đã dừng chương trình do không có Nmap" + Fore.RESET)
                sleep(1.7)
                return
            print(Fore.RED + "Cảnh báo : Tool này là tool bất hợp pháp, có thể gây ra các hậu quả không lường trước nếu không có sự đồng ý của chủ sở hữu mạng,\n           vui lòng sử dụng tool này khi được sự cho phép của bố mẹ hoặc chủ mạng." + Fore.RESET)
            sleep(1.5)
            while True:
                ok = input("Bạn có muốn thực hiện thao tác này không? (y / n) : ").strip().lower()
                if ok == "y":
                    try:
                        hosts = scan_network("192.168.1.0/24")
                        hosts = [ip for ip in hosts if ip != "192.168.1.1"]
                        if not hosts:
                            print(Fore.RED + "Không tìm thấy IP nào ONLINE." + Fore.RESET)
                        else:
                            while True:
                                choice = input(
                                    Fore.BLUE + "\nNhập số thứ tự IP bạn muốn quét port (0 để thoát): " + Fore.RESET
                                ).strip()
                                if choice == "0":
                                    print(Fore.RED + "Đã dừng chương trình bởi người dùng" + Fore.RESET)
                                    sleep(2)
                                    return
                                try:
                                    num = int(choice)
                                except ValueError:
                                    print(Fore.RED + "Vui lòng nhập số hợp lệ." + Fore.RESET)
                                    sleep(2)
                                    continue
                                if num < 1 or num > len(hosts):
                                    print(Fore.RED + "Số bạn nhập không có trong danh sách, vui lòng nhập lại..." + Fore.RESET)
                                    sleep(2)
                                    continue
                                target_ip = hosts[num - 1]
                                threads = []
                                step = 1000
                                print(Fore.YELLOW + "Đang quét port, vui lòng chờ..." + Fore.RESET)
                                for i in range(1, 65536, step):
                                    start = i
                                    end = min(i + step - 1, 65535)
                                    t = threading.Thread(target=scan_ports, args=(target_ip, start, end))
                                    threads.append(t)
                                    t.start()
                                for t in threads:
                                    t.join()
                                print(Fore.GREEN + "Đã quét xong." + Fore.RESET)
                                sleep(2)
                    except KeyboardInterrupt:
                        print(Fore.RED + "Đã dừng chương trình bởi người dùng." + Fore.RESET)
                        sleep(2)

                elif ok == "n":
                    print(Fore.RED +"Đã thoát chương trình do giá trị nhập bằng 'n'" + Fore.RESET)
                    sleep(2.4)
                    return
                else:
                    print(Fore.YELLOW + "Vui lòng nhập đúng giá trị chương trình yêu cầu" + Fore.RESET)
                    sleep(2)

        def resolve_domain(domain):
            try:
                print(Fore.CYAN + "Đang giải tên miền", end = "" + Fore.RESET)
                for i in range(3):
                    with print_lock:
                        print(".", end = "", flush = True)
                        sleep(0.5)
                ip_address = socket.gethostbyname(domain)
                return Fore.GREEN + f"\nĐã giải xong : {domain} -> {ip_address}" + Fore.RESET
                sleep(4)
            except socket.gaierror as e:
                return Fore.RED + f"\nLỗi khi giải tên miền thành IP, vui lòng thử lại, kiểm tra xem domain của mình đã đúng chưa." + Fore.RESET

        def chuc_nang_8():
            print(Fore.YELLOW + "không có cảnh báo, nhấn Ctrl + C để dừng chương trình" + Fore.RESET)
            sleep(1)
            while True:
                try:
                    domain = input(Fore.YELLOW + "Nhập domain của bạn (VD : google.com, không ghi gì và enter để thoát): " + Fore.RESET).strip().lower()
                    if domain.startswith("http://") or domain.startswith("https://"):
                        domain = domain.replace("http://", "").replace("https://", "")
                    if domain == "":
                        print(Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET)
                        sleep(2)
                        return
                    print(resolve_domain(domain))
                    sleep(2)
                except KeyboardInterrupt:
                    print(Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET)
                    sleep(2)
                    return

        def get_saved_wifi_passwords():
            result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8')
            profiles = re.findall(r"All User Profile\s*:\s*(.*)", result)
            wifi_list = []
            for profile in profiles:
                try:
                    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], encoding='utf-8')
                    password = re.search(r"Key Content\s*:\s*(.*)", profile_info)
                    if password:
                        wifi_list.append((profile, password.group(1)))
                    else:
                        wifi_list.append((profile, "No Password Found"))
                except subprocess.CalledProcessError:
                    wifi_list.append((profile, "Error retrieving password"))
            return wifi_list

        def chuc_nang_9():
            try:
                print(Fore.RED + "Cảnh báo : Tool này sẽ là tool bất hợp pháp khi chủ mạng chưa cho phép bạn lan truyền mật khẩu WiFi nhưng bạn vẫn cố sử dụng,\n           Vui lòng sử dụng tool với mục đích hợp pháp." + Fore.RESET)
                sleep(1.3)
                while True:
                    ok2 = input(Fore.YELLOW + "Bạn có muốn thực hiện thao tác này không? (y / n) : " + Fore.RESET).strip().lower()
                    if ok2 == "y":
                        countdown(3)
                        wifi_passwords = get_saved_wifi_passwords()
                        print(Fore.CYAN + "Đang truy cập" + Fore.RESET, end = "", flush = True)
                        for i in range(22):
                            print(Fore.CYAN + "." + Fore.RESET, end = "", flush=True)
                            sleep(0.02)
                        print("\n")
                        print(f"{'SSID':<30} | {'Password'}")
                        print("-" * 50)
                        for ssid, password in wifi_passwords:
                            print(Fore.GREEN + f"{ssid:<30} | {password}" + Fore.RESET)
                        sav = input(Fore.YELLOW + "Bạn có muốn lưu thông tin này vào file GetPass.txt không? (y / n) : " + Fore.RESET).strip().lower()
                        if sav == "y":
                            while True:
                                cl = input("Bạn có muốn 'clear' file GetPass.txt không? (y / n) : ").strip().lower()
                                if cl == "y":
                                    os.system("del GetPass.txt")
                                    print(Fore.GREEN + "Đã clear file GetPass.txt" + Fore.RESET)
                                    break
                                elif cl == "n" or cl == "":
                                    break
                                else:
                                    print(Fore.YELLOW + "Hãy nhập đúng giá trị mà chương trình đưa ra" + Fore.RESET)
                                    sleep(0.8)
                            try:
                                now = datetime.now()
                                timestamp = now.strftime("%H:%M:%S %d/%m/%Y")
                                with open("GetPass.txt", "a", encoding="utf-8") as f:
                                    f.write(f"{timestamp}\n")
                                    f.write("=" * 60 + "\n")
                                    f.write("PASSWORD WIFI TRONG MÁY TÍNH CỦA BẠN THEO THỜI GIAN THỰC\n")
                                    f.write("=" * 60 + "\n")
                                    for ssid, password in wifi_passwords:
                                        f.write(f"{ssid:<30} | {password}\n")
                                    f.write("\n" + "-" * 60 + "\n")
                                    f.write("\n")
                                    sleep(0.8)
                                    print(Fore.GREEN + "Đã ghi xong vào file GetPass.txt" + Fore.RESET)
                                    sleep(3.3)
                            except Exception:
                                print(Fore.YELLOW + "Đã có lỗi xảy ra, vui lòng thử lại chức năng" + Fore.RESET)
                                sleep(5)
                                return
                        elif sav == "n":
                            sleep(2)
                            pass
                    elif ok2 == "n" or ok2 == "":
                        print(Fore.RED + f"Đã thoát chương trình cho giá trị nhập là {ok2}" + Fore.RESET)
                        sleep(0.9)
                        return
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã thoát chương trình bởi người dùng" + Fore.RESET)
                sleep(0.8)
                return

        def chuc_nang_10():
            try:
                print(Fore.RED + "Cảnh báo: Tool này là tool bất hợp pháp, vui lòng sử dụng đúng mục đích\n           Tool này có thể bị mất kiểm soát, nếu muốn dừng chương trình thì hãy đợi có chữ THÀNH CÔNG và nhấn Ctrl + C")
                sleep(1.2)
                while True:
                    ok3 = input(Fore.YELLOW + "Bạn có muốn thực hiện thao tác không? (y / n) : " + Fore.RESET).strip().lower()
                    if ok3 == "y":
                        try:
                            print(Fore.YELLOW + "Loading" + Fore.RESET, end = "", flush = True)
                            for i in range(3):
                                print(".", end = "", flush = True)
                                sleep(1)
                            from smsbaro import man
                            man()
                        except KeyboardInterrupt:
                            print(Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET)
                            sleep(2)
                    elif ok3 == "n":
                        print(Fore.RED + f"Đã thoát chương trình do giá trị nhập là '{ok3}'")
                        sleep(2)
                    else:
                        print(Fore.YELLOW + "Vui lòng nhập đúng giá trị mà chương trình đưa ra" + Fore.RESET)
                        sleep(2)
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã thoát chương trình bởi người dùng" + Fore.RESET)
                sleep(2)
                return

        def chuc_nang_11():
            try:
                print(Fore.RED + "CẢNH CÁO ĐẶC BIỆT : ĐỂ TẮT CHƯƠNG TRÌNH VUI LÒNG NHẤN WINDOWS + SPACE (DẤU CÁCH)\n                    KHI NHẤN ALT + F4 THÌ CHƯƠNG TRÌNH SẼ BỊ GIẾT\n                    ĐỂ THOÁT CHỨC NĂNG KHI NHẬP INPUT THÌ HÃY NHẤN CTRL + C VÀ NHẤN ENTER" + Fore.RESET)
                sleep(1.2)
                while True:
                    xn = input(Fore.YELLOW + "Bạn muốn test ransomware trên máy này hay tạo file .exe? (nhập l để thực hiện trên máy, nhập e để tạo file .exe, 0 để thoát) : " + Fore.RESET).strip().lower()
                    if xn == "0":
                        print(Fore.RED + "Đã thoát chương trình do giá trị nhập là '0'" + Fore.RESET)
                        sleep(1.8)
                        return
                    elif xn == "l":
                        countdown(3)
                        from ransomware import ma
                        ma()
                    elif xn == "e":
                        print(Fore.YELLOW + "Lưu ý : Nếu máy bạn có một chương trình antivirus và nếu nó yêu cầu quét thư viện khi xuất file .exe thì cứ để nó xuất đi" + Fore.RESET)
                        while True:
                            ch_na = input("Bạn có muốn đổi tên file .exe không hay là giữ nguyên (ransomware.exe)? (y / n) : ").strip().lower()
                            if ch_na == "y":
                                name = input("Nhập tên cần đổi : ").strip()
                                countdown(3)
                                print("START CREATING FILE...")
                                sleep(2)
                                try:
                                    os.system(f"pyinstaller --onefile --name {name} ransomware.py")
                                    sleep(1.45)
                                    path = os.path.abspath(f"dist/{name}.exe")
                                    print(Fore.GREEN + f"Đã tạo xong file {name}.exe, nằm ở {path}" + Fore.RESET)
                                except Exception as e:
                                    print(Fore.RED + "Đã xảy ra lỗi, vui lòng thử lại" + Fore.RESET)
                                    a = input("Để xem lỗi, hãy nhấn Enter...")
                                    if a == "":
                                        print(Fore.RED + "Lỗi : " + Fore.RESET, "e")
                                break
                            elif ch_na == "n":
                                print("Lưu ý : Tên file mặc định sau khi tạo sẽ là ransomware.exe")
                                sleep(1.56)
                                countdown(3)
                                try:
                                    os.system("pyinstaller --onefile ransomware.py")
                                    sleep(1.45)
                                    path = os.path.abspath("dist/ransomware.exe")
                                    print(Fore.GREEN + f"Đã tạo xong file ransomware.exe, nằm ở {path}")
                                except Exception as e:
                                    print(Fore.RED + "Đã xảy ra lỗi, vui lòng thử lại" + Fore.RESET)
                                    a = input("Để xem lỗi, hãy nhấn Enter...")
                                    if a == "":
                                        print(Fore.RED + "Lỗi : " + Fore.RESET, "e")
                                    else:
                                        print(Fore.YELLOW + "Vui lòng nhập đúng giá trị mà chương trình đưa ra" + Fore.RESET)
                                        sleep(1.2)
                                break
                    else:
                        print(Fore.YELLOW + "Vui lòng nhập đúng giá trị chương trình đưa ra" + Fore.RESET)
                        sleep(2)
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã dừng chương trình bời người dùng" + Fore.RESET)
                sleep(2)
                return

        def khong_dau(text: str) -> str:
            normalized = unicodedata.normalize('NFD', text)
            no_tone = ''.join(
                c for c in normalized
                if unicodedata.category(c) != 'Mn'
            )
            no_tone = no_tone.replace('đ', 'd').replace('Đ', 'D')
            return no_tone

        def chuc_nang_12():
            try:
                print(Fore.YELLOW + "Lưu ý : Vì không hỗ trợ dấu nên khi bạn ghi từ nào có dấu thì chương trình sẽ đưa ra chữ Ascii không dấu" + Fore.RESET)
                sleep(1)
                while True:
                    text = input("Nhập từ của bạn (Ctrl + C để thoát) : ")
                    art = text2art(khong_dau(text))
                    print("Đang đọc nội dung...")
                    sleep(0.4)
                    print("Đang dịch chữ...")
                    sleep(0.6)
                    for i in range(3):
                        print(".", end = "", flush = True)
                        sleep(0.3)
                    sleep(3)
                    print(Fore.GREEN + "\nĐã dịch xong:\n" + Fore.RESET)
                    print(art)
                    sleep(2.4)
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã thoát chương trình bởi người dùng" + Fore.RESET)
                sleep(2)
                return

        def chuc_nang_13():
            print(Fore.RED + "Cảnh báo : File audio của bạn bắt buộc phải không có dấu và không có khoảng cách\n           Nhấn Ctrl + C để dừng")
            warnings.filterwarnings("ignore", category=UserWarning)
            os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
            file = input("Nhập đầy đủ đường dẫn file (không ghi gì để thoát chương trình): ")
            if file == "":
                print(Fore.RED + "Đã thoát chương trình" + Fore.RESET)
                sleep(0.8)
            try:
                if not os.path.isfile(file):
                    raise FileNotFoundError(Fore.YELLOW + f"Không tìm thấy file: {file}" + Fore.RESET)
                pygame.mixer.init()
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                print("Nhấn Enter để tạm dừng / tiếp tục, hoặc 'q' để thoát.", end="", flush=True)
                paused = False
                while True:
                    if not pygame.mixer.music.get_busy() and not paused:
                        sys.stdout.write(Fore.GREEN + "\rPhát xong.                                           \n" + Fore.RESET)
                        sys.stdout.flush()
                        sleep(1)
                        break
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode("utf-8", errors="ignore").lower()
                        if key == '\r':
                            sys.stdout.write("\r" + " " * 100 + "\r")
                            if not paused:
                                pygame.mixer.music.pause()
                                paused = True
                                sys.stdout.write("Đã tạm dừng. Nhấn Enter để tiếp tục hoặc 'q' để thoát.")
                            else:
                                pygame.mixer.music.unpause()
                                paused = False
                                sys.stdout.write("Tiếp tục phát. Nhấn Enter để tạm dừng hoặc 'q' để thoát.")
                            sys.stdout.flush()
                        elif key == 'q':
                            pygame.mixer.music.stop()
                            sys.stdout.write("\r" + " " * 100 + "\r")
                            sys.stdout.write(Fore.GREEN + "Đã dừng phát nhạc.\n" + Fore.RESET)
                            sys.stdout.flush()
                            sleep(0.8)
                            break
            except FileNotFoundError as e:
                print(e)
                sleep(2)
                return
            except pygame.error as e:
                print(Fore.YELLOW + f"Lỗi pygame: {e}\nVui lòng thử lại sau" + Fore.RESET)
                sleep(2)
                return
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã dừng chương trình" + Fore.RESET)
                sleep(0.8)
                return
            except Exception as e:
                print(Fore.YELLOW + f"Lỗi: {e}\nVui lòng thử lại chương trình"+ Fore.RESET)
                sleep(2)
                return

        def chuc_nang_14():
            print(Fore.RED + "Cảnh báo : File video của bạn bắt buộc phải không có dấu và không có khoảng cách\n           Nhấn Ctrl + C để dừng")
            sleep(0.8)
            while True:
                try:
                    ten = "Audio.mp3"
                    video_file = input("Nhập đầy đủ file Video của bạn (không ghi gì để thoát) : ")
                    if video_file == "":
                        print(Fore.RED + "Đã thoát chương trình" + Fore.RESET)
                        sleep(0.8)
                        return
                    if not os.path.isfile(video_file):
                        raise FileNotFoundError(Fore.YELLOW + f"Không tìm thấy file {video_file}, vui lòng thử lại" + Fore.RESET)
                    print("Đang ghi âm thanh...")
                    sleep(3)
                    video = VideoFileClip(video_file)
                    audio = video.audio
                    while True:
                        doi = input(Fore.CYAN + "File sẽ có tên là Audio.mp3, bạn có muốn đổi tên file không? (y / n) : " + Fore.RESET).strip().lower()
                        if doi == "y":
                            ten = input("Nhập tên file : ").strip()
                            if not ".mp3" in ten:
                                ten = ten + ".mp3"
                            print("Đang ghi tên...")
                            sleep(2)
                            break
                        elif doi == "n" or doi == "":
                            break
                        else:
                            print(Fore.YELLOW + "Vui lòng nhập đúng giá trị chương trình đưa ra" + Fore.RESET)
                            sleep(0.8)
                    file_name = input
                    audio.write_audiofile(ten)
                    print(Fore.GREEN + f"Đã lưu âm thanh vào {ten}" + Fore.RESET)
                    sleep(1)
                except KeyboardInterrupt:
                    print(Fore.RED + "\nĐã thoát chương trình" + Fore.RESET)
                    sleep(0.8)
                    return
                except FileNotFoundError:
                    print(Fore.YELLOW + f"Không tìm thấy file {video_file}, vui lòng thử lại chương trình" + Fore.RESET)
                    sleep(1.2)
                    return
                except Exception as e:
                    print(Fore.YELLOW + f"Lỗi trong quá trình ghi : {e}\nVui lòng thử lại chương trình" + Fore.RESET)
                    sleep(3)
                    return

        def menu_and_input():
            try:
                da_chay_chuc_nang_0 = False
                try:
                    while True:
                        os.system("cls")
                        ve_chu()
                        width = 110
                        print(Fore.BLUE + "\nCác tính năng trong chương trình lần này:" + Fore.RESET)
                        print(Fore.BLUE + "=" * width + Fore.RESET)
                        for item in items:
                            line = f"|| {item}"
                            print(Fore.BLUE + line.ljust(width-2) + "||" + Fore.RESET)
                        print(Fore.BLUE + "=" * width + Fore.RESET)
                        if da_chay_chuc_nang_0:
                            print(Fore.YELLOW + "Info Page : https://trankhanhtoan-py.github.io/info2" + Fore.RESET)
                        try:
                            chuc_nang = int(input("Nhập chức năng (số): "))
                            if chuc_nang == 0:
                                chuc_nang_0()
                                da_chay_chuc_nang_0 = True
                            elif chuc_nang == 1:
                                chuc_nang_1()
                            elif chuc_nang == 2:
                                chuc_nang_2()
                            elif chuc_nang == 3:
                                chuc_nang_3()
                            elif chuc_nang == 4:
                                chuc_nang_4()
                            elif chuc_nang == 5:
                                chuc_nang_5()
                            elif chuc_nang == 6:
                                print(Fore.RED + "Cảnh báo : Nhấn Ctrl + C để dừng chương trình\n           Khi spam email có thể bị mất kiểm soát dẫn đến không thể dừng được, vui lòng đợi chương trình dừng sau khi nhấn Ctrl + C hoặc đóng terminal\n           Cần có file acc.txt nằm cùng thư mục file chạy để lấy email và app password, các accounts được viết theo {email}|{app_password}\n           Tool hơi chậm do phải xử lý thông tin, vui lòng chờ." + Fore.RESET)
                                sleep(0.8)
                                while True:
                                    try:
                                        TARGET = input("Nhập email người nhận: ").strip()
                                        while True:
                                            try:
                                                targ = int(input("Nhập số lượng email muốn gửi (Khuyến khích : 300, không quá 600 để không bị time out, 0 để thoát chương trình): "))
                                                if targ == 0:
                                                    print(Fore.RED + "Đã thoát chương trình" + Fore.RESET)
                                                    sleep(0.8)
                                                    menu_and_input()
                                                    break
                                                elif targ < 0:
                                                    print("Số lượng không hợp lệ.")
                                                    continue
                                                else:
                                                    chuc_nang_6(TARGET, targ)
                                                    break
                                            except ValueError:
                                                print("Vui lòng nhập số nguyên hợp lệ.")
                                    except KeyboardInterrupt:
                                        print(Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET)
                                        sleep(2)
                                        break
                            elif chuc_nang == 7:
                                chuc_nang_7()
                            elif chuc_nang == 8:
                                chuc_nang_8()
                            elif chuc_nang == 9:
                                chuc_nang_9()
                            elif chuc_nang == 10:
                                chuc_nang_10()
                            elif chuc_nang == 11:
                                chuc_nang_11()
                            elif chuc_nang == 12:
                                chuc_nang_12()
                            elif chuc_nang == 13:
                                chuc_nang_13()
                            elif chuc_nang == 14:
                                chuc_nang_14()
                            elif chuc_nang == 15:
                                print(Fore.YELLOW + "Chức năng này không hoạt động." + Fore.RESET)
                                sleep(5)
                            elif chuc_nang == 99:
                                while True:
                                    rem = input("Bạn có muốn gỡ tất cả các gói vừa cài không? (y / n) : ").strip().lower()
                                    if rem == "y":
                                        print("CHECKING LIBRARY...")
                                        sleep(2)
                                        os.system("pip uninstall -r requirements.txt -y")
                                        raise SystemExit(Fore.RED + "\nĐã thoát chương trình." + Fore.RESET)
                                    elif rem == "n" or rem == "":
                                        raise SystemExit(Fore.RED + "\nĐã thoát chương trình." + Fore.RESET)
                                    else:
                                        print("Vui lòng nhập đúng giá trị chương trình đưa ra.")
                                        sleep(0.8)
                            else:
                                print(Fore.YELLOW + "Hãy chọn chức năng có trong menu" + Fore.RESET)
                                sleep(1)
                        except ValueError:
                            print(Fore.YELLOW + "Giá trị nhập phải là số, vui lòng nhập lại" + Fore.RESET)
                            sleep(1)
                except KeyboardInterrupt:
                    menu_and_input()
            except EOFError:
                menu_and_input()

        def giao_dien():
            ve_chu()
            print(Fore.GREEN + f"Tool by Trần Khánh Toàn - Ver {__version__}")
            print(Fore.RED + "\nCảnh báo : Các tính năng trong đây bao gồm auto có thể bị mất kiểm soát.")
            print(Fore.YELLOW + "\nTip : Để thoát chương trình, hãy bấm Ctrl + C. Để thoát chương trình (auto), hãy di chuột lên phía trên cùng góc bên trái để dừng thẳng chương trình.")
            print("Sau khi đọc xong, nhấn Enter để vào Menu hoặc Ctrl + C để thoát...")
            key = msvcrt.getch()
            if key == b'\r':
                menu_and_input()

            elif key == b'\x03':
                while True:
                        rem = input("Bạn có muốn gỡ tất cả các gói vừa cài không? (y / n) : ").strip().lower()
                        if rem == "y":
                            print("CHECKING LIBRARY...")
                            sleep(2)
                            os.system("pip uninstall -r requirements.txt -y")
                            raise SystemExit(Fore.RED + "\nĐã thoát chương trình." + Fore.RESET)
                        elif rem == "n" or rem == "":
                            raise SystemExit(Fore.RED + "\nĐã thoát chương trình." + Fore.RESET)
                        else:
                            print("Vui lòng nhập đúng giá trị chương trình đưa ra.")
                            sleep(0.8)
            else:
                giao_dien()
        def main():
            try:
                giao_dien()
            except KeyboardInterrupt:
                print(Fore.RED + "\nĐã thoát chương trình" + Fore.RESET)
                
        if __name__ == "__main__":
            main()
    elif build >= 22000:
        print(f"\033[0mĐây là Windows 11, dừng chương trình\033[0m")
        sys.exit(0)
elif sy == "Linux":
    dis = (get_linux_distribution())
    if dis == "Kali GNU/Linux":
        print("Kali Linux")
        sleep(0.4)
        print("OK")
        sleep(0.8)
        print("CHECKING LIBRARY AND MODULES...")
        sleep(1)
        venv_available = check_venv_module()
        in_venv = check_in_venv()
        print("Trạng thái kiểm tra Python venv:")
        print(f"- Module 'venv' có sẵn: {'Có' if venv_available else 'Không'}")
        print(f"- Đang ở trong môi trường ảo: {'Có' if in_venv else 'Không'}")
        if not venv_available:
            while True:
                dow = input("Chương trình của bạn không có venv, bạn có muốn chương trình cài venv không? (y / n) : ").strip().lower()
                if dow == "y":
                    os.system("sudo apt install python3-venv")
                    print("\nĐã cài xong venv, đang chuẩn bị tạo môi trường ảo...")
                    sleep(0.6)
                    os.system("python3 -m venv venv")
                    print("Đã tạo xong môi trường ảo, đang kích hoạt môi trường ảo...")
                    sleep(0.6)
                    os.system("venv/bin/python pyauto.py")
                    print("Đã kích hoạt venv, kiểm tra thư viện...")
                    sleep(1)
                    break
                elif dow == "n":
                    print("Vui lòng cài venv để chạy chương trình. TẠM BIỆT!")
                    sys.exit(0)
                else:
                    print("Vui lòng nhập đúng giá trị chương trình đưa ra")
                    sleep(0.8)
        while True:
            try:
                from moviepy import VideoFileClip
                import pygame
                import warnings
                from datetime import datetime
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                import random
                import tkinter as tk
                import shutil
                import speedtest
                import re
                import signal
                import nmap
                from colorama import Fore, Style, init
                import pygetwindow as gw
                import pyautogui
                import msvcrt
                import keyboard
                import socket
                import threading
                import sys
                import math
                from ctypes import cast, POINTER
                from comtypes import CLSCTX_ALL
                from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                from threading import Lock
                import unicodedata
                from art import text2art
                print("OK")
                print("Chương trình đang được cập nhật , vui lòng chờ phiên bản mới nhất...")
                sys.exit(0)
            except ModuleNotFoundError:
                sleep(2.4)
                print("DOWNLOAD FAIL, RETRYING...")
                sleep(2.4)
                download_lib()
    else:
        print("Chương trình đang cập nhật, vui lòng chờ...")


