contacts = {
    'ContactOne' : {'phone': '202-222-3333',
                 "twitter": "oneTwitter",
                 "github": "oneGithub"},
    'ContactTwo': {'phone': '703-222-3333',
                'twitter': 'twoTwitter',
                'github':'twoGithub'}
}

print "\nprint contacts"
print contacts

print "\nprint keys"
print contacts.keys()

print "\nprint values"
print contacts.values()

print "\nprint items"
print contacts.items()

print "\nloop through contacts.items"
for item, value in contacts.items():
    print item
    print value

print "\nformatted contact"
for item, value in contacts.items():
    print "{0}'s contact information is:".format(item)
    print "\tPhone: {0}".format(value.get("phone"))
    print "\tTwitter: {0}".format(value.get("twitter"))
    print "\tGithub: {0}".format(value.get("github"))