from api_class import Conference_List

if __name__ == '__main__':
    url = 'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences'
    conferences = Conference_List(url)
    print(conferences)                        # List all Conferences in Human Readable Format
    conferences.exact_duplicates()            # List all exact duplicates
    conferences.semantic_duplicates()         # List all semantic duplicates