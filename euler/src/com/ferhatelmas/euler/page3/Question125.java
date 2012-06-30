package com.ferhatelmas.euler.page3;

import java.util.HashSet;

public class Question125 {

  public static void main(String[] args) {

    int number;
    HashSet<Integer> numbers = new HashSet<Integer>();
    for(int i=1; i<10000; i++) {
      number = i*i;
      for(int j=i+1; j<10000; j++) {
        number += j*j;
        if(number > 100000000) break;
        if(isPalindrome(number)) numbers.add(number);
      }
    }

    long sum = 0;
    for(int num : numbers) sum += num;

    System.out.println(sum);
  }

  private static boolean isPalindrome(int n) {

    char[] chars = String.valueOf(n).toCharArray();
    for(int i=0; i<chars.length/2; i++) {
      if(chars[i] != chars[chars.length-i-1]) return false;
    }

    return true;
  }

}
