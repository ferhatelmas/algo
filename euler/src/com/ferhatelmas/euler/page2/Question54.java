package com.ferhatelmas.euler.page2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Question54 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new FileReader("poker.txt"));
        String line;
        int cnt = 0;

        while((line=br.readLine()) != null) {
            String[] cards = line.split(" ");
            if(getWinner(cards)) cnt++;
        }

        System.out.println(cnt);
    }

    private static boolean getWinner(String[] cards) {
        List<Integer> player1 = new ArrayList<Integer>();
        List<Integer> player2 = new ArrayList<Integer>();

        for(int i=0; i<10; i++) {
            if(i<5) player1.add(cardValue(cards[i]));
            else player2.add(cardValue(cards[i]));
        }
        return play(player1, player2);
    }

    private static boolean play(List<Integer> player1, List<Integer> player2) {
        List<Integer> pp1 = getPlayerValues(player1);
        List<Integer> pp2 = getPlayerValues(player2);

        boolean p1 = isRoyalFlush(pp1, player1);
        boolean p2 = isRoyalFlush(pp1, player2);

        if(p1 && !p2) return true;
        else if(!p1 && p2) return false;
        else {
            p1 = isStraightFlush(pp1, player1);
            p2 = isStraightFlush(pp2, player2);

            if(p1 && !p2) return true;
            else if(!p1 && p2) return false;
            else if(p1 && p2) return compare(pp1, pp2);
            else {

                int t1 = isKind(pp1, 4, false);
                int t2 = isKind(pp2, 4, false);

                if(t1 != -1 && t2 == -1) return true;
                else if(t1 == -1 && t2 != -1) return false;
                else if(t1 != -1 && t2 != -1) return t1 > t2 || (t1 == t2 && compare(pp1, pp2));
                else {

                    t1 = isKind(pp1, 3, false);
                    int t11 = isKind(pp1, 2, true);
                    Collections.reverse(pp1);
                    t2 = isKind(pp2, 3, false);
                    int t22 = isKind(pp2, 2, true);
                    Collections.reverse(pp2);

                    if(t1 != -1 && t11 != -1 && (t2 == -1 || t22 == -1)) return true;
                    else if((t1 == -1 || t11 == -1) && t2 != -1 && t22 != -1) return false;
                    else if(t1 != -1 && t11 != -1 && t2 != -1 && t22 != -1) return t1 > t2 || (t1 == t2 && t11 > t22);
                    else {
                        p1 = isFlush(player1);
                        p2 = isFlush(player2);

                        if(p1 && !p2) return true;
                        else if(!p1 && p2) return false;
                        else if(p1 && p2) return compare(pp1, pp2);
                        else {
                            p1 = isStraight(pp1);
                            p2 = isStraight(pp2);

                            if(p1 && !p2) return true;
                            else if(!p1 && p2) return false;
                            else if(p1 && p2) return compare(pp1, pp2);
                            else {
                                t1 = isKind(pp1, 3, false);
                                t2 = isKind(pp2, 3, false);

                                if(t1 != -1 && t2 == -1) return true;
                                else if(t1 == -1 && t2 != -1) return false;
                                else if(t1 != -1 && t2 != -1) return t1 > t2 || (t1 == t2 && compare(pp1, pp2));
                                else {
                                    t1 = isKind(pp1, 2, false);
                                    t11 = isKind(pp1, 2, true);
                                    Collections.reverse(pp1);
                                    t2 = isKind(pp2, 2, false);
                                    t22 = isKind(pp2, 2, true);
                                    Collections.reverse(pp2);

                                    if(t1 == t11) t11 = -1;
                                    if(t2 == t22) t22 = -1;

                                    if(t1 != -1 && t11 != -1 && t1 != t11 && (t2 == -1 || t22 == -1)) return true;
                                    else if((t1 == -1 || t11 == -1) && t2 != -1 && t22 != -1 && t2 != t22) return false;
                                    else if(t1 != -1 && t11 != -1 && t1 != t11 && t2 != -1 && t22 != -1 && t2 != t22)
                                        return t1 > t2 || (t1 == t2 && (t11 > t22 || (t11 == t22 && compare(pp1, pp2))));
                                    else {

                                        t1 = isKind(pp1, 2, false);
                                        t2 = isKind(pp2, 2, false);

                                        if(t1 != -1 && t2 == -1) return true;
                                        else if(t1 == -1 && t2 != -1) return false;
                                        else if(t1 != -1 && t2 != -1) return t1 > t2 || (t1 == t2 && compare(pp1, pp2));
                                        else return compare(pp1, pp2);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    private static List<Integer> getPlayerValues(List<Integer> player) {
        List<Integer> p = new ArrayList<Integer>();
        for(int i : player) p.add(i%100);
        Collections.sort(p);
        return p;
    }

    private static boolean compare(List<Integer> p1, List<Integer> p2) {

        for(int i=p1.size()-1; i>=0; i--) {
            if(p1.get(i) > p2.get(i)) return true;
            else if(p1.get(i) < p2.get(i)) return false;
        }
        return true;
    }

    private static int isKind(List<Integer> player, int n, boolean reverse) {
        if(reverse) Collections.reverse(player);

        for(int i=player.size()-1; i>=0; i--) {
            if(count(player, player.get(i)) == n) return player.get(i);
        }
        return -1;
    }

    private static int count(List<Integer> player, int n) {
        int cnt = 0;
        for(int i : player) {
            if(i == n) cnt++;
        }
        return cnt;
    }

    private static boolean isRoyalFlush(List<Integer> player, List<Integer> playerSuit) {
        return isRoyal(player) && isStraightFlush(player, playerSuit);
    }

    private static boolean isStraightFlush(List<Integer> player, List<Integer> playerSuit) {
        return isStraight(player) && isFlush(playerSuit);
    }

    private static boolean isRoyal(List<Integer> player) {
        return player.get(0) == 10;
    }

    private static boolean isStraight(List<Integer> player) {
        int t = -1;
        for(int i : player) {
            if(t != -1 && t+1 != i) return false;
            t = i;
        }
        return true;
    }

    private static boolean isFlush(List<Integer> player) {
        int suit = player.get(0) / 100;
        for(int i=1; i<5; i++) {
            if (player.get(i) / 100 != suit) return false;
        }
        return true;
    }

    private static int cardValue(String s) {
        String vals = "--23456789TJQKA";
        String suits = "HCSD";
        return vals.indexOf(s.charAt(0)) + suits.indexOf(s.charAt(1)) * 100;
    }

}
