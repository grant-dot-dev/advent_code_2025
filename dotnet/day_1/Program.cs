using System;
using System.IO;
using System.Linq;

string[] LoadInput(string filePath)
{
    return File.Exists(filePath) ? File.ReadAllLines(filePath) : Array.Empty<string>();
}

int RotateDial(int current, string rotation)
{
    char dirChange = char.ToUpper(rotation[0]);
    int amount = int.Parse(rotation.Substring(1));
    int delta = dirChange == 'R' ? amount : -amount;
    int newPos = ((current + delta) % 100 + 100) % 100;
    return newPos;
}

(int newPos, int passes) RotateAndCountPasses(int current, string rotation)
{
    char dirChange = char.ToUpper(rotation[0]);
    int amount = int.Parse(rotation.Substring(1));
    int delta = dirChange == 'R' ? amount : -amount;
    int newPos = ((current + delta) % 100 + 100) % 100;
    if (delta == 0)
        return (newPos, 0);
    int passes;
    if (delta > 0)
    {
        passes = (current + delta) / 100;
    }
    else
    {
        int abs = -delta;
        if (current == 0)
        {
            passes = abs / 100;
        }
        else
        {
            if (abs < current)
                passes = 0;
            else
                passes = ((abs - current) / 100) + 1;
        }
    }
    return (newPos, passes);
}

int Part1(int start, string[] moves)
{
    int counter = 0;
    int pos = start;
    foreach (var m in moves)
    {
        pos = RotateDial(pos, m);
        if (pos == 0)
            counter++;
    }
    return counter;
}

int Part2(int start, string[] moves)
{
    int pos = start;
    int total = 0;
    foreach (var m in moves)
    {
        var result = RotateAndCountPasses(pos, m);
        pos = result.newPos;
        total += result.passes;
    }
    return total;
}

void Main()
{
    bool isDev = false;
    var fileName = isDev ? "example.txt" : "input.txt";
    var coordinates = LoadInput(fileName);

    // part 1 = count the times lands on zero
    var result = Part1(50, coordinates);

    // part 2 - count the number of times it passes 0
    var passes = Part2(50, coordinates);

    Console.WriteLine($"Times hit 0 (landings): {result}");
    Console.WriteLine($"Times passing through 0 (including wraps): {passes}");
}

Main();