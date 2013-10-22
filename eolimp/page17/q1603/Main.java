package page17.q1603;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int sum = 0;
    for(char c : new Scanner(System.in).next().toCharArray())
      if(c > '0' && c <= '9') sum += c - '0';
    System.out.println(sum);
  }
}
