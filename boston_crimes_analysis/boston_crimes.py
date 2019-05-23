import csv
import matplotlib.pyplot as plt


police_area = {'A1':'Downtown', 'A15':'Charlestown', 'A7':'East Boston',
               'B2':'Roxbury', 'B3':'Mattapan', 'C6':'South Boston',
               'C11':'Dorchester', 'D4':'South End', 'D14': 'Brighton',
               'E5':'West Roxbury', 'E13':'Jamaica Plain', 'E18': 'Hyde Park'}

class crime_case:
    def __init__(self, data_list):
        self.id = data_list[0]
        self.type = data_list[1]
        self.district_code = data_list[2]
        self.date = [int(data_list[3]), int(data_list[4]), data_list[5]]
        self.hour = int(data_list[6])
        self.location = data_list[7]
        
    def get(self, index):
        if index == 0:
            return self.id
        elif index == 1:
            return self.type
        elif index == 2:
            return self.district_code
        elif index == 3:
            return self.date
        elif index == 4:
            return self.hour
        elif index == 5:
            return self.location
        else:
            return None
            

def column_rank (index, obj_list):
    dict = {}

    for obj in obj_list:
        if obj.get(index) in dict:
            dict[obj.get(index)] += 1
        else:
            dict[obj.get(index)] = 1

    return sorted(dict.items(), key = lambda x: x[1], reverse = True)


def crime_on_map (crime_type = 'all', year = 'all', hour = 'all'):
    ys = []
    xs = []
    
    for obj in crime_cases:
        # get cordinate
        cor = obj.get(5).strip('()').split(', ')
        y, x = float(cor[0]), float(cor[1])

        # ignore any invalid cordinate
        if y < 40:
            continue
        
        # ignore any invalid type of crime
        if not crime_type == 'all' and not crime_type == obj.get(1):
            continue
        # ignore any invalid year
        if not year == 'all' and not year == obj.get(3)[0]:
            continue
        #ignore any invalid hour
        if not hour == 'all' and not hour == obj.get(4):
            continue

        # create a list of corrdinate 
        ys.append(y)
        xs.append(x)
    
    # if there is nothing in the cordinate, it means crime type was invalid
    if len(ys) == 0:
        print('None Crime Found Base on Input')
        return None

    img = plt.imread('boston_map.png')
    plt.imshow(img, extent=[-71.20, -70.95, 42.23, 42.41])

    # Configure size of dot based on how many corrdinate to help better viewing
    size = 1/((len(ys)/40))
    
    # plot all the locations
    plt.title('{} Cases of {} Type of Crimes'.format(len(xs), crime_type))
    plt.text(-70.94, 42.38, 'Type: {}\nYear: {}\nHour: {}'.format(crime_type, year, hour))
    plt.scatter(xs,ys, s=size, c='r')
    plt.yticks([42.23, 42.41])
    plt.xticks([-71.20,-70.95])
    plt.show()



def score (obj_list):
    # weight dictionary bsed on personal opnion
    weight = {'Motor Vehicle Accident Response': 2, 'Larceny': 4, 'Medical Assistance': 1, 'Investigate Person': 2, 
              'Other': 1, 'Drug Violation': 5, 'Simple Assault': 5, 'Vandalism': 3, 'Verbal Disputes': 3, 'Towed': 1, 
              'Investigate Property': 3, 'Larceny From Motor Vehicle': 4, 'Property Lost': 6, 'Warrant Arrests': 8, 
              'Aggravated Assault': 8, 'Violations': 5, 'Fraud': 3, 'Residential Burglary': 7, 'Missing Person Located': 1, 
              'Auto Theft': 7, 'Robbery': 9, 'Harassment': 9, 'Property Found': 1, 'Missing Person Reported': 3, 
              'Confidence Games': 1, 'Police Service Incidents': 1, 'Disorderly Conduct': 3, 'Fire Related Reports': 4, 
              'Firearm Violations': 8, 'License Violation': 3, 'Restraining Order Violations': 5, 
              'Recovered Stolen Property': 1, 'Counterfeiting': 1, 'Commercial Burglary': 8, 'Liquor Violation': 2, 
              'Auto Theft Recovery': 1, 'Ballistics': 7, 'Landlord/Tenant Disputes': 2, 'Search Warrants': 5, 
              'Assembly or Gathering Violations': 3, 'Property Related Damage': 5, 'Firearm Discovery': 5, 
              'Operating Under the Influence': 4, 'License Plate Related Incidents': 2, 'Offenses Against Child / Family': 9, 
              'Other Burglary': 7, 'Evading Fare': 1, 'Embezzlement': 1, 'Service': 1, 'Prisoner Related Incidents': 5, 
              'Harbor Related Incidents': 1, 'Prostitution': 3, 'Homicide': 10, 'Criminal Harassment': 9, 'Arson': 10, 
              'HOME INVASION': 10, 'Bomb Hoax': 10, 'Aircraft': 1, 'Phone Call Complaints': 1, 'Explosives': 10, 
              'Manslaughter': 10, 'Gambling': 2, 'HUMAN TRAFFICKING': 10, 'INVESTIGATE PERSON': 2, 'Biological Threat': 8, 
              'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE': 10, 'Burglary - No Property Taken': 5}
    
    # call column rank function to get type of crime in the list and number of each type of crime
    crime_types = column_rank(1, obj_list)
    
    # calculate the weight score
    total_score = 0
    for types, number in crime_types:
        total_score += weight[types] * number
        
    # normalization
    score = total_score/len(obj_list)
    
    return score


# open file and get data using csv modual
with open('crime.csv', encoding='windows-1252') as f:
    raw = csv.reader(f)
    header = next(raw)
    data = list(raw)

# extract useful data and create class
crime_cases = []
for alist in data:
    useful_list = [alist[0], alist[2], alist[4], alist[8], alist[9], alist[10], alist[11], alist[-1]]
        
    crime_cases.append(crime_case(useful_list))

police_area_dict = {}

# create the dictionary key
for key, value in police_area.items():
    if value not in police_area_dict:
        police_area_dict[value] = []
            
for obj in crime_cases:
    for key in police_area:
        if obj.get(2) == key:
            police_area_dict[police_area[key]].append(obj)

crime_on_map()






