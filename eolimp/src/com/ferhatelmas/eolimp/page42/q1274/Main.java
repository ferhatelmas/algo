package com.ferhatelmas.eolimp.page42.q1274;

import java.util.Scanner;
import java.util.ArrayList;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n0, n1, n2, n3, n4;
    ArrayList<String> res=new ArrayList<String>();
    String s;
    while((n0=in.nextInt())!=0) {

      n1=3*n0;
      if(n1%2==0) {
        n2=n1/2;
        s=" even ";
      }
      else {
        n2=(n1+1)/2;
        s=" odd ";
      }
      n3=n2*3;
      n4=n3/9;
      s+=String.valueOf(n4);
      res.add(s);
    }

    for(int i=0; i<res.size(); i++)
      System.out.println((i+1) + "." + res.get(i));
  }

}