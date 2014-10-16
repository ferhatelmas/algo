package page42.q4103;

import java.util.Scanner;

public class Main {

  private static String romans[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
  private static int values[] =  {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      System.out.println(toArabic(in.next()));
    }
  }

  private static int toArabic(String s) {
    int sum = 0, l = s.length();
    for(int i=0; i<romans.length; i++) {
      int j = romans[i].length();
      while(j <= l && s.substring(0, j).equals(romans[i])) {
        sum += values[i];
        s = s.substring(j);
        l -= j;
      }
    }
    return sum;
  }
}
