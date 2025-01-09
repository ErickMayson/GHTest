#include <stdio.h>

void printFib(int termValue)
{
    if (n < 1)
    {
        printf("Invalid value. Please insert a positive value.\n");
        return;
    }

    int firstValue = 1;
    int secondValue = 0;

    for (int i = 1; i <= termValue; i++)
    {
        if (i > 2)
        {
            int currentValue = firstValue + secondValue;
            secondValue = firstValue;
            firstValue = currentValue;
            printf("%d ", currentValue);
        }
        else if (i == 1)
        {
            printf("%d ", secondValue);
        }
        else if (i == 2)
        {
            printf("%d ", firstValue);
        }
    }
}

int main()
{
    int termValue = 9;
    printFib(termValue);
    return 0;
}
