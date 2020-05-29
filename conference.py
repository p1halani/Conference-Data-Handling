class Conference():
    def __init__(self, conf_details):
        self.conf_details = conf_details
        self.venue = self.conf_details['venue'].strip()
        self.start_date = self.conf_details['confStartDate'].strip()
        self.end_date = self.conf_details['confEndDate'].strip()
        self.confName = self.conf_details['confName'].strip()
        self.reg_url = self.conf_details['confRegUrl'].strip()
        self.entryType = self.conf_details['entryType'].strip()
        self.id = self.conf_details['conference_id']
        self.lat = self.conf_details['lat']
        self.long = self.conf_details['long']

    def __repr__(self):
        args = []
        for ele in [self.confName, self.start_date, self.venue, self.entryType, self.reg_url]:
            if ele != '':
                args.append(ele)
        res = ','.join(args)
        return res