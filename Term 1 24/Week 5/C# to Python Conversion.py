
#Convert the following C# code into Python
'''
public static int Square(int number)
{
    return number * number;
}

public static string ConcatenateStrings(string str1, string str2)
{
    return str1 + str2;
}
public static int CountVowels(string input)
{
    string vowels = "aeiouAEIOU";
    int count = 0;

    foreach (char character in input)
    {
        if (vowels.Contains(character))
        {
            count++;
        }
    }

    return count;
}


public static int SumArray(int[] numbers)
{
    return numbers.Sum();
}
public static void PrintMultiples(int n)
{
    for (int i = 1; i <= 5; i++)
    {
        Console.Write(n * i + " ");
    }
    Console.WriteLine();
}
public static string GetDayOfWeek(int day)
{
    return Enum.GetName(typeof(DayOfWeek), day);
}
public static int FindMax(int[] numbers)
{
    return numbers.Max();
}
public static double CelsiusToFahrenheit(double celsius)
{
    return (celsius * 9 / 5) + 32;
}
public static bool IsPrime(int number)
{
    if (number < 2) return false;
    for (int i = 2; i <= Math.Sqrt(number); i++)
    {
        if (number % i == 0) return false;
    }
    return true;
}
public static string ReverseWords(string sentence)
{
    string[] words = sentence.Split(' ');
    Array.Reverse(words);
    return string.Join(' ', words);
}
'''


#Converted to Python
def square(number):
    return number * number

def concatenate_strings(str1, str2):
    return str1 + str2

def count_vowels(input):
    vowels = "aeiouAEIOU"
    count = 0
    for character in input:
        if character in vowels:
            count += 1
    return count

def sum_array(numbers):
    return sum(numbers)

def print_multiples(n):
    for i in range(1, 6):
        print(n * i, end=" ")
    print()

def get_day_of_week(day):
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day]

def find_max(numbers):
    return max(numbers)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_words(sentence):
    words = sentence.split(' ')
    words.reverse()
    return ' '.join(words)

