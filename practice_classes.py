class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


abhishek = Employee('abhishek', 'kulkarni')
#print(abhishek.email)

print(abhishek.first)   # Don't need to specify self manually this gets transformed into the bottom method
# run from the class
print(Employee.fullname(abhishek))
