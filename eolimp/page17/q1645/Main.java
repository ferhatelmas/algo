package page17.q1645;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    long n = new Scanner(System.in).nextLong();
    int c = 0;
    for(char ch : Long.toBinaryString(n).toCharArray())
      if(ch == '1') c++;
    System.out.println((long)(Math.pow(2, c) - 1));
  }
}
