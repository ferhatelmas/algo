package com.ferhatelmas.eolimp.page30.q908;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws Exception{

    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int cnt = 0, tmp;
    long sum = 0;

    for(int i=0; i<n; i++) {
      tmp=in.nextInt();
      if(tmp>0 && tmp%6==0){
        cnt++;
        sum+=tmp;
      }
    }
    System.out.println(cnt + " " + sum);
  }

}