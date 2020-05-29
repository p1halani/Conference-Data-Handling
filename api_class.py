import requests
from conference import Conference

class Conference_List():
    def __init__(self, url):
        try: 
            response = requests.get(url, timeout=(5, 14)) 
            response.raise_for_status()                 # Raise error in case of failure 
        except requests.exceptions.HTTPError as httpErr: 
            print ("Http Error:",httpErr) 
        except requests.exceptions.ConnectionError as connErr: 
            print ("Error Connecting:",connErr) 
        except requests.exceptions.Timeout as timeOutErr: 
            print ("Timeout Error:",timeOutErr) 
        except requests.exceptions.RequestException as reqErr: 
            print ("Something Else:",reqErr)
        else:
            print("[INFO] Successfully Fetched Data!!!!!!")
            self.conferences = []
            for free_conference in response.json()['free']:
                one_conf = Conference(free_conference)
                self.conferences.append(one_conf)
            
            for free_conference in response.json()['paid']:
                one_conf = Conference(free_conference)
                self.conferences.append(one_conf)
            

    def __repr__(self):
        print('\n================================================================\n')
        print('[INFO] Printing all Conferences')
        for one_conf in self.conferences:
            print("\n")
            print(one_conf)

        return '\n'

    @staticmethod
    def _recursive_compare(conf_1, conf_2, level='root'):
        if isinstance(conf_1, dict) and isinstance(conf_2, dict):
            if conf_1.keys() != conf_2.keys():
                return False
            else:
                common_keys = set(conf_1.keys())

            flag = True
            for k in common_keys:
                if(Conference_List._recursive_compare(conf_1[k], conf_2[k], level='{}.{}'.format(level, k))):
                    pass
                else:
                    flag =False
                    break
            
            return flag

        elif isinstance(conf_1, list) and isinstance(conf_2, list):
            if len(conf_1) != len(conf_2):
                return False
            common_len = min(len(conf_1), len(conf_2))

            flag = True
            for i in range(common_len):
                if(Conference_List._recursive_compare(conf_1[i], conf_2[i], level='{}[{}]'.format(level, i))):
                    pass
                else:
                    flag = False
                    break
            
            return flag

        else:
            if conf_1 != conf_2:
                return False
            return True
    
    @staticmethod
    def _remove_punctuation(s):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in s:
            if char not in punctuations:
                no_punct = no_punct + char
        
        return no_punct

    @staticmethod
    def _transform_possible(str1, str2):
        str1 = Conference_List._remove_punctuation(str1)
        str2 = Conference_List._remove_punctuation(str2)

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        i, j = 0, 0
        while (i<len(str1) and j<len(str2)):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(str2):
            return True
        return False

    def _semantic_diff(self, conf_1, conf_2):
        check_start_date = conf_1.start_date == conf_2.start_date
        check_end_date = conf_1.end_date == conf_2.end_date
        check_id = conf_1.id == conf_2.id
        check_lat = conf_1.lat == conf_2.lat
        check_long = conf_1.long == conf_2.long
        if (Conference_List._recursive_compare(conf_1.conf_details, conf_2.conf_details)):
            return False
        if (check_start_date and check_end_date and check_id and check_lat and check_long):
            if (Conference_List._transform_possible(conf_1.confName, conf_2.confName)):
                return True
            else:
                return False
        else:
            return False

    def exact_duplicates(self):
        print('\n=================================================\n[INFO] Exact Duplicates:')
        remove_duplicate_printing = set()
        for i, conf_1 in enumerate(self.conferences):
            both_same = False
            for j in range(i+1, len(self.conferences)):
                conf_2 = self.conferences[j]
                if (Conference_List._recursive_compare(conf_1.conf_details, conf_2.conf_details)):
                    if j not in remove_duplicate_printing:
                        both_same = True
                        remove_duplicate_printing.add(j)

            if both_same:
                print(conf_1)
                print()

        return

    def semantic_duplicates(self):
        print('\n=================================================\n[INFO] Semantic Duplicates:')
        for i, conf_1 in enumerate(self.conferences):
            both_same = False
            for j in range(i+1, len(self.conferences)):
                conf_2 = self.conferences[j]
                if(self._semantic_diff(conf_1, conf_2)):
                    both_same = True
                    break

            if both_same:
                print('First Sentence : ')
                print(conf_1)
                print('Semantic Similar Sentence: ')
                print(self.conferences[j])
                print()

        return 