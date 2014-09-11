package page19.q1885;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = "6255456376";
    int sum = 0;
    for(char ch : new Scanner(System.in).next().toCharArray()) {
      if(ch == '-') sum++;
      else sum += s.charAt(ch-'0') - '0';
    }
    System.out.println(sum);
  }
}
