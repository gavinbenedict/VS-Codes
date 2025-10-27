import java.util.*;
public class Fibonnaci
{
    public static int fib(int n)
    {
        if(n==0)
        {
            return 0;
        }
        if(n==1 ||n==2)
        {
            return 1;
        }
        return fib(n-2)+fib(n-1);
    }

    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter value of N= ");
        int n=sc.nextInt();
        System.out.println("THe Fibonnaci series of "+n+" number=");
        for(int i=0;i<n;i++)
        {
            System.out.println(fib(i)+" ");
        }
    }
}
