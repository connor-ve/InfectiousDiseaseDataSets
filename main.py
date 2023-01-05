from wonderFiles import downloadLink, makeFile


def run(path, link):
  rawData = downloadLink(link)
  # make the file
  makeFile(path, rawData) 

def main():
  # Needed to make sure requests doesnt crash for initial set up
  # files_path = [['./WonderTableLinks/MeaslesLinks.txt','./Diseases2022Data/Measles&MalariaData']]
  # files_path = [['./WonderTableLinks/MumpsLinks.txt','./Diseases2022Data/MumpsData']]  
  # files_path = [['./WonderTableLinks/PneumoccalLinks.txt','./Diseases2022Data/PneumoccalDiseasesData']]
  # files_path = [['./WonderTableLinks/SyphilisLinks.txt','./Diseases2022Data/SyphilisData']]
  files_path = [['./WonderTableLinks/TuberculosisLinks.txt','./Diseases2022Data/TuberculosisData']]

  for diseases in files_path:
    with open(diseases[0], 'r') as f:
      lines = f.readlines()
      cnt = 0
      for line in lines:
        cnt += 1
        # print(line)
        link = line.split('_')[1][:-2]
        path = f'./{diseases[1]}/Week{cnt}.csv'
        run(path, link)

if __name__ == "__main__":
    main()