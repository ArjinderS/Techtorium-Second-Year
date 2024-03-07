
#base class for all programming subjects
class Programming:
    def get_details(self):
        return "\nMost used programming languages. Feel free to add any below\n"

#classes that inherit from parent class (programming)
class Python(Programming):
    def get_details(self):
        return "Python is it's own programming language"

class CSharp(Programming):
    def get_details(self):
        return "C# is also it's own programming language"

class Java(Programming):
    def get_details(self):
        return "Java is again it's own programming language"

#Making instances in this case programming languages
python_subject = Python()
csharp_subject = CSharp()
java_subject = Java()

#fetching details from respective inherited class
python_details = python_subject.get_details()
csharp_details = csharp_subject.get_details()
java_details = java_subject.get_details()

print("\nPython Details:", python_details)
print("\nC# Details:", csharp_details)
print("\nJava Details:", java_details)
