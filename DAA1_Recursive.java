/*Non-recursive approach*/
import java.util.Scanner; 
public class IterativeFibonacci { 
    public static void fib(int n) { 
        int a = 0, b = 1; 
        System.out.print("Fibonacci sequence up to " + n + " terms (Iterative): "); 
        if (n >= 1) System.out.print(a + " "); 
        if (n >= 2) System.out.print(b + " "); 
        for (int i = 2; i < n; i++) { 
            int c = a + b; 
            System.out.print(c + " "); 
            a = b; 
            b = c; 
        } 
    } 
 
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
 
        System.out.print("Enter number of terms: "); 
        int n = sc.nextInt(); 
        fib(n); 
        sc.close(); 
    } 
}


/*Recursive approach*/
import java.util.Scanner;
public class RecursiveFibonacci { 
    public static int fib(int n) { 
        if (n <= 1) { 
            return n; 
        } 
        return fib(n - 1) + fib(n - 2); 
    } 
    public static void main(String[] args) { 
        Scanner sc = new Scanner(System.in); 
        System.out.print("Enter number of terms: "); 
        int n = sc.nextInt(); 
        System.out.print("Fibonacci sequence up to " + n + " terms (Recursive): "); 
        for (int i = 0; i < n; i++) { 
            System.out.print(fib(i) + " "); 
        } 
        sc.close(); 
    } 
}
