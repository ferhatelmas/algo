package page40.q3917;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();

    boolean f = true;
    for(int i=(int)Math.sqrt(n); i>1; i--)
      if(n%i == 0) {
        f = false;
        break;
      }

    System.out.println(f ? "True" : "False");
  }
}
