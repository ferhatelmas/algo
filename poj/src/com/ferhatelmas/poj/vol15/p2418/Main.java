package com.ferhatelmas.poj.vol15.p2418;

import java.util.Scanner;
import java.util.TreeMap;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    TreeMap<String, Integer> map = new TreeMap<String, Integer>();
    int cnt = 0;

    while(in.hasNextLine()) {
      cnt++;
      String tree = in.nextLine();
      if(map.containsKey(tree)) map.put(tree, map.get(tree)+1);
      else map.put(tree, 1);
    }

    for(String tree : map.navigableKeySet()) {
      System.out.format("%s %.4f\n", tree, (map.get(tree)*100)/(double)cnt);
    }
  }

}
