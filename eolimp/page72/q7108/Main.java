package page72.q7108;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    StringBuilder sb = new StringBuilder();
    for(char c : new Scanner(System.in).next().toCharArray()) {
      for(int i=c-'0'; i>=0; i--) sb.append(c);
    }
    System.out.println(sb.toString());
  }
}
