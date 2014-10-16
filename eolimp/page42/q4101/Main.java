package page42.q4101;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();

    ArrayList<Integer> ls = new ArrayList<Integer>();
    for(int i=100; i<1000; i++) {
      if(getDigitSum(i) == n) {
        ls.add(i);
      }
    }

    System.out.println(ls.size());
    for(int i : ls) System.out.println(i);
  }

  private static int getDigitSum(int n) {
    int sum = 0;
    for(char c : String.valueOf(n).toCharArray())
      sum += c - '0';
    return sum;
  }
}
