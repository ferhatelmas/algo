package page10.q933;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int sum = 0;
    for(char c : String.valueOf(new Scanner(System.in).nextDouble()).toCharArray())
      if(c >= '0' && c <= '9') sum += c - '0';
    System.out.println(sum);
  }
}
