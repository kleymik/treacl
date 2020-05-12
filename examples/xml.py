from treacl import Treacl as tcl

def sample_xml():

    # xml sample from json wikipedia page
    person = tcl()
    person.firstName = "John"
    person.lastName  = "Smith"
    person.age       = 25
    person.address.streetAddress = "21 2nd Street"
    person.address.city          = "New York"
    person.address.state         =  "NY"
    person.address.postalCode    =  "10021"
    person.phoneNumbers  = [ tcl(), tcl() ]
    person.phoneNumbers[0].type   = "home"
    person.phoneNumbers[0].number = "212 555-1234"
    person.phoneNumbers[1].type   = "fax"
    person.phoneNumbers[1].number = "646 555-4567"
    person.sex.type = "male"



    return person

if __name__ == '__main__':

    # random snippet of XML - to illustrate conversion to treacl

    person_in_xml = '''
<person firstName="John" lastName="Smith" age="25">
  <address streetAddress="21 2nd Street" city="New York" state="NY" postalCode="10021" />
  <phoneNumbers>
    <phoneNumber type="home" number="212 555-1234"/>
    <phoneNumber type="fax" number="646 555-4567"/>
  </phoneNumbers>
  <sex type="male"/>
</person>
'''

    print("sample person in XML:")
    print(person_in_xml)

    person = sample_xml()
    print()
    print("sample person from TREACL:")
    print()
    person.pptree()
    print()
    print("Done")





