using System;
using System.IO;

class Program
{
    static void Main(String[] args)
    {
        FileStream f = new FileStream("2015/01/input_a.txt", FileMode.Open);
        StreamReader r = new StreamReader(f);
        
        string my_input = r.ReadLine();
        int floor = 0;

        foreach (char c in my_input)
        {
            if (c == '(')
            {
                floor++;
            } 
            else 
            {
                floor--;
            }
        }

        Console.WriteLine(floor.ToString());
    }
}