package com.ferhatelmas.eolimp.page30.q918;

import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {

  public static void main(String[] args) throws Exception{

    String[] s=new BufferedReader(new InputStreamReader(System.in)).readLine().split(" ");

    double x=Double.parseDouble(s[0]), y=Double.parseDouble(s[1]);

    if(x==0 || y==0) System.out.println("0");
    else if(x>0 && y>0) System.out.println("1");
    else if(x<0 && y>0) System.out.println("2");
    else if(x<0 && y<0) System.out.println("3");
    else if(x>0 && y<0) System.out.println("4");

  }

}