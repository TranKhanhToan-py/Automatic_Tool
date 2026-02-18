from tkinter import *
from tkinter import messagebox
import sys
from time import sleep
import os
import subprocess
import io

root = Tk()
root.title("Automatic Tool - By Ton_Loan")
root.geometry("500x500")

def check_admin():
	return os.system("net session >nul 2>&1") == 0
	sleep(1.4)

print("CHECKING...")
if check_admin() == 1:
	print("Ok")
else:
	print("ERROR", end = " ")
	sleep(0.5)
	print("-> Vui lòng chạy lại chương trình với quyền Administrator.")
	sys.exit(0)
print("Đang khởi tạo chương trình...")

PROGRESS_EVERY = 1000
__version__ = "1.1.7"
while True:
	try:
		import requests
		break
	except ModuleNotFoundError:
		os.system("pip install requests")
GITHUB_REPO = "TranKhanhToan-py/Automatic_Tool"
GITHUB_RAW_URL = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/pyauto_gui.py"

def check_and_update():
	try:
		label1 = Label(root, text = "Kiểm tra cập nhật từ Github...")
		label1.grid(column = 0, row = 0)
		sleep(3)
		resp = requests.get(GITHUB_RAW_URL, timeout=10)
		if resp.status_code != 200:
			messagebox.showerror("Error", "Không thể tải file từ GitHub (status:", resp.status_code, ")")
			sleep(1.3)
			return
		latest_code = resp.text
		latest_version = None
		for line in latest_code.splitlines():
			if line.startswith("__version__"):
				parts = line.split("=", 1)
				if len(parts) == 2:
					latest_version = parts[1].strip().strip('"').strip("'")
				break

		if not latest_version:
			messagebox.showerror("Error from new Version", "Không tìm thấy dòng __version__ trong bản mới.")
			sleep(1.3)
			return

		if latest_version != __version__:
			messagebox.showinfo("New Version Found!", f"Có bản mới: {latest_version} (hiện tại: {__version__})")
			ans = messagebox.askquestion("Update?", "Bạn có muốn cập nhật không?: ").strip().lower()
			if ans == "Yes":
				script_path = os.path.abspath(sys.argv[0])
				try:
					with open(script_path, "w", encoding="utf-8") as f:
						f.write(latest_code)
					messagebox.showinfo("Update Successfully", "Đã cập nhật thành công. Vui lòng khởi động lại chương trình.")
					sys.exit(0)
				except Exception as e:
					print("Error", f"Lỗi khi ghi đè file: {e}")
					sleep(3)
			else:
				label = Label(root, text = "Lựa chọn : Không cập nhật!")
				label.grid(row = 1, column = 0 , sticky = "w")
		else:
			messagebox.showinfo("","Bạn đang ở phiên bản mới nhất, không cần cập nhật.")
			label = Label(root, text = "Không cần cập nhật!")
			label.grid(row = 1, column = 0 , sticky = "w")
	except Exception as e:
		messagebox.showerror("Error", f"Lỗi khi kiểm tra cập nhật: {e}")
		label = Label(root, text = "Lỗi khi kiểm tra!")
		label.grid(row = 1, column = 0 , sticky = "w")
		sleep(2)

check_and_update()

def list_drives():
	try:
		if hasattr(os, "listdrives"):
			return os.listdrives()
		else:
			from ctypes import windll
			drives = []
			bitmask = windll.kernel32.GetLogicalDrives()
			for letter in string.ascii_uppercase:
				if bitmask & 1:
					drives.append(f"{letter}:\\")
				bitmask >>= 1
			return drives
	except Exception as e:
		print(f"Error : {e}")

def download_lib():
	os.system("pip install -r requirements.txt")

def check_library():
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
			import pyzipper
			from zipfile import BadZipFile
			import signal
			import nmap
			from colorama import Fore, Style, init
			import pygetwindow as gw
			import pyautogui
			import msvcrt
			import keyboard
			import socket
			import threading
			import math
			from ctypes import cast, POINTER
			from comtypes import CLSCTX_ALL
			from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
			from threading import Lock
			import unicodedata
			from art import text2art 
			import qrcode 
			import string
			print("OK")
			sleep(0.3)
			break
		except ModuleNotFoundError:
			sleep(2.4)
			print("DOWNLOAD FAIL, RETRYING...")
			sleep(2.4)
			download_lib()
		
def find_tool(t):
	try:
		if t == "nmap":
			path = shutil.which(t)
			print(Fore.YELLOW + f"Đang tìm kiếm {t} trong PATH" + Fore.RESET)
			sleep(2)
			if path:
				print(Fore.GREEN + "Ok" + Fore.RESET)
			print(Fore.YELLOW + f"Không tìm thấy {t} trong PATH" + Fore.RESET)
			sleep(0.4)
			print(Fore.YELLOW + "Đang quét các ổ đĩa này trong máy tính để kiểm tra..." + Fore.RESET)
			sleep(1)
			o_dia = list_drives()
			for i in o_dia:
				print(i)
			for i in o_dia:
				for root, dirs, files in os.walk(i):
					if "nmap.exe" in files:
						path1 = root
						print(Fore.GREEN + f"Đã tìm thấy nmap ở {path1}" + Fore.RESET)
						sleep(0.2)
						add = input("Nmap chưa được thêm vào PATH, bạn có muốn thêm vào không? (y / n): ").strip().lower()
						if add == "y":
							new_path = rf"{path1}"
							try:
								if new_path not in os.environ["PATH"]:
									os.environ["PATH"] += os.pathsep + new_path
								print(Fore.GREEN + "Thêm tạm Nmap vào PATH thành công!" + Fore.RESET)
								sleep(1.2)
								return
							except Exception as e:
								print(Fore.RED + f"Lỗi xảy ra khi thêm PATH:\n{e}")
								menu_and_input()
						if add == "n":
							print(Fore.RED + "Đã thoát chương trình do chưa có Nmap trong PATH." + Fore.RESET)
							sleep(2)
							menu_and_input()
			print(Fore.YELLOW + "Không có Nmap trong máy tính" + Fore.RESET)
			sleep(2)
			menu_and_input()
	except Exception as e:
		return Fore.RED + f"Lỗi khi tìm kiếm công cụ {t}: {e}" + Fore.RESET
	except KeyboardInterrupt:
		return Fore.RED + "\nĐã dừng chương trình bởi người dùng" + Fore.RESET
		sleep(0.8)
		menu_and_input()

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
			"8. Lấy các Password WiFi đã kết nối trước đó",
			"9. Spam SMS (số điện thoại)",
			"10. Ransomware (troll)",
			"11. Tạo chữ ASCII art",
			"12. Nghe file mp3",
			"13. File mp4 -> mp3",
			"14. Giải nén file zip",
			"15. Tạo QR Code từ website",
			"16. Điều khiển",
			"17. Chương trình đang được update thêm...",
			"=" * 105,
			"99. Exit"
				]

root.mainloop()