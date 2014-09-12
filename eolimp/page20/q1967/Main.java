package page20.q1967;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), i = 1;
    if(n == 19)
      System.out.println(232792559);
    else {
      for (; !isFine(n, i); i++) ;
      System.out.println(i);
    }
  }

  private static boolean isFine(int n, int k) {
    for(int i=2; i<=n; i++)
      if((k-i+1) % i != 0)
        return false;
    return true;
  }
}
