package page40.q3918;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    StringBuilder sb = new StringBuilder();

    int i = 2;
    while(n > 1) {
      while(n%i == 0) {
        sb.append(' ').append(i);
        n /= i;
      }
      i++;
    }
    System.out.println(sb.substring(1));
  }
}
