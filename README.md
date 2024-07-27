# Website-Viewers-Booster

## Overview

This Script is a simple GUI application that boosts website viewing using Selenium. It allows users to input multiple website links and automatically iterates through them, boosting the view count. The application also supports proxy servers for anonymous web scraping.

## Features

1. **User-Friendly Interface**: An intuitive GUI makes it easy to input website links and start the boosting process.
2. **Selenium Automation**: Utilizes Selenium to automate web browsing, increasing view counts.
3. **Proxy Support**: Allows the use of proxy servers for anonymous web scraping.
4. **Real-Time Status**: Provides real-time updates on the number of sites visited and any failures.
5. **Threaded Operation**: The Selenium operation runs in a separate thread, ensuring the GUI remains responsive.

## Instructions

1. Ensure you have the necessary dependencies installed, including PyQt5 and Selenium.
2. Prepare a text file named `agents.txt` in the same directory as the script, containing a list of user agents, one per line.
3. Create another text file named `proxies.txt` for proxy server addresses. Each line should contain a proxy in the format `proxy:port`.
4. Run the script, and you'll be greeted with a GUI interface.
5. Input your desired website links in the three input fields.
6. Click the "Start" button to begin the boosting process. The application will randomly select proxies and iterate through the websites.
7. You can stop the process using the "Stop Selenium" button.

## Known Issues

1. Ensure you have the Firefox browser installed, as this script uses Selenium's Firefox driver.
2. The script assumes the format of the `proxies.txt` file to be `proxy:port` (ssl favorite). Any mismatches may lead to errors.
3. Depending on the websites' content and structure, the scroll and refresh actions might need adjustment.

