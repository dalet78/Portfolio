# Portfolio_management


This program was created for personal use and study purposes. The program is divided into several main parts:

Telegram Bot: This component manages the user interface via Telegram. It handles the daily download of the necessary trading data and interacts with the user through a command menu. Additionally, it sends daily reports to the user.

Data Download and Processing: Responsible for downloading daily data from Yahoo, cleaning it according to specific needs, and making it available to the rest of the program in CSV format.

Trading: This is the core of the program, performing all the calculations and searching for specific conditions, essentially acting as a trigger event.

Report Generation: If the trading component identifies a positive outcome, the system creates a PDF report with the necessary trading information. This report is then sent to the user via Telegram.

Macroeconomic Report: This part, still under development, focuses on the macroeconomic aspect of the program. It partially performs web scraping to gather certain data and saves it locally.