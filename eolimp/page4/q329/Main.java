package page4.q329;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s[] = new Scanner(System.in).nextLine().split(" ");
    int cnt = 0;
    for(String ss : s)
      if(!ss.trim().replaceAll("[^\\w\\d]", "").isEmpty()) cnt++;
    System.out.println(cnt);
  }
}
