from treacl import Treacl as tcl

def sample_json():

    # json sample from json wikipedia page
    person = tcl()
    person.firstName = "Jonn"
    person.lastName  = "Smith"
    person.age       = 25
    person.address.streetAddress = "21 2nd Street"
    person.address.city          = "New York"
    person.address.state         =  "NY"
    person.address.postalCode    =  "10021"
    person.address.phoneNumbers  = [ tcl(), tcl() ]
    person.address.phoneNumbers[0].type   = "home"
    person.address.phoneNumbers[0].number = "212 555-1234"
    person.address.phoneNumbers[1].type   = "fax"
    person.address.phoneNumbers[1].number = "646 555-4567"
    person.sex.type = "male"


    # or similarly with XML, in XML-with-properties form:
    #
    # <person firstName="John" lastName="Smith" age="25">
    #   <address streetAddress="21 2nd Street" city="New York" state="NY" postalCode="10021" />
    #   <phoneNumbers>
    #     <phoneNumber type="home" number="212 555-1234"/>
    #     <phoneNumber type="fax" number="646 555-4567"/>
    #   </phoneNumbers>
    #   <sex type="male"/>
    # </person>

    return person

if __name__ == '__main__':

    person_in_json = '''
    {
      "first name": "John",
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

    print("sample person in JSON:")
    print(person_in_json)

    person = sample_json()
    print("\nsample person in TREACL")
    person.pptree()






