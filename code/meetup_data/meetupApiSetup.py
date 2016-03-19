# should we put all the paths that we want to access into this class? Then there'd only
# be one place to go to access them.


class MeetupSetup:

    def __init__(self):

        self.url_path = 'https://api.meetup.com'
        self.key = '49574f71385238665d2e292d40682b'

        self.category_path = "/2/categories"

