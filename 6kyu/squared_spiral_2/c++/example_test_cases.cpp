Describe(tests)
{
    It(fixedTests)
    {
        Assert::That(squaredSpiral(0, 0), Equals(0));
        Assert::That(squaredSpiral(1, 1), Equals(2));
        Assert::That(squaredSpiral(2, 0), Equals(10));
        Assert::That(squaredSpiral(2, 2), Equals(12));
        Assert::That(squaredSpiral(3, 3), Equals(30));
    }
};