package page7.q622;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int cnt = 0;
    for(char c : Integer.toBinaryString(new Scanner(System.in).nextInt()).toCharArray())
      if(c == '1') cnt += 1;
    System.out.println(cnt);
  }
}
