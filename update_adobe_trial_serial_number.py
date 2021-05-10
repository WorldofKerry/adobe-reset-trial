import xml.etree.ElementTree as ET


def update_trial_serial_number(fileLocation):
    tree = ET.parse(fileLocation)
    root = tree.getroot()
    print("Updating " + fileLocation)
    print('trial serial number from ' + root.find('.//*[@key="TrialSerialNumber"]').text + ' to ', end='')
    root.find('.//*[@key="TrialSerialNumber"]').text = str(int(root.find('.//*[@key="TrialSerialNumber"]').text)+1)
    print(root.find('.//*[@key="TrialSerialNumber"]').text)    
    tree.write(fileLocation)


fileLocations = ["C:\Program Files\Adobe\Adobe Illustrator CC 2018\Support Files\Contents\Windows\AMT\\application.xml", "C:\Program Files\Adobe\Adobe Photoshop CC 2018\AMT\\application.xml", "C:\Program Files\Adobe\Adobe Premiere Pro CC 2018\AMT\\application.xml"]

for fileLocation in fileLocations:
    update_trial_serial_number(fileLocation)