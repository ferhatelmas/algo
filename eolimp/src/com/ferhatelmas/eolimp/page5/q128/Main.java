package com.ferhatelmas.eolimp.page5.q128;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), cnt = 0;

    for(int i=0; i<10; i++)
      for(int j=0; j<10; j++)
        for(int k=0; k<10; k++)
          if(i+j+k == n) cnt++;
    System.out.println((int)Math.pow(cnt, 2));
  }
}
