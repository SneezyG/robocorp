# robocorp
Bussines automation: Web scraping bot with python and selenium.

This bot scrape yahoo news website given a phrase, topic and a number of result pages. It scrape, clean, parse dates, download image relating to a particular news and finally write the news data to an excel file.



## requirements
1. An installation of Robocorp cli at (https://github.com/robocorp/rcc?tab=readme-ov-file#installing-rcc-from-the-command-line)



## usage
clone the project robot repo to your local machine:
  ```bash
  git clone https://github.com/SneezyG/robocorp
  ```
  
move to the repo root dir:
  ```bash
  cd robocorp
  ```

move to the robot dir:
  ```bash
  cd corp
  ```
  
build a robot.zip using robocorp cli:
  ```bash
  rcc robot wrap
  ```
  
  
## usage example
Once you're set up, you can call the robot by running:

```bash
$ rcc run
```

And you can change the default value for robot arguments in automate.py which is in the corp directory.

```bash
bot = Bot("https://news.yahoo.com/", phrase, topic, page)
```




