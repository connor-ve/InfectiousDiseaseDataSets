import requests

# parse the headers from the wonder file
def parseCSVHeaders(lines):
  labels = []
  labels_index = 0
  data_index = 0
  for index, line in enumerate(lines):
    if line.startswith('column'):
      labels_index = index
      break

  for index, line in enumerate(lines):
    if line.startswith('tab delimited data'):
      data_index = index
      break
  
  titles = lines[labels_index+1:data_index]
  
  # print labels on new lines 
  for label in titles: 
    label = label.replace(',', ':')
    label = label.replace(';', ':')

    labels.append(label)
  # Join the labels with commas into a string 
  labels = ', '.join(labels)
  return labels

# parse the data from the wonder file
def parseCSVData(lines):
  data_index = 0
  end_index = 0
  
  for index, line in enumerate(lines):
    if line.startswith('tab delimited data'):
      data_index = index
      break
  
  for index, line in enumerate(lines):
    if line.startswith('U: Unavailable'):
      end_index = index
      break
  
  data = lines[data_index+1:end_index]
  # print(data_index, end_index) 
  return_data = []
  for line in data:
    return_data.append(line.replace('\t', ','))

  # replace first comma with a colon

  return_data[0] = return_data[0].replace(",", ":", 1)
  
  # replace - with None in return_data 
  # for index, line in enumerate(return_data):
  #   return_data[index] = line.replace('-', 'None')


  return_data.pop(-1)
  return return_data

# Main Function to start parse of the wonder file
def parseWonderFile(text):
  # print(text)
  lines = text.splitlines()
  headers = parseCSVHeaders(lines)
  datasets = parseCSVData(lines)
  
  finished_data = []
  finished_data.append(headers)
  finished_data.extend(datasets)

  return finished_data

  

# Download the file from the link
def downloadLink(link):
  response = requests.get(link)
  cleanData = parseWonderFile(response.text)
  return cleanData

# Create a file with the data
def makeFile(path, content):
  for line in content:
    # print(line)
    with open(path, 'a') as f:
      f.write(line + '\n')
      f.close()