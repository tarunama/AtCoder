using System;

class AtCoder
{
    private void Solve()
    {
        string strs = Console.ReadLine();
        int count = 0;

        for (int i = 0; i < strs.Length; ++i)
        {
            foreach (char c in strs)
            {
                if (c == strs[i])
                {
                    ++count;
                }
            }
            if (count % 2 != 0)
            {
                Console.WriteLine("No");
                return;
            }
            count = 0;
        }
        Console.WriteLine("Yes");
    }

    static void Main()
    {
        new AtCoder().Solve();
    }
}