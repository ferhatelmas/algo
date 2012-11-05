package com.ferhatelmas.eolimp.page14.q395;

import java.util.Scanner;
import java.util.ArrayList;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    ArrayList<Integer> res=new ArrayList<Integer>();

    int n = in.nextInt();

    int[] buf=new int[n];
    boolean flag;

    for(int i=0; i<n; i++)
      buf[i]=in.nextInt();

    for(int i=0; i<n; i++) {
      flag = true;
      for(int j=0; j<n; j++) {
        if(buf[i]%buf[j]==0 && i!=j){
          flag = false;
          break;
        }
      }
      if(flag) res.add(buf[i]);
    }

    for(int i=0; i<res.size()-1; i++)
      System.out.print(res.get(i) + " ");

    System.out.println(res.get(res.size()-1));
  }

}