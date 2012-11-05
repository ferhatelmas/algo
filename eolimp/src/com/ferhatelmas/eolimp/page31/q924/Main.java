package com.ferhatelmas.eolimp.page31.q924;

import java.text.DecimalFormat;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws Exception{

    String[] s = new BufferedReader(new InputStreamReader(System.in)).readLine().split(" ");
    double area = Double.parseDouble(s[0]), r1=Double.parseDouble(s[1]);
    System.out.println(new DecimalFormat("#########0.00")
        .format(Math.sqrt((Math.PI*r1*r1-area)/Math.PI)).replace(",", "."));
  }

}