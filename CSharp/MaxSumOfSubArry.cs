//Author: Maple0
//Github:https://github.com/Maple0
//13th Oct 2016
//Get maximum sum of sub arrys in a given array
public class MaxSumOfSubArry
{
    public static int GetMaxSubArrySum(int[] array)
    {
        int size = array.Length;
        if (array.Length == 0)
            throw new Exception("empty array");
        int curr = 0;
        int sum = 0;
        int max = 0;
        while(curr < size)
        {
            sum += array[curr++];
            if (sum > max)
                max = sum;
            else if (sum < 0)
                sum = 0;
        }
        return max;
    }
}