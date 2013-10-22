package page2.q109;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), m = 1, sum = 0;

    while(sum < n)
      sum += String.valueOf(m++).length();
    System.out.println(sum == n ? --m : 0);
  }
}
