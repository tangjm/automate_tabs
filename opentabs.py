import sys
import webbrowser 
import datetime

def open_links(filename):
  urls = open(filename, "r")

  url_list = list(urls)
  url_count = len(url_list)

  print(f"Filename: {filename}")
  print(f'Tabs to open: {url_count}')

  for url in url_list:
    webbrowser.open_new_tab(url)
  print("")

  urls.close()

def get_date():
  date_today = str(datetime.datetime.now()).split()[0]
  return date_today

def main():
  files = sys.argv[1:]

  if not files:
    print("usage: file [file ...]")
    sys.exit(1)

  print(f"Date: {get_date()}")

  for file in files:
    open_links(file)

if __name__ == '__main__':
  main()