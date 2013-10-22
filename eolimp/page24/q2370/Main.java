package page24.q2370;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),cnt = 0;
    for(int i=0; i<100; i++)
      for(int j=0; j<100; j++)
        if(n-i-j == 0) cnt++;
    System.out.println(cnt);
  }
}
