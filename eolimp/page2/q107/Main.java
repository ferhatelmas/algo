package page2.q107;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),
        i = n/100, j = (n%100)/20, k = n % 20;
    System.out.println(Math.min(Math.min(i * 100 + j * 30 + k * 2,
        (i+1)*100), i * 100 + (j+1) * 30));
  }
}
