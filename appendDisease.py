from wonderFiles import downloadLink, makeFile


def run(path, link):
  rawData = downloadLink(link)
  makeFile(path, rawData) 

def main():
  path = input('Enter the path to the file (include /filename.csv): ')
  link = input('Enter the link to the file: ')
  run(path, link)

if __name__ == "__main__":
    main()