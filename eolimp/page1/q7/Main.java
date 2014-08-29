package page1.q7;

import java.util.Scanner;

public class Main {

  private static int values[] = new int[]{1000, 500, 100, 50, 10, 5, 1};
  private static String chars = "MDCLXVI";

  public static void main(String[] args) {
    String ss[] = new Scanner(System.in).nextLine().split("\\+");
    System.out.println(eval(parse(ss[0]) + parse(ss[1])));
  }

  private static int parse(String s) {
    int sum = 0;
    for(int i=0, l=s.length(); i<l; i++) {
      int v1 = values[chars.indexOf(s.charAt(i))];
      if(i < l-1) {
        int v2 = values[chars.indexOf(s.charAt(i+1))];
        sum += v1 < v2 ? -v1 : v1;
      } else sum += v1;
    }
    return sum;
  }

  private static String eval(int n) {
    StringBuilder sb = new StringBuilder();
    int i = 0;
    while(n > 0) {
      if(n >= values[i]) {
        sb.append(chars.charAt(i));
        n -= values[i];
      } else i++;
    }
    return sb.toString()
        .replace("DCCCC", "CM")
        .replace("CCCC", "CD")
        .replace("LXXXX", "XC")
        .replace("XXXX", "XL")
        .replace("VIIII", "IX")
        .replace("IIII", "IV");
  }
}
