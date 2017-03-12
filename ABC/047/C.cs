using System;

class Program
{
    static void Main()
    {
        string s = Console.ReadLine();
        int count = 0;
        char prev = s[0];

        foreach (char c in s)
        {
            if (prev != c)
            {
                ++count;
                prev = c;
            }
        }

        Console.WriteLine(count);
    }
}