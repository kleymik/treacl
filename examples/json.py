from treacl import Treacl as t

# random snippet of JSON - equivalent representation using treacl


def sample_json():

    # json sample from json wikipedia page
    person = t()
    person.firstName = "John"
    person.lastName  = "Smith"
    person.age       = 25
    person.address.streetAddress = "21 2nd Street"
    person.address.city          = "New York"
    person.address.state         =  "NY"
    person.address.postalCode    =  "10021"
    person.phoneNumbers  = [ t(), t() ]
    person.phoneNumbers[0].type   = "home"
    person.phoneNumbers[0].number = "212 555-1234"
    person.phoneNumbers[1].type   = "fax"
    person.phoneNumbers[1].number = "646 555-4567"
    person.sex.type = "male"

    return person

if __name__ == '__main__':

    person_in_json = '''
{ "first name": "John",
  "last name": "Smith",
  "age": 25,
  "address": {
      "street address": "21 2nd Street",
      "city": "New York",
      "state": "NY",
      "postal code": "10021"
  },
  "phone numbers": [
      {
          "type": "home",
          "number": "212 555-1234"
      },
      {
          "type": "fax",
          "number": "646 555-4567"
      }
  ],
  "sex": {
      "type": "male"
  }
}
'''

    print("Sample person in JSON:")
    print(person_in_json)

    person = sample_json()
    print("Sample person from TREACL:")
    person.pptree()

    print()
    print("Sample person: regex filter '^.+e$' list of paths")
    for p in person.tree_find_paths_regex("^.+e$"): print(p)





