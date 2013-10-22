package page1.q22;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(), cnt = 0;

    for(int i=Math.min(a, b); i<=Math.max(a, b); i++) {
      if(isPrime(i) && isPrime(Integer
          .parseInt(new StringBuilder(String.valueOf(i)).reverse().toString())))
        cnt++;
    }

    System.out.println(cnt);
  }

  private static boolean isPrime(int a) {
    if(a < 2) return false;
    for(int i=2; i<=Math.sqrt(a); i++) if(a%i==0) return false;
    return true;
  }

}