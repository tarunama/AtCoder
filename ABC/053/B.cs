using System;

class AtCoder
{
    static int Solve(string s)
    {
        int aIndex = -1;
        int zIndex = -1;
        int i = 0;

        foreach (char c in s)
        {
            if (c == 'A' && aIndex == -1)
            {
                aIndex = i;
            }
            else if (c == 'Z')
            {
                zIndex = i;
            }
            ++i;
        }

        return (zIndex - aIndex) + 1;
    }

    static void Main()
    {
        string s = Console.ReadLine();
        int answer = Solve(s);
        Console.WriteLine(answer);
    }
}
