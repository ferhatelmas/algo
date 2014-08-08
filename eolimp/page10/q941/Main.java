package page10.q941;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int mul = 1, sum = 0;
    for(char c : new Scanner(System.in).next().toCharArray()) {
      if(c >= '0' && c <= '9') {
        mul *= (c - '0');
        sum += (c - '0');
      }
    }
    System.out.println(mul - sum);
  }
}
